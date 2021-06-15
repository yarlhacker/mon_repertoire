from django.shortcuts import get_object_or_404, redirect, render
from . import models
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import User





def login_views(request):

    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        name = request.POST['username']
        pwd = request.POST['password']
        user = authenticate(username=name, password=pwd)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            message = 'error'

    return render(request, 'login.html',locals())

def logout_view(request):

    logout(request)

    return redirect('login')





def index(request):
    if request.user.is_authenticated:
        contacts = models.ListContact.objects.filter(status=True)
    return render(request, 'index.html',locals())

def detail(request ,id):
    contact = get_object_or_404(models.ListContact , id =id )
    return render(request, 'detail.html',locals())

def modifier(request ,id ):
    contact = get_object_or_404(models.ListContact , id =id )

    if request.method == "POST":
        contact.nom  = request.POST.get('nom')
        contact.prenom  = request.POST.get('prenom')
        contact.email  = request.POST.get('email')
        contact.contact  = request.POST.get('phone')
        contact.photo  = request.FILES.get('photo')
        contact.save()
        
        return redirect('/detail/'+ str(contact.id))
    return render(request, 'modifier.html',locals())

def ajouter(request):

    if request.method == "POST":
        nom  = request.POST.get('nom')
        prenom  = request.POST.get('prenom')
        email  = request.POST.get('email')
        contact  = request.POST.get('phone')
        photo  = request.FILES.get('photo')

        contact = models.ListContact(nom=nom,prenom=prenom,email= email,contact=contact,photo=photo)
        contact.save()
        return redirect('index')
    return render(request, 'ajouter.html')


def supprimer(request, id):
    contact = get_object_or_404(models.ListContact , id =id )
    
    if request.method == "POST":
        
        contact.delete()

        return redirect('index')
    return render(request, 'supprimer.html')


# Create your views here.
