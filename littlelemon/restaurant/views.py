from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from .models import Menu,Bookings
from django.contrib.auth.models import User
from rest_framework import generics,viewsets,permissions
from .serializers import MenuSerializer,BookingSerializer,UserSerializer

from rest_framework.permissions import IsAuthenticated


# Create your views here. 
class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Bookings.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [permissions.IsAuthenticated] 