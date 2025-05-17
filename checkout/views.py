from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from .forms import OrderForm
from .models import Order, OrderLineItem
from cart.cart import Cart
from boxes.models import Product
from django.conf import settings
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

def checkout(request):
    # Create a Cart instance from the session
    cart = Cart(request)

    # If this is a POST request, process the form
    if request.method == 'POST':
        form = OrderForm(request.POST)

        # Check if form is valid
        if form.is_valid():
            # Save order data without committing to DB yet
            order = form.save(commit=False)
            order.save()

            # Create order line items for each item in cart
            for item in cart:
                # Only handle line items with a product_id (skip services etc.)
                if 'product_id' in item:
                    product = Product.objects.get(id=item['product_id'])
                    OrderLineItem.objects.create(
                        order=order,
                        product=product,
                        quantity=item['quantity']
                    )

            # Once order and items are created, redirect to success page
            return redirect('checkout_success', order_number=order.order_number)
    else:
        # If it's a GET request, show a blank form
        form = OrderForm()

    # Calculate total amount in cents for Stripe
    total = int(cart.get_total_price() * 100)

    # Create PaymentIntent with Stripe
    intent = stripe.PaymentIntent.create(
        amount=total,
        currency='eur',
    )

    # Context to send to the checkout template
    context = {
        'form': form,
        'cart': cart,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,  # Required for JS
        'client_secret': intent.client_secret,            # Needed for confirmCardPayment()
    }

    # Render the checkout page
    return render(request, 'checkout/checkout.html', context)
