from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ConversationViewSet, MessageViewSet

urlpatterns = [
]

router = DefaultRouter()
router.register('conversations', ConversationViewSet)
router.register('messages', MessageViewSet)
urlpatterns = urlpatterns + router.urls
