from tabnanny import verbose

from django.core.mail import send_mail
from django.core.validators import RegexValidator
from django.http import JsonResponse
from solo.models import SingletonModel
from django.contrib.sites.models import Site
from django.db import models

# Create your models here.
from Ninom import settings


class titulo(SingletonModel):
    titulo = models.CharField(max_length=100, verbose_name='Title')
    imagen = models.ImageField(verbose_name='header image', upload_to='images/header_imagen/', default=" ")

    class Meta:
        verbose_name = '01- Header'

    def __str__(self):
        return self.titulo


class carrusel1(models.Model):
    imagen = models.ImageField(verbose_name='Picture', upload_to='images/carrusel1/')

    class Meta:
        verbose_name_plural = '02- Carousel'
        verbose_name = 'item'


class navbar(SingletonModel):
    home = models.CharField(max_length=100, verbose_name='Home', default='Home')
    about = models.CharField(max_length=100, verbose_name='About', default='About')
    fruit = models.CharField(max_length=100, verbose_name='Fruit', default='Our Fruit')
    testimonial = models.CharField(max_length=100, verbose_name='Testimonial', default='Testimonial')
    contact = models.CharField(max_length=100, verbose_name='Contact', default='Contact Us')

    class Meta:
        verbose_name = '03- Navigation bar'

    def __str__(self):
        return self.home + ' | ' + self.about + ' | ' + self.fruit + ' | ' + self.testimonial + ' | ' + self.contact


class shop(SingletonModel):
    titulo = models.CharField(max_length=100, verbose_name='Title', default='Fruit shop')
    descripcion = models.TextField(max_length=1000, verbose_name='Description',
                                   default='There are many variations of passages of Lorem Ipsum available')
    imagen = models.ImageField(verbose_name='Picture', upload_to='images/shop/')
    boton = models.CharField(max_length=1000, verbose_name='Button', default='Buy now')

    class Meta:
        verbose_name = '04- Shop'

    def __str__(self):
        return self.titulo


class about(SingletonModel):
    titulo = models.CharField(max_length=100, verbose_name='Title', default='About Our Fruit Shop')
    descripcion = models.TextField(max_length=2000, verbose_name='Description',
                                   default='There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour')
    imagen = models.ImageField(verbose_name='Picture', upload_to='images/shop/')

    class Meta:
        verbose_name = '05- About us'

    def __str__(self):
        return self.titulo


class fruitTitle(SingletonModel):
    nombre = models.CharField(max_length=100, verbose_name='Name', default='Fresh Fruit')

    class Meta:
        verbose_name = '06- Title for fruits'

    def __str__(self):
        return self.nombre


class fruit(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Name', default='')
    imagen = models.ImageField(verbose_name='Picture', upload_to='images/fruit/')
    activ = models.BooleanField(default=True, verbose_name='Show')

    class Meta:
        verbose_name_plural = '07- Fruits'
        verbose_name = 'Fruit'

    def __str__(self):
        if self.activ:
            result = "Shown"
        else:
            result = "No show"
        return self.nombre + ' (' + result + ')'

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.activ:
            destinatarios = []
            for dest in subscripciones.objects.all():
                destinatarios.append(dest.email)
            print(destinatarios)
            url = Site.objects.get_current().domain

            send_mail(
                titulo.objects.get().titulo,
                "Hello! We have new products visit us at: "+url,
                settings.EMAIL_HOST_USER,
                destinatarios,
            )

        return super(fruit, self).save()


class testimonialTitle(SingletonModel):
    titulo = models.CharField(max_length=100, verbose_name='Title', default='What Says Cutomer')

    class Meta:
        verbose_name = '08- testimonial title'

    def __str__(self):
        return self.titulo


class testimonial(models.Model):
    nombreCliente = models.CharField(max_length=100, verbose_name='Customer name', default='')
    enunciado = models.CharField(max_length=50, verbose_name='Statement', default='')
    descripcion = models.TextField(max_length=1000, verbose_name='Description', default='')
    imagen = models.ImageField(verbose_name='Picture', upload_to='images/client/')

    class Meta:
        verbose_name_plural = '09- Testimonials'
        verbose_name = 'Testimony'

    def __str__(self):
        return self.nombreCliente


class contact(SingletonModel):
    titulo = models.CharField(max_length=100, verbose_name='Title', default='Request A call back')
    mapa = models.TextField(max_length=1000, verbose_name='Map', default='')

    class Meta:
        verbose_name = '10- Contact Us'

    def __str__(self):
        return self.titulo


class info(SingletonModel):
    ubicacion = models.CharField(max_length=100, verbose_name='Location', default='')
    ubicacion_en = models.CharField(max_length=100, verbose_name='Location link', default='')
    telef = models.CharField(max_length=100, verbose_name='Phone', default='')
    telef_en = models.CharField(max_length=100, verbose_name='Phone link', default='')
    email = models.EmailField(max_length=100, verbose_name='Mail', default='')
    email_en = models.CharField(max_length=100, verbose_name='Mail link', default='')
    facebookAct = models.BooleanField(default=False, verbose_name='Facebook')
    facebook = models.CharField(max_length=100, verbose_name='Link', default='/', blank=True)
    twitterAct = models.BooleanField(default=False, verbose_name='Twitter')
    twitter = models.CharField(max_length=100, verbose_name='Link', default='/', blank=True)
    instagramAct = models.BooleanField(default=False, verbose_name='Instagram')
    instagram = models.CharField(max_length=100, verbose_name='Link', default='/', blank=True)
    linkedinAct = models.BooleanField(default=False, verbose_name='Linkedin')
    linkedin = models.CharField(max_length=100, verbose_name='Link', default='/', blank=True)

    class Meta:
        verbose_name = '12- Information'


class destinatario(SingletonModel):
    email = models.EmailField(max_length=100, verbose_name='Email')

    class Meta:
        verbose_name = '13- Addressee'

    def __str__(self):
        return self.email


class contacto(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Name')
    email = models.CharField(verbose_name='Email', max_length=200)
    mensaje = models.TextField(max_length=1000, verbose_name='Message')
    numero = models.CharField(max_length=100, verbose_name='Number')

    class Meta:
        verbose_name_plural = '14- Contacts'
        verbose_name = 'Contact'

    def __str__(self):
        return self.nombre


class subscripciones(models.Model):
    email = models.EmailField(max_length=100, verbose_name='Email')

    class Meta:
        verbose_name_plural = '15- Subscriptions'
        verbose_name = 'subscription'

    def __str__(self):
        return self.email
