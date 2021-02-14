from django.shortcuts import render
from Products_Details.models import Destination
from django.db.models import Q

def home_list(request):
    context=Destination.objects.all()[0:6]
    return render(request,'Home/home.html',{'products':context})

def home_detail_view(request,slug):
    data=Destination.objects.get(slug=slug)
    data2=data.additional_feature.all()
    return render(request,'Home/home_detail.html',{'data':data,'data2':data2})

def categoricalSorting(request, slug):
    posts=Destination.objects.filter(categories__slug=slug)
    return render(request, 'Home/categorial.html',{'posts':posts})


def search(request):
    queryset=Destination.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        ).distinct()
    context = {
        'queryset': queryset
    }
    return render(request, 'Home/search_result.html', context)
