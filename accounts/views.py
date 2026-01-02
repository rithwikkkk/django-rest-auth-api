from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile_view(request):
    user = request.user
    return Response({
        "id": user.id,
        "username": user.username,
        "email": user.email,
    })


@api_view(['POST'])
@permission_classes([AllowAny])
def register_view(request):
    serializer = RegisterSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(
            {"message": "User registered successfully"},
            status=status.HTTP_201_CREATED
        )

    return Response(
        serializer.errors, 
        status=status.HTTP_400_BAD_REQUEST
    )

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view, permission_classes


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    try:
        refresh_token = request.data.get("refresh")
        token = RefreshToken(refresh_token)
        token.blacklist()

        return Response(
            {"message": "Logged out successfully"},
            status=status.HTTP_205_RESET_CONTENT
        )
    except Exception:
        return Response(
            {"error": "Invalid token"},
            status=status.HTTP_400_BAD_REQUEST
        )


from rest_framework_simplejwt.views import TokenObtainPairView
from .jwt import EmailTokenObtainPairSerializer

class EmailTokenObtainPairView(TokenObtainPairView):
    serializer_class = EmailTokenObtainPairSerializer