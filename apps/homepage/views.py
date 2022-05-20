# Django imports
from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic


# Create your views here.
class IndexView(generic.TemplateView):
    template_name = 'homepage/index.html'

