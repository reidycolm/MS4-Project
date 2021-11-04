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