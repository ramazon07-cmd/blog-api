from rest_framework.serializers import ModelSerializer
from posts.models import Post
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['name'] = user.first_name
        token['user'] = user.username

        return token

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']

class PostSerializer(ModelSerializer):
    # author = UserSerializer() # agarda author 1 tadan ko'p bo'lganida many=True qo'yilishi kerak
    class Meta:
        model = Post
        fields = ['id', 'title', 'author', 'body', 'created_at', 'updated_at']
        # depth = 1 # malumotni ichiga qay darajada chuqurroq kirib borishi
