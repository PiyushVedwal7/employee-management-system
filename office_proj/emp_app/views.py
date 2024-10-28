from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from .models import Employee,Department,Role
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from datetime import datetime
from django.db.models import Q

# Create your views here.

def start(request):
    return render(request,'index.html')



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('start')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('start')





def all_emp(request):
    emps=Employee.objects.all()
    context={
        'emps':emps
    }
    print(context)
    return render(request,'view_all_emp.html',context)

def emp_profile(request, emp_id):
    emp = get_object_or_404(Employee, id=emp_id)
    context = {'emp': emp}
    return render(request, 'emp_profile.html', context)


def add_emp(request):

    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        salary=int(request.POST['salary'])
        bonus=int(request.POST['bonus'])

        phone=int(request.POST['phone'])
   
        dept=int(request.POST['dept'])
        role=int(request.POST['role'])

        new_employee=Employee(first_name=first_name,last_name=last_name,dept_id=dept,role_id=role,salary=salary,phone=phone,bonus=bonus,hire_date=datetime.now())
        new_employee.save()
        return HttpResponse("new employee added sucessfully")
    elif request.method=='GET':
          return render(request,'add_emp.html')



    else:
        return HttpResponse("error occured")
    



import csv
from django.http import HttpResponse

def export_emp(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="employees.csv"'
    writer = csv.writer(response)
    writer.writerow(['First Name', 'Last Name', 'Department', 'Role', 'Salary'])
    
    for emp in Employee.objects.all():
        writer.writerow([emp.first_name, emp.last_name, emp.dept.name, emp.role.name, emp.salary])
    
    return response



def landing_page(request):
    return render(request, 'landing_page.html')
   




def remove_emp(request,emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee Removed Successfully")
        except:
            return HttpResponse("Please Enter A Valid EMP ID")
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request, 'remove_emp.html',context)
    


def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if dept:
            emps = emps.filter(dept__name__icontains = dept)
        if role:
            emps = emps.filter(role__name__icontains = role)

        context = {
            'emps': emps
        }
        return render(request, 'view_all_emp.html', context)

    elif request.method == 'GET':
        return render(request, 'filter_emp.html')
    else:
        return HttpResponse('An Exception Occurred')



