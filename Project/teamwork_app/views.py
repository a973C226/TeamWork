from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from django.contrib.auth import authenticate

from .serializers import EmployeeSerializer
from .tokens import create_jwt_pair_for_user


# Create your views here.
class RegisterView(APIView):
    permission_classes = []
    serializer_class = EmployeeSerializer

    def post(self, request: Request) -> Response:
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'message': 'User created successfully',
                'data': serializer.data
            }
            return Response(data=response, status=HTTP_201_CREATED)
        return Response(data=serializer.errors, status=HTTP_400_BAD_REQUEST)


class AuthView(APIView):
    permission_classes = []

    def post(self, request: Request) -> Response:
        email = request.data['email']
        password = request.data['password']

        user = authenticate(email=email, password=password)

        if user is not None:
            tokens = create_jwt_pair_for_user(user)
            response = {"message": "Login successfully", "tokens": tokens}
            return Response(data=response, status=HTTP_200_OK)
        else:
            return Response(data={"message": "Invalid email or password"})
