from decimal import Decimal
from django.conf import settings
from boxes.models import Product  # still needed in case I'm adding physical products

class Cart:
    def __init__(self, request):
        # This gets the current user session
        self.session = request.session

        # Try to get the cart from session using the session key (e.g. 'cart')
        cart = self.session.get(settings.CART_SESSION_ID)

        # If cart doesn’t exist yet in session, initialize an empty one
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}

        # Save the cart dict into self.cart so I can use it in this object
        self.cart = cart

    def add(self, product, quantity=1):
        # Standard add-to-cart function for physical products (still kept for future use)
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {
                'quantity': 0,
                'price': str(product.price)
            }

        # Increase the quantity
        self.cart[product_id]['quantity'] += quantity
        self.save()

    def remove(self, item_key):
        # New version of remove – works for both product and service keys (like 'service-birthchart-2')
        if item_key in self.cart:
            del self.cart[item_key]
            self.save()

    def save(self):
        # Mark the session as modified so it gets saved
        self.session.modified = True

    def __iter__(self):
        for key, item in self.cart.items():
            if key.startswith('service-'):
                # It's a service item, already contains name & price
                item['key'] = key
                item['total_price'] = Decimal(item['price']) * item['quantity']
                yield item
            else:
                # It's a product from Product model
                product = Product.objects.get(id=key)
                item['product'] = product
                item['name'] = product.name
                item['key'] = key
                item['total_price'] = Decimal(item['price']) * item['quantity']
                yield item



    def get_total_price(self):
        # Total cost of everything in the cart
        return sum(
            Decimal(item['price']) * item['quantity']
            for item in self.cart.values()
        )

    def clear(self):
        # Completely remove the cart from session
        self.session[settings.CART_SESSION_ID] = {}
        self.save()
