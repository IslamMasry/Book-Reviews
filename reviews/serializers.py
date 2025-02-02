from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Book, Review

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class BookSerializer(serializers.ModelSerializer):
    published_by = UserSerializer(read_only=True)

    class Meta:
        model = Book
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'user', 'book', 'content', 'created_at', 'updated_at']
        read_only_fields = ['user', 'book', 'created_at', 'updated_at']
