from django.db import models

# Create your models here.
CATEGORY = (("revo","リボ"), ("installment_payment","分割払"))
class Debt(models.Model):
    lender = models.CharField(max_length=200)
    total_amount = models.IntegerField(default=0)
    interest_rate = models.FloatField()
    manthly_repayment = models.IntegerField(default=0)
    repayment_method = models.CharField(max_length=50, choices=CATEGORY)

    def __str__(self):
        return self.lender