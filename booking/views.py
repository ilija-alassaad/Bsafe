# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import AppointmentForm
from .models import Appointment, Client
from django.http import HttpResponse


def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            client_name = form.cleaned_data['client_name']
            client_email = form.cleaned_data['client_email']
            available_time = form.cleaned_data['available_time']
            client, created = Client.objects.get_or_create(
                name=client_name, email=client_email)
            appointment = Appointment(
                client=client,
                administrator=available_time.administrator,
                available_time=available_time
            )
            appointment.save()
            return redirect('home:home')
    else:
        form = AppointmentForm()
    return render(request, 'booking/book_appointment.html', {'form': form})


def appointment_success_view(request):
    return HttpResponse("Appointment booked successfully!")
