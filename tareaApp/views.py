from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

lista_tareas = [
    ['DESCANSAR','20-12-2024','EN PROGRESO','ALEXANDER'],
  
]

# Create your views here.
def index(request):
    return render(request,'index.html',{
        'lista_tareas':lista_tareas
    })

def nuevaTarea(request):
    if request.method == 'POST':
        print(request.POST)
        nombre = request.POST.get('nombre')
        fechaFin = request.POST.get('fecha')
        descripcion = request.POST.get('descripcion')
        
        print(nombre)
        print(fechaFin)
        print(descripcion)
        lista_tareas.append([nombre,descripcion,fechaFin,'Responsable'])
        return HttpResponseRedirect(reverse('tareaApp:index'))
    return render(request,'nuevaTarea.html')
