from django.urls import path
from .views import UserRegisterView, BookListCreateView, BookDetailView, ReviewListCreateView, ReviewDetailView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('books/', BookListCreateView.as_view(), name='book_list_create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    
    path('books/<int:book_id>/reviews/', ReviewListCreateView.as_view(), name='review_list_create'),
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='review_detail'),
]
