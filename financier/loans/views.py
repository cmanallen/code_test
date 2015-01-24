from rest_framework.viewsets import ModelViewSet

from .models import Loan, Payment
from .serializers import LoanSerializer, PaymentSerializer


class LoanViewSet(ModelViewSet):

	queryset = Loan.objects.all()
	serializer_class = LoanSerializer


class PaymentViewSet(ModelViewSet):

	queryset = Payment.objects.all()
	serializer_class = PaymentSerializer