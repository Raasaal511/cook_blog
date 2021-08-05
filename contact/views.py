from django.shortcuts import render
from django.views import View

from .forms import ContactForm
from .models import ContactLink, About

from django.views.generic import CreateView


class ContactView(View):

    def get(self, request):
        contacts = ContactLink.objects.all()
        form = ContactForm()

        context = {
            'contacts': contacts,
            'form': form
        }

        return render(request, 'contact/contact.html', context)


class CreateContact(CreateView):
    form_class = ContactForm
    success_url = '/'


class AboutView(View):

    def get(self, request):
        about = About.objects.last()

        return render(request, 'contact/about.html', {'about': about})

