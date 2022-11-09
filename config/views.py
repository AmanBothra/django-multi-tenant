from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView

from company.models import Employee, Company
from django.contrib import messages


class EmployeeListView(ListView):
    model = Employee
    template_name = "index.html"

    def get_queryset(self):
        return self.model.objects.select_related().order_by(
            "-id"
        )  # inner join query employee with company

    def get_context_data(self, **kwargs):
        context = super(EmployeeListView, self).get_context_data(**kwargs)

        context["company"] = Company.objects.all()  # get all company name
        return context

    def post(self, request):
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        company_id = request.POST.get("company")
        profile_picture = request.FILES.get("profile_picture")
        company = Company.objects.get(id=int(company_id))
        action = request.POST.get("action")

        if action == "add":
            try:
                Employee.objects.create(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    company=company,
                    profile_picture=profile_picture,
                )
                messages.info(request, "Saved")
            except Exception as e:
                messages.warning(request, f"{e}")

        elif action == "update":
            try:
                data = Employee.objects.get(id=int(request.POST.get("object_id")))
                data.first_name = first_name
                data.last_name = last_name
                data.email = email
                data.company = company
                if profile_picture:
                    data.profile_picture = profile_picture
                data.save()
                messages.success(request)
            except Exception as e:
                messages.warning(request, f"{e}")

        return redirect(request.path)
