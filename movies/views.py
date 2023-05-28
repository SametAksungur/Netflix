from django.shortcuts import render, redirect
from .models import *
from user.models import *
from django.contrib.auth.models import User
# Create your views here.


def index(request):
    return render(request, 'index.html')


def movies(request, slug, profilId):
    profil = profile.objects.get(id=profilId, slug=slug)
    profiller = profile.objects.filter(olusturan=request.user)
    filmler = Movie.objects.all()
    populer = Movie.objects.filter(kategori__isim="Popüler")
    gundemde = Movie.objects.filter(kategori__isim="Gündemde")
    context = {
        'filmler': filmler,
        'populer': populer,
        'gundemde': gundemde,
        'profil': profil,
        'profiller': profiller
    }
    return render(request, 'browse-index.html', context)


def view_404(request, exception):
    return redirect('/')
