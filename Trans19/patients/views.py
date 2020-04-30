from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.http import HttpResponse
from patients.models import Patient, Visit

# Create your views here.


class PatientViewVisits(TemplateView):
    template_name = "visit_list.html"

    def get_context_data(self, **kwargs):
        patient = self.kwargs['patient']

        context = super().get_context_data(**kwargs)
        context['visit_list'] = Visit.objects.filter(patient__pk=patient)
        context['patient'] = Patient.objects.get(pk=patient)
        return context

class PatientsViewAll(ListView):
    template_name = "patient_list.html"
    model = Patient

class indexView(TemplateView):
    template_name = "index.html"

