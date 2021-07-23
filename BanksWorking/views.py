from django.shortcuts import render
from . models import Customer,Transaction
from datetime import datetime

# Create your views here.
def index(request):
    return render(request,'index.html')


def view_customer(request):
    customer = Customer.objects.all() 
    return render(request,'view.html',{'vc':customer})
    
    
def make_transaction(request):
    customer = Customer.objects.all()

    if request.method == 'POST':
        sname = request.POST.get('sname')
        rname = request.POST.get('rname')
        money = float(request.POST.get('amount'))
        scust = Customer.objects.get(name=sname)
        scust.amount = (scust.amount-money)
        scust.save()
        rcust = Customer.objects.get(name=rname)
        rcust.amount = (rcust.amount+money)
        rcust.save()    
        transfer = Transaction(sname=sname,rname=rname,money=money,tdate=datetime.today())
        transfer.save()       
        return render(request, 'success.html')
    # else:
    return render(request,'transfer.html',{'vc':customer})

def success(request):
    return render(request,'success.html')


def history(request):
    transaction = Transaction.objects.all().order_by('-id')
    return render(request,'history.html',{'tc':transaction})
