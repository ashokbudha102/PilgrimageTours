from django.shortcuts import render
from Products_Details.models import Destination,Add_category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from Login.forms import Login_Form

def home_list(request):
    context=Destination.objects.all()[0:6]
    form=Login_Form()
    return render(request,'Home/home.html',{'products':context,'form':form})

def home_detail_view(request,slug):
    data=Destination.objects.get(slug=slug)
    data2=data.additional_feature.all()
    return render(request,'Home/home_detail.html',{'data':data,'data2':data2})

def categoricalSorting(request, slug):
    posts=Destination.objects.filter(categories__slug=slug)
    return render(request, 'Home/categorial.html',{'posts':posts})

def PackagesView(request):
    dest = Destination.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(dest, 3)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
        
    context={"Destination":users,
             "Add_category":Add_category.objects.all()   
    }
    return render(request,'Home/packages.html',context)