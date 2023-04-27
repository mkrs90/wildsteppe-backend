from rest_framework import viewsets
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status, permissions, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from .models import *

from .serializers import *

class UserCreate(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class DifficultyViewSet(viewsets.ModelViewSet):
    queryset = Difficulty.objects.all()
    serializer_class = DifficultySerializer    

class TrailViewSet(viewsets.ModelViewSet):
    queryset = Trail.objects.all()
    
    def get_serializer_class(self):
        if self.action in ("create", "update", "partial_update", "destroy"):
            print("you did either a PUT, PATCH, POST, or DELETE on trails")
            return TrailWriteSerializer
        print("You did a GET on trails")
        return TrailSerializer

class TrailSimplifiedViewSet(viewsets.ModelViewSet):
    queryset = Trail.objects.all()
    serializer_class = TrailSimplifiedSerializer 

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()

    def get_serializer_class(self):
        if self.action in ("create", "update", "partial_update", "destroy"):
            print("you did either a PUT, PATCH, POST, or DELETE on comments")
            return CommentWriteSerializer
        print("You did a GET on comments")
        return CommentSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)