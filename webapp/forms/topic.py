from django import forms
from django.core.exceptions import ValidationError

from webapp.models import Topic


class TopicForm(forms.ModelForm):
    summary = forms.CharField(max_length=500, label="Тема")

    def clean_summary(self):
        summary = self.cleaned_data.get('summary')
        if summary:
            if summary:
                if len(summary) < 3:
                    raise ValidationError('This field must contain at least 3 symbols')
                elif len(summary) > 300:
                    raise ValidationError('This field cant contain more then 300 symbols')
        return summary

    class Meta:
        model = Topic
        fields = ['summary']
