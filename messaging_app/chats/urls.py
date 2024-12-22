from django.urls import path
from rest_framework import routers
from .views import ConversationViewSet, MessageViewSet


router = routers.DefaultRouter()
router.register('conversations', ConversationViewSet)
router.register('messages', MessageViewSet)

NestedDefaultRouter = False

urlpatterns = [
    path('api/', include((router.urls, 'chats'))),
]
