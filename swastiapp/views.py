from django.shortcuts import render
import razorpay


# Create your views here.

def index(request):
    return render(request, "index.html")


def payment(request):
    if request.method == 'POST':
        client = razorpay.Client(auth=("rzp_live_c3Tu4t0RwnyP12", "EW1Zy2lQ2T3oKwkAs3pble4I"))

        DATA = {
            "amount": 100,
            "currency": "INR",
            "receipt": "receipt#1",
            "notes": {
                "key1": "value3",
                "key2": "value2"
            }
        }
        client.order.create(data=DATA)
    return render(request, "index1.html")


def success(request):
    return render(request, "success.html")
