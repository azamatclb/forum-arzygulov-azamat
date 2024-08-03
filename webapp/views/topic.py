from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView

from webapp.forms.comment import CommentForm
from webapp.forms.topic import TopicForm
from webapp.models import Topic


class TopicListView(ListView):
    template_name = 'topic_templates/topics.html'
    model = Topic
    context_object_name = 'topics'


class TopicCreateView(CreateView, LoginRequiredMixin):
    template_name = 'topic_templates/topic_create.html'
    form_class = TopicForm
    model = Topic
    success_url = reverse_lazy('webapp:topics')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TopicDetailView(DetailView, LoginRequiredMixin):
    template_name = 'topic_templates/topic_detail.html'
    model = Topic
    context_object_name = 'topic'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        topic = self.get_object()
        context['comments'] = topic.comments.all()
        context['comment_form'] = CommentForm()
        return context
