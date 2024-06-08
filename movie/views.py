from django.shortcuts import render
from .models import *
from django.db.models import Q

# Create your views here.

def index(request):
    return render(request,"index.html")
def browse_index(request):
    # 获取所有的类别 (tüm kategorileri al demekmiş geleneksel çincede)
    filmler=Movies.objects.all()
    search=""
    context={}
    if request.GET.get("search"):
        search=request.GET.get("search")
        filmler=filmler.filter(
            Q(isim__icontains=search) |
            Q(kategori__name__icontains=search)
        )

    context={
        'filmler':filmler
    }
    return render(request,"browse-index.html",context)