from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from .models import MessagesList


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Save the message to the database
        new_message = MessagesList(
            name=name,
            email=email,
            phone=phone,
            subject=subject,
            message=message
        )
        new_message.save()

        # Send a success message in JSON response
        return JsonResponse({'success': True, 'message': 'Your message has been sent successfully.'})

    return render(request, 'contact/contact.html')
