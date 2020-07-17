
from django.shortcuts import render

from appdetreinos.evaluations.forms import EvaluationForm


def evaluation(request):
    context = {
        'form': EvaluationForm()
    }
    template_name = 'evaluations/evaluation_form.html'
    return render(request, template_name, context)
