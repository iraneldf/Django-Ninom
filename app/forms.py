from django import forms
from django.core.mail import send_mail
from django.http import JsonResponse

from Ninom import settings
from app import models
from app.models import contacto, subscripciones
import smtplib


class contactoForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = models.contacto

    def get_info(self):
        cl_data = super().clean()

        nombre = cl_data.get('nombre').strip()
        mensaje = cl_data.get('mensaje')
        correo = cl_data.get('email')
        numero = cl_data.get('numero')
        destinatarios = models.destinatario.objects.get().email
        return nombre, correo, mensaje, numero, destinatarios

    def send_user_mail(self, titulo):
        nombre, correo, mensaje, numero, destinatarios = self.get_info()
        send_mail(
            'Nuevo contacto de ' + str(titulo),
            'Nombre: ' + nombre +
            '\nCorreo: ' + correo +
            '\nNúmero telfónico: ' + numero +
            '\nMensaje: \n' + mensaje,
            settings.EMAIL_HOST_USER,
            [destinatarios],
        )
        return JsonResponse({
            'msg': 'ok'
        })

