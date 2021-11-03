from django.http import HttpResponse
from django.shortcuts import render
from .models import Client


# Create your views here.
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def liste_client(request,pk):
    client=Client.objects.get(id=pk)
    commande=client.commande_set.all()
    total_commande=commande.count()
    context={'client':client,'commande':commande,'total':total_commande}
    return render(request,'client/client.html',context)
