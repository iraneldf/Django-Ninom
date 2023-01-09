from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from django.conf import settings

from Ninom import settings
from . import views

from app.views import Index, About, Fruit, Contact, Testimonial, Subscribe

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('about', About.as_view(), name='about'),
    path('fruit', Fruit.as_view(), name='fruit'),
    path('contact', Contact.as_view(), name='contact'),
    path('testimonial', Testimonial.as_view(), name='testimonial'),
    path('subscribe', Subscribe, name='subscribe'),
]
