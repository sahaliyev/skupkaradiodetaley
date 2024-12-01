from django.shortcuts import render
from . import models


# Create your views here.
def index(request):
    contact_info = models.Contact.get_solo()
    contact_info = {
        "address": contact_info.address,
        "map_url": contact_info.map_address,
        "whatsap_numbers": contact_info.whatsap_number.split(",") if contact_info.whatsap_number else None,
        "call_numbers": contact_info.call_number.split(",") if contact_info.call_number else None,

    }
    context = {
        "images": models.Images.objects.filter(active=True),
        "contact_info": contact_info}
    return render(request, 'index.html', context=context)
