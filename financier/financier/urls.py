from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework.routers import DefaultRouter

from loans.views import LoanViewSet, PaymentViewSet


router = DefaultRouter()
router.register(r'loan', LoanViewSet)
router.register(r'payment', PaymentViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'financier.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^api/v1/', include(router.urls)),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
