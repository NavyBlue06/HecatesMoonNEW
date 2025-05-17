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
    cart = Cart(request)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.save()

            for item in cart:
                if 'product_id' in item:
                    product = Product.objects.get(id=item['product_id'])
                    OrderLineItem.objects.create(
                        order=order,
                        product=product,
                        quantity=item['quantity']
                    )

            return redirect('checkout_success', order_number=order.order_number)
    else:
        form = OrderForm()

    context = {
        'form': form,
        'cart': cart,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,  # Required for JS
    }

    return render(request, 'checkout/checkout.html', context)


def checkout_success(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    context = {
        'order': order,
    }

    return render(request, 'checkout/checkout_success.html', context)


@require_POST
def create_checkout_session(request):
    """ Create a Stripe Checkout session for client-side redirect """
    cart = Cart(request)
    line_items = []

    for item in cart:
        line_items.append({
            'price_data': {
                'currency': 'eur',
                'unit_amount': int(item['price'] * 100),
                'product_data': {
                    'name': item['name'],
                },
            },
            'quantity': item['quantity'],
        })

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=line_items,
        mode='payment',
        success_url=request.build_absolute_uri('/checkout/checkout-success/') + '?session_id={CHECKOUT_SESSION_ID}',
        cancel_url=request.build_absolute_uri('/cart/'),
    )

    return JsonResponse({'id': session.id})
