from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register(r"company", views.CompanyViewSets)
router.register(r"employee", views.EmployeeViewSets)

urlpatterns = [path("", include(router.urls))]
