from django.shortcuts import render

# Create your views here.
from .models import Donation

def donation_list_view(request):
    donation_objects = Donation.objects.all()
    context = {
        'donation_objects': donation_objects
    }
    return render(request, "donations/index.html", context)