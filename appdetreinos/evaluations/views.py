from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from appdetreinos.evaluations.models import Evaluation


def evaluation(request):
    template_name = 'evaluations/evaluation_form.html'
    return render(request, template_name)
