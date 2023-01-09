from django.core.mail import send_mail
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from Ninom import settings
from . import models, forms


# Create your views here.

class Index(generic.CreateView):
    template_name = 'index.html'
    model = models.contacto
    form_class = forms.contactoForm
    success_url = reverse_lazy('index')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Index, self).get_context_data()
        context['title'] = 'Ninom'
        context['encabezado'] = models.titulo.objects.all().first
        context['carrusel1'] = models.carrusel1.objects.all()
        context['navbar'] = models.navbar.objects.all().first
        context['shop'] = models.shop.objects.all().first
        context['about'] = models.about.objects.all().first
        context['titleFruit'] = models.fruitTitle.objects.all().first
        context['fruits'] = models.fruit.objects.all()
        context['titleTestimonial'] = models.testimonialTitle.objects.all().first
        context['Testimonials'] = models.testimonial.objects.all()
        context['contact'] = models.contact.objects.all().first
        context['info'] = models.info.objects.all().first

        return context

    def form_valid(self, form):
        # Calls the custom send method
        form.send_user_mail(models.titulo.objects.get().titulo)
        return super().form_valid(form)


class About(generic.TemplateView):
    template_name = 'about.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(About, self).get_context_data()
        context['title'] = 'About'
        context['encabezado'] = models.titulo.objects.all().first
        context['carrusel1'] = models.carrusel1.objects.all()
        context['navbar'] = models.navbar.objects.all().first
        context['about'] = models.about.objects.all().first
        context['info'] = models.info.objects.all().first

        return context


class Fruit(generic.TemplateView):
    template_name = 'fruit.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Fruit, self).get_context_data()
        context['title'] = 'Fruit'
        context['encabezado'] = models.titulo.objects.all().first
        context['carrusel1'] = models.carrusel1.objects.all()
        context['navbar'] = models.navbar.objects.all().first
        context['titleFruit'] = models.fruitTitle.objects.all().first
        context['fruits'] = models.fruit.objects.all()
        context['shop'] = models.shop.objects.all().first
        context['info'] = models.info.objects.all().first

        return context


class Contact(generic.CreateView):
    template_name = 'contact.html'
    model = models.contacto
    form_class = forms.contactoForm
    success_url = reverse_lazy('index')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Contact, self).get_context_data()
        context['title'] = 'Contact'
        context['encabezado'] = models.titulo.objects.all().first
        context['carrusel1'] = models.carrusel1.objects.all()
        context['navbar'] = models.navbar.objects.all().first
        context['contact'] = models.contact.objects.all().first
        context['info'] = models.info.objects.all().first
        context['msg'] = models.contact.objects.all().first

        return context

    def form_valid(self, form):
        # Calls the custom send method
        form.send_user_mail(models.titulo.objects.get().titulo)
        return super().form_valid(form)


class Testimonial(generic.TemplateView):
    template_name = 'testimonial.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Testimonial, self).get_context_data()
        context['title'] = 'Testimonial'
        context['encabezado'] = models.titulo.objects.all().first
        context['carrusel1'] = models.carrusel1.objects.all()
        context['navbar'] = models.navbar.objects.all().first
        context['titleTestimonial'] = models.testimonialTitle.objects.all().first
        context['Testimonials'] = models.testimonial.objects.all()
        context['info'] = models.info.objects.all().first

        return context


@require_POST
def Subscribe(request):
    subs = models.subscripciones(email=request.POST["email"])
    subs.save()
    return redirect('index')
