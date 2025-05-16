from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .forms import OrderForm
from .models import Order, OrderLineItem
from cart.cart import Cart
from boxes.models import Product


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

    # Context to send to the checkout template
    context = {
        'form': form,
        'cart': cart,
    }

    # Render the checkout page
    return render(request, 'checkout/checkout.html', context)


def checkout_success(request, order_number):
    """ Display the success page after a successful checkout """
    order = get_object_or_404(Order, order_number=order_number)

    context = {
        'order': order,
    }

    return render(request, 'checkout/checkout_success.html', context)
