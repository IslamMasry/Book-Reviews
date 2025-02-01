from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Book, Review
from .serializers import BookSerializer, ReviewSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib.auth.models import User
# User Signup
class UserRegisterView(APIView):

    authentication_classes = []  
    permission_classes = []
    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        if not (username and email and password):
            return Response({"error": "All fields are required"}, status=400)
        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already taken"}, status=400)
        user = User.objects.create_user(username=username, email=email, password=password)
        return Response({"message": "User registered successfully"}, status=201)

# Book Views
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(published_by=self.request.user)

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = []

    def perform_update(self, serializer):
        if self.request.user == self.get_object().published_by:
            serializer.save()
        else:
            return Response({"error": "You can only edit books you published"}, status=403)

    def perform_destroy(self, instance):
        if self.request.user == instance.published_by:
            instance.delete()
        else:
            return Response({"error": "You can only delete books you published"}, status=403)

# Review Views
class ReviewListCreateView(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        book_id = self.kwargs['book_id']
        return Review.objects.filter(book_id=book_id)

    def perform_create(self, serializer):
        book = Book.objects.get(id=self.kwargs['book_id'])
        if book.published_by == self.request.user:
            return Response({"error": "You cannot review your own book"}, status=403)
        serializer.save(user=self.request.user, book=book)

class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        if self.request.user == self.get_object().user:
            serializer.save()
        else:
            return Response({"error": "You can only edit your own reviews"}, status=403)

    def perform_destroy(self, instance):
        if self.request.user == instance.user:
            instance.delete()
        else:
            return Response({"error": "You can only delete your own reviews"}, status=403)
