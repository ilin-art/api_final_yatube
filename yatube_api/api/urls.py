from rest_framework.routers import SimpleRouter

from django.urls import include, path

from .views import GroupViewSet, PostViewSet, CommentViewSet


router = SimpleRouter()

router.register('groups', GroupViewSet) # Убрать basename если нет def get_queryset во вью
router.register('posts', PostViewSet)
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)
router.register('follow', PostViewSet)


urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
] 