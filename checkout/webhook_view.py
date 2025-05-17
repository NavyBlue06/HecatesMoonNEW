# checkout/webhook_view.py

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import stripe
from django.conf import settings

from .webhook_handler import StripeWH_Handler


@csrf_exempt
def stripe_webhook(request):
    """Listen for webhooks from Stripe"""
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WH_SECRET
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Set up a webhook handler
    handler = StripeWH_Handler(request)

    # Map webhook events to relevant handler functions
    event_map = {
        'payment_intent.succeeded': handler.handle_payment_intent_succeeded,
        'payment_intent.payment_failed': handler.handle_payment_intent_failed,
    }

    # Get event type from Stripe
    event_type = event['type']

    # If there's a handler for it, call it
    event_handler = event_map.get(event_type, handler.handle_event)
    response = event_handler(event)
    return response
