from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from PayPalApp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
	path('order/',views.order,name='order'),
	path('process-payment/', views.process_payment, name='process_payment'),
    path('payment-done/', views.payment_done, name='payment_done'),
    path('payment-cancelled/', views.payment_canceled, name='payment_cancelled'),

]