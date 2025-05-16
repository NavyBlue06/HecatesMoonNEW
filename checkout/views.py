from django.shortcuts import render, redirect, get_object_or_404
from .forms import OrderForm
from .models import Order
from cart.cart import Cart

def checkout(request):
    cart = Cart(request)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.save()
            # I’ll add line items + stripe here soon
            return redirect('checkout_success', order_number=order.order_number)
    else:
        form = OrderForm()

    context = {
        'form': form,
        'cart': cart,
    }

    return render(request, 'checkout/checkout.html', context)

def checkout_success(request, order_number):
    """ Display the success page after a successful checkout """
    order = get_object_or_404(Order, order_number=order_number)

    context = {
        'order': order,
    }

    return render(request, 'checkout/checkout_success.html', context)