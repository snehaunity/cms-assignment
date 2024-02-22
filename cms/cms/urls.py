from django.urls import path
from content.views import (
    ContentItemListCreateAPIView,
    ContentItemRetrieveUpdateDestroyAPIView
)
from accounts.views import LoginAPIView,SignUpAPIView
urlpatterns = [
    path('content/', ContentItemListCreateAPIView.as_view(), name='content-list-create'),
    path('content/<int:pk>/', ContentItemRetrieveUpdateDestroyAPIView.as_view(), name='content-retrieve-update-destroy'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('signup/', SignUpAPIView.as_view(), name='signup')
    
]
