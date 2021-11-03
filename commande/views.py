from django.http import HttpResponse
from django.shortcuts import render, redirect
#
from django.views.decorators.csrf import csrf_exempt
from .forms import Formulaire
from .models import Commande


@csrf_exempt
def liste_commande(request):
    return render(request,'commande/commande.html')

@csrf_exempt
def ajouter_commande(request):
    form =Formulaire()
    if request.method=='POST':
        form=Formulaire(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'commande/ajouter_commande.html',context)

@csrf_exempt
def modifier_commande(request,pk):
    commande=Commande.objects.get(id=pk)
    form =Formulaire(instance=commande)
    if request.method=='POST':
        form=Formulaire(request.POST,instance=commande)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'commande/ajouter_commande.html',context)

def supprimer_commmande(request,pk):
    commande=Commande.objects.get(id=pk)
    if request.method=='POST':
        commande.delete()
        return redirect('/')
    context={'item':commande}
    return render(request,'commande/modifier_commande.html', context)