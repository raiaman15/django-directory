from django.urls import path
from django_filters import filterset
from django_filters.views import FilterView

from .filters import TeacherFilter
from .views import ImportTaskCreateView, ImportTaskDetailView, TeacherDetailView, TeacherListView, TeacherSearchView

urlpatterns = [
    # import specific routes
    path('import/', ImportTaskCreateView.as_view(), name='import_task_create'),
    path('import/<int:pk>/', ImportTaskDetailView.as_view(), name='import_task_detail'),
    # teacher specific routes
    # path('teachers/', TeacherListView.as_view(), name='teacher_list'),
    path(
        'teachers/', FilterView.as_view(
            filterset_class=TeacherFilter,
            template_name='directory/teacher_list.html',
        ),
        name='teacher_list'
    ),
    path('teacher/<int:pk>/', TeacherDetailView.as_view(), name='teacher_detail'),
    path('teacher/search/', TeacherSearchView.as_view(), name='teacher_search'),
]
