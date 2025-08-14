from django.contrib.auth.models import User  # Don't forget this import
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny
from .serializers import UserSignupSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    identifier = request.data.get('username') or request.data.get('email')
    password = request.data.get('password')

    if not identifier or not password:
        return Response({'error': 'Identifier and password are required'}, status=status.HTTP_400_BAD_REQUEST)

    # 1) try as username
    user = authenticate(username=identifier, password=password)

    # 2) if not found, try lookup by email then authenticate using that user's username
    if user is None:
        try:
            u = User.objects.get(email__iexact=identifier)
        except User.DoesNotExist:
            u = None
        if u:
            user = authenticate(username=u.username, password=password)

    if user is None:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

    token, _ = Token.objects.get_or_create(user=user)
    return Response({'message': 'Login successful', 'token': token.key})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    request.user.auth_token.delete()
    return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_user_view(request):
    user = request.user
    return Response({
        'id': user.id,
        'username': user.username,
        'email': user.email,
    })

@api_view(['POST'])
@permission_classes([AllowAny])
def signup_view(request):
    serializer = UserSignupSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

