from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.paginator import Paginator
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from webapp.forms.comment import CommentForm
from webapp.forms.topic import TopicForm
from webapp.models import Topic


class TopicListView(ListView):
    template_name = 'topic_templates/topics.html'
    model = Topic
    context_object_name = 'topics'
    paginate_by = 4


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
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        topic = self.get_object()
        comments = topic.comments.all()
        paginator = Paginator(comments, 2)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['comments'] = page_obj
        context['comment_form'] = CommentForm()
        return context


class TopicUpdateView(LoginRequiredMixin, UpdateView, PermissionRequiredMixin):
    template_name = 'topic_templates/topic_update.html'
    form_class = TopicForm
    model = Topic
    permission_required = 'webapp.change_topic'

    def has_permission(self):
        return super().has_permission() or self.request.user == self.get_object().author or self.request.user.groups.filter(
            name='moderator').exists()

    def get_success_url(self):
        return reverse('webapp:topic_detail', kwargs={"pk": self.object.pk})


class TopicDeleteView(LoginRequiredMixin, DeleteView, PermissionRequiredMixin):
    template_name = 'topic_templates/topic_delete.html'
    model = Topic
    permission_required = 'webapp.delete_topic'
    success_url = reverse_lazy('webapp:topics')

    def has_permission(self):
        return super().has_permission() or self.request.user == self.get_object().author or self.request.user.groups.filter(
            name='moderator')

