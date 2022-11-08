from rest_framework import serializers

from .models import Company, Employee


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"


class EmployeeSerializer(serializers.ModelSerializer):
    company_details = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Employee
        fields = (
            "first_name",
            "last_name",
            "company",
            "company_details",
            "profile_picture",
            "email",
            "created_at",
            "updated_at",
        )

    def get_company_details(self, obj):
        return CompanySerializer(obj.company).data
