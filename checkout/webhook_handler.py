# webhook_handler.py
# this file handles incoming Stripe webhooks like payment success/failure

from django.http import HttpResponse
import json
import stripe
from .models import Order


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        # handle a generic/unknown webhook event
        return HttpResponse(content=f'Unhandled webhook received: {event["type"]}', status=200)

    def handle_payment_intent_succeeded(self, event):
        # this will run when Stripe confirms payment success
        intent = event.data.object
        pid = intent.id
        # maybe later I’ll link the PID to the order if I store it

        print(f"💸 PaymentIntent succeeded: {pid}")
        return HttpResponse(content=f'Webhook received: {event["type"]}', status=200)

    def handle_payment_intent_payment_failed(self, event):
        # logs if payment failed
        return HttpResponse(content=f'Payment failed webhook received: {event["type"]}', status=200)
