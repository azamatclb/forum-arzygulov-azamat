from django.urls import path, include

from webapp.views.comment import CommentAddView
from webapp.views.topic import TopicListView, TopicCreateView, TopicDetailView

app_name = 'webapp'

urlpatterns = [
    path('', TopicListView.as_view(), name='topics'),
    path('topic/create/', TopicCreateView.as_view(), name='topic_create'),
    path('topic/<int:pk>/', TopicDetailView.as_view(), name='topic_detail'),
    path('topic/<int:pk>/comment/add', CommentAddView.as_view(), name='comment_add')
]
