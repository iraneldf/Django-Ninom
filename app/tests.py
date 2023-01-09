from django.test import TestCase
from django.core.mail import send_mail
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from Ninom import settings
from . import models, forms

# Create your tests here.
from .views import Fruit

