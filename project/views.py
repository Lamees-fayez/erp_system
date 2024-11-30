from django.shortcuts import render , redirect
from pages.models import Employee
from pages.forms import EmployeeForm
# retrieve all
def home(request):
    employee=Employee.objects.all()
    context={'employee':employee}
    return render(request, 'home.html', context)

def detail(request,id):
    employee = Employee.objects.get(id=id)
    return render(request, 'detail.html',{'employee':employee})

def update (request,id):
    employee = Employee.objects.get(id=id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
            return redirect('detail' ,employee.id)
    form = EmployeeForm(instance=employee)
    return render(request, 'update.html', {'form': form })

def delete(request,id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('home')
def add_emp(request):
    if request.method == 'POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form=EmployeeForm()    
    
    return render(request ,'add_emp.html',{'form': form} )  