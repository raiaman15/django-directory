import numpy as np
import os
import pandas as pd
import re
import shutil
import zipfile

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.forms.models import BaseModelForm
from django.http.response import HttpResponse
from django.views.generic import CreateView, DetailView, ListView

from .models import Teacher, ImportTask

TEMP_PATH = settings.BASE_DIR.joinpath('files-media').joinpath('temp')
PICTURE_PATH = settings.BASE_DIR.joinpath('files-media').joinpath('picture')


class ImportTaskCreateView(LoginRequiredMixin, CreateView):
    model = ImportTask
    fields = ['records_to_import', 'images_to_import']
    template_name = 'directory/import_task_create.html'

    @staticmethod
    def _scan_file(f):
        print(f'Dummy scan file {f}')

    @staticmethod
    def _import_record(r):
        status = 'Success'
        try:
            t = Teacher(
                first_name=r['First Name'],
                last_name=r['Last Name'],
                email=r['Email Address'],
                phone_number=r['Phone Number'],
                room_number=r['Room Number']
            )

            if not pd.isna(r['Profile picture']):
                # Move the picture from /temp/ folder to /picture/
                source = str(TEMP_PATH.joinpath(r["Profile picture"]))
                destination = str(PICTURE_PATH.joinpath(r["Profile picture"]))
                shutil.move(source, destination)
                t.picture = f'picture/{r["Profile picture"]}'

            s = r['Subjects taught'].lower().strip().split(',')
            t.subject_taught = ' | '.join(s)

            t.save()

        except IOError as io:
            status = f'Failure: Missing actual profile picture.'
        except Exception as e:
            status = f'Failure: {e}'

        return status

    def _run_import_task(self) -> None:
        # Scan uploaded files for security
        self._scan_file(self.object.images_to_import)
        self._scan_file(self.object.records_to_import)

        # Unzip Image Zip file to <media directory>/temp/
        with zipfile.ZipFile(self.object.images_to_import, 'r') as zip_ref:
            zip_ref.extractall(str(TEMP_PATH))

        # Rename filename to lowercase for standardization
        for file in os.listdir(str(TEMP_PATH)):
            os.rename(str(TEMP_PATH.joinpath(file)), str(TEMP_PATH.joinpath(file.lower())))
            # Scan individual image files in temp folder for security
            self._scan_file(file)

        # Process CSV file, move image file per record to <media directory>/picture/
        try:
            os.makedirs(os.path.dirname(str(PICTURE_PATH)))
        except OSError:
            pass
        data = pd.read_csv(self.object.records_to_import)

        # Clean data
        data['Profile picture'] = data['Profile picture'].apply(
            lambda v: v.lower() if re.match(r'(\d)+.(jpg|JPG|png|PNG)', v) else np.NaN)
        data.dropna(axis=0, how='all', inplace=True)
        self.object.total_records = data.shape[0]
        data['Import Status'] = data.apply(lambda r: self._import_record(r), axis=1)
        self.object.status = 'E' if data['Import Status'].str.contains('Failure', regex=False).any() else 'S'

        # Save Task processing log
        self.object.log = data.to_html()
        self.object.save()

        # Remove all files from <media directory>/temp/ for storage
        try:
            shutil.rmtree(str(TEMP_PATH))
        except OSError:
            os.remove(str(TEMP_PATH))

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
    template_name = 'directory/import_task_detail.html'


class TeacherListView(ListView):
    model = Teacher
    fields = [
        'last_name',
        'subject_taught',
        # 'subject_taught_2',
        # 'subject_taught_3',
        # 'subject_taught_4',
        # 'subject_taught_5',
    ]
    context_object_name = 'teachers'
    paginate_by = 100
    template_name = 'directory/teacher_list.html'


class TeacherDetailView(DetailView):
    model = Teacher
    context_object_name = 'teacher'
    template_name = 'directory/teacher_detail.html'


class TeacherSearchView(ListView):
    model = Teacher
    context_object_name = 'teachers'
    paginate_by = 100
    template_name = 'directory/teacher_search.html'

    def get_queryset(self):
        if self.request.GET.get('q'):
            query = self.request.GET.get('q')
            return Teacher.objects.filter(Q(last_name__icontains=query) | Q(subject_taught__icontains=query))
        else:
            return Teacher.objects.all()
