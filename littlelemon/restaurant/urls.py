from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # Other paths...
    path('menu/', views.MenuItemsView.as_view(), name='menu-list-create'),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='menu-detail'),
    # path('bookings/', views.BookingViewSet.as_view()),
    path('api-token-auth/', obtain_auth_token),
]