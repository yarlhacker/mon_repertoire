from django.shortcuts import render
from . import models


def index(request):
    return render(request, 'index.html')

def detail(request):
    return render(request, 'detail.html')

def modifier(request):
    return render(request, 'modifier.html')

def ajouter(request):

    if request.method == "POST":
        nom  = request.POST.get('nom')
        prenom  = request.POST.get('prenom')
        email  = request.POST.get('email')
        contact  = request.POST.get('phone')
        photo  = request.FILES.get('photo')

        contact = models.ListContact(nom=nom,prenom=prenom,email= email,contact=contact,photo=photo)
        contact.save()
    return render(request, 'ajouter.html')
# Create your views here.
