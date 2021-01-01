from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .models import Event
from math import ceil


def gallery(request):
    all_img = []
    bhatt = Event.objects.values('title','id')
    img_tit = { item['title']  for item in bhatt}
    for title in img_tit:
     imge = Event.objects.filter(title=title)
     n = len(imge)
     nSlides = n // 4 + ceil((n / 4) - (n // 4))
     all_img.append([imge])
     params = {'all_img': all_img}

    return render(request, 'neelamtenthouse/gallery.html',params)
def index(request):
    all_img = []
    bhatt = Event.objects.values('title', 'id')
    img_tit = {item['title'] for item in bhatt}
    for title in img_tit:
        imge = Event.objects.filter(title=title)
        n = len(imge)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        all_img.append([imge])
        params = {'all_img': all_img}
        print(params)
    return render(request,'neelamtenthouse/index.html',params)
def contact(request):
    return HttpResponse("We are here!.")
def faq(request):
    return HttpResponse("your queries!")