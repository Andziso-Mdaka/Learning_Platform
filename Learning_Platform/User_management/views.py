from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status, viewsets
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm
from .models import User, Profile
from .serializers import UserSerializer, ProfileSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = authenticate(request, email=email, password=password)
    if user is not None:
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        user_data = UserSerializer(user).data
        user_data['is_staff'] = user.is_staff
        user_data['is_lecturer'] = user.is_lecturer
        return Response({
            'token': token.key,
            'user': user_data
        })
    else:
        return Response({'error': 'Invalid email or password'}, status=400)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    logout(request)
    return Response({'message': 'Logged out successfully'})

@api_view(['POST'])
@permission_classes([AllowAny])
def register_view(request):
    print("Received registration data:", request.data)
    if request.method == 'POST':
        form = RegisterForm(request.data)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user, 
                                   first_name=form.cleaned_data.get('first_name', ''),
                                   last_name=form.cleaned_data.get('last_name', ''))
            return Response({'message': 'Registration successful'}, status=status.HTTP_201_CREATED)
        else:
            print("Form errors:", form.errors)
            return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_home(request):
    if request.user.is_staff:
        return Response({'message': f'Welcome {request.user.email} (Admin)'})
    elif request.user.is_lecturer:
        return Response({'message': f'Welcome {request.user.email} (Lecturer)'})
    else:
        return Response({'message': f'Welcome {request.user.email} (Student)'})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def admin_home(request):
    if request.user.is_staff:
        return Response({'message': f'Welcome {request.user.email} (Admin)'})
    else:
        return Response({'error': 'Access denied'}, status=403)

@api_view(['GET'])
@permission_classes([AllowAny])
def landing_page_view(request):
    return Response({'message': 'Welcome to the landing page'})