from django.shortcuts import render, redirect
from .models import Teacher
from django.contrib import messages

# Create your views here.
def createView(request):
    return render(request, 'create.html')

def store(request):
    teacher = Teacher()
    teacher.name = request.POST.get('emp_name')
    teacher.age = request.POST.get('emp_age')
    teacher.save()
    messages.success(request, "Teacher added succesfully")
    return redirect('/')

def index(request):
    emp = Teacher.objects.all()
    return render(request, 'index.html', {'emp':emp})

def viewEmp(request, pk):
    emp =  Teacher.objects.get(id=pk)
    return render(request, 'view.html', {'emp':emp})

def deleteEmp(request, pk):
    emp = Teacher.objects.get(id=pk)
    emp.delete()
    messages.success(request, "Employee deleted successfully")
    return redirect('/')

def updateView(request, pk):
    emp = Teacher.objects.get(id=pk)
    return render(request, 'update.html', {'emp':emp})

def updateEmp(request, pk):
    emp = Teacher.objects.get(id=pk)
    emp.name = request.POST.get('emp_name')
    emp.age = request.POST.get('emp_age')
    emp.save()
    messages.success(request, "Employee updated")
    return redirect('/')
