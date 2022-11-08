from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from company.models import Employee, Company


class EmployeeListView(ListView):
    model = Employee
    template_name = "index.html"

    def get_queryset(self):
        return self.model.objects.select_related()

    def get_context_data(self, **kwargs):
        context = super(EmployeeListView, self).get_context_data(**kwargs)
        return context