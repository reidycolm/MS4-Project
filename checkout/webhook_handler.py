from django.http import HttpResponse


class StripeWH_Handler:
    """ a class to handle stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
            Handles a generic or unknown webhook event
        """
        return HttpResponse(
            content=f'Unhandled Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """"
            Handles payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        print(intent)
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_failed(self, event):
        """
            Handles payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
