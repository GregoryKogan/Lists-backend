from django.contrib.auth.models import User
from lists.serializers import UserSerializer
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DeleteAccount(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, format=None):
        user=self.request.user
        user.delete()

        return Response({"result": "user deleted"}, status=status.HTTP_204_NO_CONTENT)
