import django_filters
from django_filters.filters import CharFilter

from .models import Teacher


class TeacherFilter(django_filters.FilterSet):
    class Meta:
        last_name = CharFilter()

        model = Teacher
        fields = {
            'last_name': ['icontains'],
            'subject_taught': ['icontains'],
        }
