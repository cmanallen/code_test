from django.db import models


class TimeStampedModel(models.Model):

	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True


class Loan(TimeStampedModel):

	title = models.CharField(max_length=100)
	principal = models.FloatField()
	interest_rate = models.FloatField()
	length = models.IntegerField()

	def __str__(self):
		return "Loan called %s" % self.title


class Payment(TimeStampedModel):

	loan = models.ForeignKey(Loan, related_name="payments")
	amount = models.FloatField()

	def __str__(self):
		return "Payment of %s to %s" % (self.amount, self.loan.title)