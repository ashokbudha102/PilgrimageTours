from django.shortcuts import render
from .models import about
# Create your views here.
def about_view(request):
    context={'about':about.objects.all()}
    return render(request,'About/about.html',context)