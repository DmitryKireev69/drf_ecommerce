from rest_framework.response import Response
from rest_framework.views import APIView

from apps.accounts.serializers import CreateUserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from apps.accounts.serializers import MyTokenObtainPairSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class RegisterAPIView(APIView):
    serializer_class = CreateUserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': "success"}, status=201)