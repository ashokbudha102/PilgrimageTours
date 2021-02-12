from django.shortcuts import render, redirect
import requests as req
from .models import Transaction,Serial
import random,hashlib
from django.contrib.auth import get_user_model
from Products_Details.models import Destination

User=get_user_model()
pid=''

# Create your views here.
#AT login required
def epay(request,slug):
    user=request.user
    #print(request.user)
    des=Destination.objects.get(slug=slug)
    print(des.pk)
    ser=Serial()
    ser.save()
    global pid
    pid = str('000000'+str(des.pk))[-6:]+str('000000'+str(user.pk))[-6:]+str('000000'+str(ser.pk))[-6:]#destination+userid+serial
    h=hashlib.sha1(pid.encode()).hexdigest()
    return render(request,'esewa/esewa.html',{'pid':h,'data':des})


#return from esewa payment
#def check(request):
#    rid=request.GET['refId']
#    p=request.GET['oid']
#    #print(p)
#    #print(hashlib.sha1(pid.encode()).hexdigest())
#    if(p==str(hashlib.sha1(pid.encode()).hexdigest())):
#        url = "https://uat.esewa.com.np/epay/transrec"
#        d = {
#            'amt': 100,
#            'scd': 'EPAYTEST',
#            'rid': rid,
#            'pid': p,
#        }
#        resp = req.post(url, d)
#        print(resp.text)
#        if('Success' in resp.text):
#            trans=Transaction(pid=p,rid=rid,tamt=100)
#            #save on destination of user model
#            trans.save()
#            return redirect('success')
#        else:
#            return redirect('failed')
#    else:
#        #print('error')
#        return redirect('failed')

#Only after paid, and check verification this url should be accessed, check if the payment is verified
def success(request):
    rid = request.GET['refId']
    p = request.GET['oid']
    print(pid[0:6])
    des=Destination.objects.get(pk=(int(pid[0:6])))
    if(Transaction.objects.filter(rid=rid).exists()):
        return render(request, 'esewa/success.html', {'data':des})
    else:
        print(p)
        print(hashlib.sha1(pid.encode()).hexdigest())
        if (p == str(hashlib.sha1(pid.encode()).hexdigest())):  # checking if the returned value is correct
            url = "https://uat.esewa.com.np/epay/transrec"
            d = {
                'amt': 100,  # this amount should be included from destination amt from database
                'scd': 'EPAYTEST',
                'rid': rid,
                'pid': p,
            }
            resp = req.post(url, d)
            print(resp.text)
            if ('Success' in resp.text):
                trans = Transaction(pid=p, rid=rid, tamt=100)
                # save what destination has user paid for in database of user paid destination
                trans.save()
                return render(request, 'esewa/success.html', {'data':des})
            else:
                return redirect('failed')
        else:
            # print('error')
            return redirect('failed')



#Return from esewa payment(in case of failed payment)
def failed(request):
    return render(request,'esewa/failed.html',{})