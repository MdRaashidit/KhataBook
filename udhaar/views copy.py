from django.shortcuts import render
from .models import Party,Transactions

def home(request):
    all_party=Party.objects.all() 

    if request.method == "POST":
        amt = request.POST.get('formamount')
        idData=request.POST.get('formparty')
        
        ne = amt[0]
        account = Transactions.objects.filter(dbparty=idData)            
        if len(account)>0:
            if ne=='-':
                addparty=request.POST.get('formparty')
                addamount=request.POST.get('formamount')
                adddes=request.POST.get('description')
                adddate=request.POST.get('formdate')
                addtrans=request.POST.get('mytrans')
                party = Transactions.objects.filter(dbparty=idData).last()
                olderAmt = party.dbamount
                newAmt=int(olderAmt) + int(addamount)
                party = Party.objects.get(id=addparty)
                transactions_save = Transactions(dbparty=party,dbamount=newAmt,description=adddes,dbdate=adddate,trace=addtrans)
                transactions_save.save()

            else:
                addparty=request.POST.get('formparty')
                addamount=request.POST.get('formamount')
                adddes=request.POST.get('description')
                adddate=request.POST.get('formdate')
                addtrans=request.POST.get('mytrans')
                party = Transactions.objects.filter(dbparty=idData).last()
                olderAmt = party.dbamount
                newAmt=int(olderAmt) + int(addamount)
                party = Party.objects.get(id=addparty)
                transactions_save = Transactions(dbparty=party,dbamount=newAmt,description=adddes,dbdate=adddate,trace=addtrans)
                transactions_save.save()
                
        else:
            addparty=request.POST.get('formparty')
            addamount=request.POST.get('formamount')
            adddes=request.POST.get('description')
            adddate=request.POST.get('formdate')
            addtrans=request.POST.get('mytrans')
            party = Party.objects.get(id=addparty)
            transactions_save = Transactions(dbparty=party,dbamount=addamount,description=adddes,dbdate=adddate,trace=addtrans)
            transactions_save.save()
            
    
    
    context={'all_party':all_party}
    return render(request,'index.html',context)

def history(request):
    all_transaction=Transactions.objects.all()
    context={'all_transaction':all_transaction}
    return render(request,'balance.html',context)
