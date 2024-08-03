from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView

from webapp.forms.comment import CommentForm
from webapp.models import Topic
from webapp.models.comment import Comment


class CommentAddView(LoginRequiredMixin, CreateView, PermissionRequiredMixin):
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
        return reverse('webapp:topic_detail', kwargs={'pk': self.object.topic.pk})


class CommentUpdateView(UpdateView, LoginRequiredMixin, PermissionRequiredMixin):
    model = Comment
    form_class = CommentForm
    template_name = 'comment_templates/comment_update.html'

    def has_permission(self):
        return super().has_permission() or self.request.user == self.get_object().author or self.request.user.groups.filter(
            name='moderator')

    def get_success_url(self):
        return reverse('webapp:topic_detail', kwargs={"pk": self.object.pk})


class CommentDeleteView(DeleteView, LoginRequiredMixin, PermissionRequiredMixin):
    model = Comment
    template_name = 'comment_templates/comment_delete.html'
    permission_required = 'webapp.delete_comment'

    def has_permission(self):
        return super().has_permission() or self.request.user == self.get_object().author or self.request.user.groups.filter(
            name='moderator')
