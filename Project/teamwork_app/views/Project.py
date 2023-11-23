from django.views.generic import TemplateView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.request import Request

from teamwork_app.models import Employee
from teamwork_app.serializers import ProjectSerializer


class ProjectView(APIView, TemplateView):
    """
    Действие над проектоем
    """

    permission_classes = []
    serializer_class = ProjectSerializer
    template_name = "mainMenu.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        employees = Employee.objects.all()
        context["employees"] = employees
        return context

    def post(self, request: Request) -> Response:
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "message": "Project created successfully",
                "data": serializer.data
            }
            return Response(data=response, status=HTTP_201_CREATED)

        return Response(data=serializer.errors, status=HTTP_400_BAD_REQUEST)
