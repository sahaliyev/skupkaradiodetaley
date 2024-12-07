from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator
from . import models


def robots_txt(request):
    content = (
        "User-agent: *\n"
        "Disallow: /admin/\n"
        "Allow: /\n"
        "Sitemap: https://www.skupkaradiodetaley.org/sitemaps.xml\n"
    )
    return HttpResponse(content, content_type="text/plain")


def index(request):
    contact_info = models.Contact.get_solo()
    contact_info = {
        "address": contact_info.address,
        "map_url": contact_info.map_address,
        "whatsap_numbers": contact_info.whatsap_number.split(",") if contact_info.whatsap_number else None,
        "call_numbers": contact_info.call_number.split(",") if contact_info.call_number else None,

    }
    keywords = list(models.Keyword.objects.filter(active=True).values_list('keyword', flat=True))
    keyword_str = ", ".join(keywords)
    context = {
        "images": models.Images.objects.filter(active=True),
        "contact_info": contact_info,
        "keyword_str": keyword_str
    }

    return render(request, 'index.html', context=context)


def return_images_as_json(request):
    images = models.Images.objects.filter(active=True)

    data = {
        "images": [
            {
                "name": image.name,
                "url": image.image.url,
            }
            for image in images
        ]
    }
    return JsonResponse(data)
