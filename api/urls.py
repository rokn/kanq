from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as token_views

from api.views import posts, badges
from api.views import images
from api.views import topics
from api.views import tags
from api.views import users
from api.views import comments
from api.views import medals

router = DefaultRouter()

router.register(r'posts', posts.PostViewSet)
router.register(r'images', images.ImageViewSet)
router.register(r'topics', topics.TopicViewSet)
router.register(r'tags', tags.TagViewSet)
router.register(r'users', users.UserViewSet)
router.register(r'comments', comments.CommentViewSet)
router.register(r'medals', medals.MedalViewSet)
router.register(r'badges', badges.BadgeViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', token_views.obtain_auth_token, name='auth'),
    url(r'^oauth/', include('rest_framework_social_oauth2.urls')),
]
