from django.shortcuts import render, HttpResponse,get_object_or_404
from .models import modelo

# Create your views here.
def inicio(request):
    return render(request,'core/inicio.html')
def publicaciones(request):
    bd= modelo.objects.all()
    return render(request,'core/publicaciones.html',{'bd':bd})
def detalle(request, id):
    bd = get_object_or_404(modelo, id=id)
    return render(request,"core/detalle.html",{'bd':bd})
