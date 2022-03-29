from rest_framework import viewsets 
from rest_framework.decorators import action
from rest_framework.response import Response

from posts.models import Group, Post, Comment, Follow
from .serializers import GroupSerializer, PostSerializer, CommentSerializer, FollowSerializer
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from rest_framework import filters


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def get_queryset(self):
        post_id = self.kwargs.get("post_id")
        new_queryset = Comment.objects.filter(post=post_id)
        return new_queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


# class FollowViewSet(viewsets.ModelViewSet):
#     serializer_class = FollowSerializer
#     filter_backends =  (filters.SearchFilter,)
#     search_fields = ('following__username',)

#     def get_queryset(self):
#         return Follow.objects.filter(user=self.request.user)

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)

class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ("following__username",)

    def get_queryset(self):
        queryset = Follow.objects.filter(user=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)