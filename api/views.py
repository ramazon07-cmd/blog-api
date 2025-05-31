from api.serializers import PostSerializer
from posts.models import Post
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsAuthorOrReadOnly
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.views import APIView, Response ---> PostListView uchun kerak bo'lgan kutubxonalar
# from rest_framework import generics
# class PostListView(APIView):

#     def get(self, request):
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)

# or

# class PostListAPIView(generics.ListCreateAPIView): # Post yaratish va postlar listlari bitta sahifada
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# class PostCreateAPIView(generics.CreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView): # Postni o'chirish va o'zgartirish, detail funksiyalari ham bir sahifada
#     permission_classes = [IsAuthorOrReadOnly]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# class PostDestroyAPIView(generics.DestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# class PostUpdateAPIView(generics.UpdateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


class PostViewSet(viewsets.ModelViewSet):  # tepadagilarni hammasi bittada
    permission_classes = [IsAuthorOrReadOnly, IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filterset_fields = ['title', 'author']
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    search_fields = ['title', 'author__username'] # category bo'lganida category__name qilinardi
    ordering_fields = ['title', 'author__username'] # category bo'lganida category__name qilinardi
    ordering = ['title', 'author__username'] # category bo'lganida category__name qilinardi
