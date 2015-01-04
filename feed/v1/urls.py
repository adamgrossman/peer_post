from rest_framework import routers
from feed.v1.api.views import MemberViewSet, GroupViewSet, CommentViewSet, LinkViewSet

router = routers.DefaultRouter()
router.register(r'members', MemberViewSet, base_name='members')
router.register(r'groups', GroupViewSet, base_name='groups')
router.register(r'links', LinkViewSet, base_name='links')
router.register(r'comments', CommentViewSet, base_name='comments')
