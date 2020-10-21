from django.shortcuts import render

from django.contrib import messages
from django.conf import settings
from decimal import Decimal
from paypal.standard.forms import PayPalPaymentsForm
from django.shortcuts import redirect
from paypal.standard.forms import PayPalPaymentsForm
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
def order(request):
	if request.method == 'POST':

		Amount = request.POST.get("amount")
		Ordersession = request.session.get("Ordersession")
		if Ordersession:
			Ordersession["Amount"] = Amount
			request.session["Ordersession"] = Ordersession
		else:
			Ordersession = {}
			Ordersession.update({"Amount":Amount})
			request.session["Ordersession"] = Ordersession
		return redirect("process_payment")

		
	else:
		return render(request, 'order.html')


def process_payment(request):
	Ordersession = request.session.get('Ordersession')
	Amount = Ordersession["Amount"]
	host = request.get_host()

	paypal_dict = {
		'business': settings.PAYPAL_RECEIVER_EMAIL,
		'amount': Amount,
		'item_name': 'Chair',
		'invoice': str(Amount),
		'currency_code': 'INR',
		'notify_url': 'http://{}{}'.format(host,
										   reverse('paypal-ipn')),
		'return_url': 'http://{}{}'.format(host,
										   reverse('payment_done')),
		'cancel_return': 'http://{}{}'.format(host,
											  reverse('payment_cancelled')),
	}

	form = PayPalPaymentsForm(initial=paypal_dict)
	return render(request, 'process_payment.html', {'order': order, 'form': form})



@csrf_exempt
def payment_done(request):
	return render(request, 'paymentdone.html')


@csrf_exempt
def payment_canceled(request):
	return render(request, 'payment_cancelled.html')


