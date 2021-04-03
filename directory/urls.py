from django.urls import path
from .views import ImportTaskCreateView, ImportTaskDetailView

urlpatterns = [
    path('import/', ImportTaskCreateView.as_view(), name='import_task_create'),
    path('import/<int:pk>/', ImportTaskDetailView.as_view(), name='import_task_detail'),
]
