from django.shortcuts import render, HttpResponse
from .models import Employee, Role , Department
from datetime import datetime 
from django.db.models import Q


# Create your views here.
def index(request):
    return render(request,'index.html')

def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    print(context)
    return render(request,'view_all_emp.html',context)

def add_emp(request):
    depts = Department.objects.all()
    roles= Role.objects.all()
    context = {
        'depts': depts,
        'roles' : roles
    }

    if request.method == 'POST':
       First_Name = request.POST['First_Name']
       Last_Name = request.POST['Last_Name']
       Salary = int(request.POST['Salary'])
       Bonus = int(request.POST['Bonus'])
       Phone = int(request.POST['Phone'])
       department = int(request.POST['department'])
       role = int(request.POST['role'])
       new_emp = Employee(First_Name= First_Name, Last_Name= Last_Name, Salary=Salary, Bonus=Bonus, Phone=Phone,department_id = department,role_id = role,Hire_Date = datetime.now() )
       new_emp.save()
       return HttpResponse("Employee Added successfully")
    elif request.method=='GET':
    
        return render(request, 'add_emp.html', context)
    else:
        return HttpResponse("An exception occured ! employee has not been added")

def remove_emp(request, emp_id = 0):
    if emp_id:
        try:
           emp_to_be_removed =  Employee.objects.get(id=emp_id)
           emp_to_be_removed.delete()
           return HttpResponse("Employee Remove successfully!!")
        
        except:
            return HttpResponse("Please Enter A Valid Employee ID.")
            
    emps = Employee.objects.all()
    context = {
        'emps':emps
    }
    return render(request,'remove_emp.html', context)

def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['Name']
        department = request.POST['department']
        role = request.POST['role']
        emps =Employee.objects.all()
        if name:
            emps = emps.filter(Q(First_Name__icontains = name) | Q(Last_Name__icontains = name))
        if Department:
            emps = emps.filter(department__Name__icontains = department)
            
        if Role:
            emps = emps.filter(role__Name__icontains = role)
            
        context = {
            'emps' : emps
        }
        return render(request, 'view_all_emp.html', context)
        
    elif request.method == 'GET':
        return render(request, 'filter_emp.html')
    else:
        return HttpResponse("An Exception Accurred")
            