from django.shortcuts import render
from Products_Details.models import Destination

def home_list(request):
    context=Destination.objects.all()[0:6]
    return render(request,'Home/home.html',{'products':context})

def home_detail_view(request,slug):
    data=Destination.objects.get(slug=slug)
    data2=data.additional_feature.all()
    return render(request,'Home/home_detail.html',{'data':data,'data2':data2})