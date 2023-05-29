from django.urls import path, include
from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()

router.register('posts', views.PostViewSet)
router.register('groups', views.GroupViewSet)
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    views.CommentViewSet,
    basename='comments')
router.register('follow', views.FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(router.urls)),
]
