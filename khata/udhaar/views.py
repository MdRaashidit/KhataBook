from django.shortcuts import render, HttpResponse
from .models import Party,Transactions

def home(request):
    all_party=Party.objects.all() 
    if request.method == "POST":
        amt = request.POST.get('formamount')
        idData=request.POST.get('formparty')
        ne = amt[0]
        if ne=='-':
            party = Transactions.objects.filter(dbparty=idData).last()
            print(party)
            olderAmt = party.dbamount
            new = amt[1:]
            newAmt = int(olderAmt)-int(new) 
            party.dbamount = newAmt
            party.save()
            message = 'Data upated successfully !'
            context = {
                'message':message,
            }
            return render(request, 'index.html', context)
        else:
            addparty=request.POST.get('formparty')
            addamount=request.POST.get('formamount')
            adddes=request.POST.get('description')
            adddate=request.POST.get('formdate')
            party = Party.objects.get(id=addparty)
            transactions_save = Transactions(dbparty=party,dbamount=addamount,description=adddes,dbdate=adddate)
            transactions_save.save()
    
    context={'all_party':all_party}
    return render(request,'index.html',context)

