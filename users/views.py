from rest_framework import generics, status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, CustomUserSerializer,CustomUserGetSerializer, RegistrantSerializer
from .models import CustomUser, Registrant


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class UserLoginView(APIView):
    def post(self, request):
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Invalid credentials'}, status=401)

class CustomUserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserGetSerializer
    permission_classes = [permissions.IsAdminUser]

class CustomUserCreateView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAdminUser]

class CustomUserUpdateView(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAdminUser]

    def perform_update(self, serializer):
        serializer.save()

class CustomUserDeleteView(generics.DestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAdminUser]

    def perform_update(self, serializer):
        serializer.save()

class UserListByGroupView(generics.ListAPIView):
    serializer_class = CustomUserSerializer

    def get_queryset(self):
        group_id = self.kwargs.get('group_id')  
        return CustomUser.objects.filter(role__groups=group_id).distinct()



class RegistrantListOnEvent(generics.ListAPIView):
    queryset = Registrant.objects.all()
    serializer_class = RegistrantSerializer
    permission_classes = [permissions.IsAdminUser]


    def get_queryset(self):
        event_id = self.kwargs.get('event_id')
        return Registrant.objects.filter(event=event_id)


class JoinEventAPIView(generics.CreateAPIView):
    queryset = Registrant.objects.all()
    serializer_class = RegistrantSerializer
    permission_classes = [permissions.IsAuthenticated]


    def create(self, request, *args, **kwargs):
        event_id = kwargs.get('event_id')
        user = request.user

        if Registrant.objects.filter(user=user, event_id=event_id).exists():
            return Response({'message': 'User is already registered for this event.'}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = self.get_serializer(data={'user': user.id, 'event': event_id, 'payment_status': True})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)