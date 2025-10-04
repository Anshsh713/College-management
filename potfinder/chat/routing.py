from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/groups/(?P<group_id>\d+)/$', consumers.GroupChatConsumer.as_asgi()),
]