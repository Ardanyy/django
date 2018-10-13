from django.shortcuts import render, get_object_or_404
from .models import Post
from django.template import RequestContext
from .forms import PageCreate
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.shortcuts import redirect
from django.conf import settings




def post(request):
    proyectos= Post.objects.filter(published_date__isnull=False)
    return render(request,"paginas/post.html",{'proyectos':proyectos})



@login_required(login_url='/login/')
def publicar(request, id):
    post = get_object_or_404(Post, id=id)
    post.published_date=timezone.now()
    post.save()
    return render(request,"paginas/post.html",{'post':post})

@login_required(login_url='/login/')
def eliminar(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return render(request,"paginas/post.html",{'post':post})



def detalle(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, "paginas/detalle.html", {'detalle':post})



@login_required(login_url='/login/')
def borradores(request):
      post = Post.objects.filter(published_date__isnull=True).order_by('published_date')
      return render(request,'paginas/borrador.html',{'post':post})

@login_required(login_url='/login/')
def post_new(request):
     proyectos= Post.objects.all()
     if request.method=="POST":
          form = PageCreate(request.POST)
          if form.is_valid():
            post=form.save(commit=False)
            post.Titulo=request.user
            post.save()
            return render(request,'paginas/borrador.html',{'proyectos':proyectos})
    
     else:
            form= PageCreate()
            return render(request,"paginas/post_form.html",{'form':form})

   

@login_required(login_url='/login/')
def post_detalle(request,id):
     post = get_object_or_404(Post, id=id)
     if request.method=="POST":
          form = PageCreate(request.POST, instance=post)
          if form.is_valid():
            post=form.save(commit=False)
            post.Titulo=request.user
            post.save()
            return render(request, "paginas/detalle.html", {'detalle':post})
    
     else:
            form= PageCreate(instance=post)
            return render(request,"paginas/post_form.html",{'form':form})
  
