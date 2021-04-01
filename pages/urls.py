from django.urls import path
from .views import CompanyPageView, ProductPageView, DashboardView

urlpatterns = [
    path('company/', CompanyPageView.as_view(), name='company_page'),
    path('product/', ProductPageView.as_view(), name='product_page'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]
