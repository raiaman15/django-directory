from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms.models import BaseModelForm
from django.http.response import HttpResponse
from django.views.generic import CreateView, DetailView

from .models import ImportTask


class ImportTaskCreateView(LoginRequiredMixin, CreateView):
    model = ImportTask
    fields = ['records_to_import', 'images_to_import']
    template_name = 'directory/import_task_create_view.html'

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.importer = self.request.user
        return super().form_valid(form)


class ImportTaskDetailView(LoginRequiredMixin, DetailView):
    model = ImportTask
    fields = ['total_records', 'processed_records', 'status', 'log']
    context_object_name = 'import_task'
    template_name = 'directory/import_task_create_view.html'
