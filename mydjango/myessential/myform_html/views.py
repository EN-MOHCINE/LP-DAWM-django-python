from django.shortcuts import render, redirect
from .models import Car

def add_car(request):
    if request.method == 'POST':
        brand = request.POST.get('brand')
        year = request.POST.get('year')
        Car.objects.create(brand=brand, year=year)
        return redirect('myform_html:list_cars')
    return render(request, 'myform_html/add.html')

def list_cars(request):
    all_cars = Car.objects.all()
    return render(request, 'myform_html/list.html', {'all_cars': all_cars})

def delete_car(request):
    if request.method == 'POST':
        pk = request.POST.get('pk')
        try:
            car = Car.objects.get(pk=pk)
            car.delete()
            return redirect('myform_html:list_cars')
        except Car.DoesNotExist:
            return HttpResponse("Car not found")
    return render(request, 'myform_html/delete.html')