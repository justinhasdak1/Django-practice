#Correction file 
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.conf import settings


# Home page view
def home(request):
    return render(request, 'index.html')

def contact_view(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            print("✅ Form saved successfully!")

            # Send email
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            subject = f"New Contact Form Submission from {name}"
            body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
            recipient_list = [settings.EMAIL_HOST_USER]  # Send to your email

            send_mail(subject, body, settings.EMAIL_HOST_USER, recipient_list)

            return redirect('contact')

    return render(request, 'index.html', {'form': form})

