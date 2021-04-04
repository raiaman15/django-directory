from django.urls import path
from .views import ImportTaskCreateView, ImportTaskDetailView, TeacherDetailView, TeacherListView, TeacherSearchView

urlpatterns = [
    # import specific routes
    path('import/', ImportTaskCreateView.as_view(), name='import_task_create'),
    path('import/<int:pk>/', ImportTaskDetailView.as_view(), name='import_task_detail'),
    # teacher specific routes
    path('teachers/', TeacherListView.as_view(), name='teacher_list'),
    path('teacher/<int:pk>/', TeacherDetailView.as_view(), name='teacher_detail'),
    path('teacher/search/', TeacherSearchView.as_view(), name='teacher_search'),
]
