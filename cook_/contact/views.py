from django.shortcuts import render
from django.views.generic import CreateView
from django.views import View
from .models import ContactLink, About
from .forms import ContactForm 

class ContactView(View):

    def get(self, request):
        contacts = ContactLink.objects.all()
        form = ContactForm()
        return render(request, 'contact/contact.html', {"contacts": contacts, "form": form})

class CreateContact(CreateView):
    form_class = ContactForm
    success_url = '/'
    template_name = 'contact/contact.html'

class AboutView(View):
    def get(self, request):
        about = About.objects.last()
        return render(request, 'contact/about.html', {"about": about})
