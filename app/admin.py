from django.contrib import admin
from app import models
from solo.admin import SingletonModelAdmin

# Register your models here.

admin.site.register(models.titulo, SingletonModelAdmin)
admin.site.register(models.carrusel1)
admin.site.register(models.navbar, SingletonModelAdmin)
admin.site.register(models.about, SingletonModelAdmin)
admin.site.register(models.fruitTitle, SingletonModelAdmin)
admin.site.register(models.fruit)
admin.site.register(models.shop, SingletonModelAdmin)
admin.site.register(models.testimonialTitle, SingletonModelAdmin)
admin.site.register(models.testimonial)
admin.site.register(models.contact, SingletonModelAdmin)
admin.site.register(models.info, SingletonModelAdmin)
admin.site.register(models.contacto)
admin.site.register(models.destinatario, SingletonModelAdmin)
admin.site.register(models.subscripciones)






