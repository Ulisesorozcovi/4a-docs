from rest_framework import generics
from authApp.models.user import User
from authApp.serializers import userSerializer

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = userSerializer