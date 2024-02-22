from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser
from .serializer import CustomUserSerializer,LoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.

class SignUpAPIView(APIView):
    """
    API endpoint for user signup.
    """

    serializer_class = CustomUserSerializer

    def post(self, request, *args, **kwargs):
        """
        Create a new user.

        Parameters:
        - email: Email address of the user.
        - password: Password for the user account.
        - first_name: First name of the user.
        - last_name: Last name of the user.
        - phone: Phone number of the user.
        - address: (Optional) Address of the user.
        - city: (Optional) City of the user.
        - state: (Optional) State of the user.
        - country: (Optional) Country of the user.
        - pincode: Pincode of the user.

        Returns:
        - Success: Returns user data with status code 201.
        - Failure: Returns error message with status code 400 if validation fails.
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

 
class LoginAPIView(APIView):
    """
    API endpoint for user login.
    """

    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        """
        Log in a user and generate JWT token.

        Parameters:
        - email: Email address of the user.
        - password: Password for the user account.

        Returns:
        - Success: Returns JWT token data with status code 200.
        - Failure: Returns error message with status code 400 if validation fails.
        """
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_200_OK)
   