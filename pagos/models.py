from django.db import models
from decimal import Decimal

from payments import PurchasedItem
from payments.models import BasePayment

class Pago(BasePayment):

    def get_failure_url(self):
        # Return a URL where users are redirected after
        # they fail to complete a payment:
        return f"http://example.com/payments/{self.pk}/failure"

    def get_success_url(self):
        # Return a URL where users are redirected after
        # they successfully complete a payment:
        return f"http://example.com/payments/{self.pk}/success"

    def get_purchased_items(self):
        # Return items that will be included in this payment.
        yield PurchasedItem(
            #name='The Hound of the Baskervilles',
            name = 'Club de socios,'
            sku='BSKV',
            quantity=9,
            price=Decimal(10),
            currency='ARS',
        )
