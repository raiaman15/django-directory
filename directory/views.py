import numpy as np
import pandas as pd
import random
import re
import zipfile

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms.models import BaseModelForm
from django.http.response import HttpResponse
from django.views.generic import CreateView, DetailView

from .models import ImportTask

TEMP_PATH = str(settings.BASE_DIR.joinpath('files-media').joinpath('temp'))


class ImportTaskCreateView(LoginRequiredMixin, CreateView):
    model = ImportTask
    fields = ['records_to_import', 'images_to_import']
    template_name = 'directory/import_task_create_view.html'

    @staticmethod
    def _scan_file(f):
        print(f'Dummy scan file {f}')

    @staticmethod
    def _import_record(r):
        return 'Success' if bool(random.getrandbits(1)) else 'Failure'

    def _run_import_task(self) -> None:
        print(f'Rinning task: {str(self.object)}')
        # Scan uploaded files for security
        self._scan_file(self.object.images_to_import)
        self._scan_file(self.object.records_to_import)

        # Unzip Image Zip file to <media directory>/temp/
        with zipfile.ZipFile(self.object.images_to_import, 'r') as zip_ref:
            zip_ref.extractall(TEMP_PATH)

        # Scan individual image files in temp folder for security
        pass

        # Process CSV file, move image file per record to <media directory>/picture/
        data = pd.read_csv(self.object.records_to_import)

        # Clean data
        data['Profile picture'] = data['Profile picture'].apply(
            lambda v: v.lower() if re.match(r'(\d)+.(jpg|JPG|png|PNG)', v) else np.NaN)
        data.dropna(axis=0, how='all', inplace=True)
        self.object.total_records = data.shape[0]
        data['Import Status'] = data.apply(lambda r: self._import_record(r), axis=1)
        self.object.status = 'E' if 'Failure' in data['Import Status'] else 'S'

        # Save Task processing log
        self.object.log = data.to_html()
        self.object.save()

        # Remove all files from <media directory>/temp/ for storage
        pass

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.importer = self.request.user
        return super().form_valid(form)

    def get_success_url(self) -> str:
        self._run_import_task()
        print(self.object.log)
        return super().get_success_url()


class ImportTaskDetailView(LoginRequiredMixin, DetailView):
    model = ImportTask
    fields = ['total_records', 'status', 'log']
    context_object_name = 'import_task'
    template_name = 'directory/import_task_detail_view.html'
