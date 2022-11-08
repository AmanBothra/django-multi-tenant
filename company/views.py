from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import Employee, Company
from .serializers import CompanySerializer, EmployeeSerializer


class CompanyViewSets(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def delete(self):
        instance = self.get_object()

        self.perform_destroy(instance)
        return Response(
            {
                "status": status.HTTP_204_NO_CONTENT,
                "message": f"Data {instance} deleted successfully"
            }
        )


class EmployeeViewSets(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


    def delete(self):
        instance = self.get_object()

        self.perform_destroy(instance)
        return Response(
            {
                "status": status.HTTP_204_NO_CONTENT,
                "message": f"Data {instance} deleted successfully"
            }
        )



