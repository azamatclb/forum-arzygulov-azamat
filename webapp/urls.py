from django.urls import path
from webapp.views.comment import CommentAddView, CommentUpdateView, CommentDeleteView
from webapp.views.topic import TopicListView, TopicCreateView, TopicDetailView, TopicUpdateView, TopicDeleteView

app_name = 'webapp'

urlpatterns = [
    path('', TopicListView.as_view(), name='topics'),
    path('topic/create/', TopicCreateView.as_view(), name='topic_create'),
    path('topic/<int:pk>/', TopicDetailView.as_view(), name='topic_detail'),
    path('topic/<int:topic_id>/comment/add/', CommentAddView.as_view(), name='comment_add'),
    path('topic/<int:pk>/update', TopicUpdateView.as_view(), name='topic_update'),
    path('topic/<int:pk>/delete', TopicDeleteView.as_view(), name='topic_delete'),
    path('topic/<int:pk>/comment/update/', CommentUpdateView.as_view(), name='comment_update'),
    path('topic/<int:pk>/comment/delete/', CommentDeleteView.as_view(), name='comment_delete'),
]
