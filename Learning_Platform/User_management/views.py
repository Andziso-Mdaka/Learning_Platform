from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm
from rest_framework import viewsets
from .models import User, Profile
from .serializers import UserSerializer, ProfileSerializer
from Qualification_management.serializers import QualificationSerializer
from Qualification_management.models import Qualification
from django.contrib import messages
from django.http import JsonResponse


# View sets for API endpoints
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

# Regular views
@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    email = request.data.get('email')
    password = request.data.get('password')

    if not email or not password:
        return Response({'error': 'Email and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(request, email=email, password=password)
    if user is not None:
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        user_data = UserSerializer(user).data
        return Response({'token': token.key, 'user': UserSerializer(user).data})
    else:
        return Response({'error': 'Invalid email or password'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    logout(request)
    return Response({'message': 'Logged out successfully'})

# user_management/views.py
@api_view(['POST'])
@permission_classes([AllowAny])
def register_view(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # Assuming Profile model has first_name and last_name fields
            Profile.objects.create(
                user=user,
                first_name=serializer.validated_data.get('first_name', ''),
                last_name=serializer.validated_data.get('last_name', '')
            )
            return Response({'message': 'Registration successful'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_home(request):
    if request.user.role == 'student':
        return Response({'message': f'Welcome {request.user.email} (Student)'})
    elif request.user.role == 'lecturer':
        return Response({'message': f'Welcome {request.user.email} (Lecturer)'})
    elif request.user.role == 'admin' or request.user.is_superuser:
        return Response({'message': f'Welcome {request.user.email} (Admin)'})
    else:
        return Response({'error': 'Unknown role or access denied'}, status=403)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def admin_home(request):
    if request.user.is_superuser or request.user.role == 'admin':
        return Response({'message': f'Welcome {request.user.email} (Admin)'})
    else:
        return Response({'error': 'Access denied'}, status=403)

@api_view(['GET'])
@permission_classes([AllowAny])
def landing_page_view(request):
    if request.user.is_authenticated:
        return Response({'message': f'Welcome back, {request.user.email}!'})
    else:
        return Response({'message': 'Welcome to the landing page'})


# Lecturer endpoints