from rest_framework.serializers import (
	ModelSerializer, HyperlinkedModelSerializer
)

from .models import Loan, Payment


class PaymentSerializer(ModelSerializer):
	"""
	Returns serialized Payment model
	"""
	class Meta:
		model = Payment
		fields = ('id', 'loan', 'amount', 'created')


class LoanSerializer(HyperlinkedModelSerializer):

	payments = PaymentSerializer(many=True, read_only=True)

	class Meta:
		model = Loan
		fields = (
			'url', 'id', 'title', 'principal', 'interest_rate', 'length',
			'payments'
		)