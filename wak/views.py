from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from wak.models import Categoria,Vaca,Producto
# Create your views here.
from datetime import date
class IndexView(TemplateView):
    template_name = 'intro.html'

def logOut(request):
    from django.contrib.auth import logout
    logout(request)
    return redirect('/login')

def IntroView(request):
    chauchas = Producto.objects.all().filter(categoria__nombre='Chauchitas')
    print chauchas
    vacas = Producto.objects.all().filter(categoria__nombre='La Vaca')
    return render(request,'index1.html',{'chauchas':chauchas,'vacas':vacas})

def ingresoVaca(request):
    if(request.method == 'POST'):
        print "Dentro de POST"
        categoria = Categoria.objects.all()
        creacion = Producto(titulo=request.POST.get('exampleInputEmail1'),descripcion=request.POST.get('exampleTextarea'),foto=request.FILES['exampleInputFile'],oferta=request.POST.get('exampleOferta'),lon=2.3, lat=3.4,categoria_id=request.POST.get('exampleSelect1'))
        creacion.save()
        estado = True
        return render(request,'Ingreso.html',{'categoria':categoria,'estado':estado})
    else:
        categoria = Categoria.objects.all()
        return render(request,'Ingreso.html',{'categoria':categoria})
