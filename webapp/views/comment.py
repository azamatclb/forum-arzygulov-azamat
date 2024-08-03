from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, CreateView

from webapp.forms.comment import CommentForm
from webapp.models import Topic
from webapp.models.comment import Comment


class CommentListView(ListView):
    # template_name = 'comment_list.html'
    model = Comment


class CommentAddView(LoginRequiredMixin, CreateView):
    template_name = 'comment_templates/comment_create.html'
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        topic_id = self.kwargs.get('topic_id')
        topic = get_object_or_404(Topic, id=topic_id)
        form.instance.topic = topic
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('topic_detail', kwargs={'pk': self.object.topic.pk})
