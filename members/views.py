# members/views.py
from django.shortcuts import render, redirect
from .models import Member, Car

def member_list(request):
    members = Member.objects.all()
    return render(request, 'members/member_list.html', {'members': members})

def add_member(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        Member.objects.create(name=name, age=age, gender=gender)
        return redirect('member_list')
    return render(request, 'members/add_member.html')

def delete_member(request, member_id):
    member = Member.objects.get(id=member_id)
    member.delete()
    return redirect('member_list')

def car_list(request):
    cars = Car.objects.all()
    return render(request, 'members/car_list.html', {'cars': cars})

def add_car(request):
    if request.method == 'POST':
        brand = request.POST.get('brand')
        year = request.POST.get('year')
        color = request.POST.get('color')
        price = request.POST.get('price')
        discount = request.POST.get('discount')
        Car.objects.create(brand=brand, year=year, color=color, price=price, discount=discount)
        return redirect('car_list')
    return render(request, 'members/add_car.html')

def delete_car(request, car_id):
    car = Car.objects.get(id=car_id)
    car.delete()
    return redirect('car_list')
