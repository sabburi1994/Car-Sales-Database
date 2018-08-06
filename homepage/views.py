# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.
from .forms import CarForm
from .models import Car

def add_car(request):
    if request.method == 'POST':  # data sent by user
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()  # this will save Car info to database
            return render(request,'saved.html')
    else:  # display empty form
        form = CarForm()
    return render(request, 'add_car.html', {'car_form': form})

def car_details(request):
    car_billing_number = request.GET['car_billing_number']
    return render(request, 'car_list.html', {
        'car': Car.objects.get(pk=car_billing_number)
    })
