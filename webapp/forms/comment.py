from django import forms
from django.core.exceptions import ValidationError

from webapp.models import Comment


class CommentForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea, max_length=500, label="Комментарий", required=True)

    def clean_comment(self):
        comment = self.cleaned_data.get('comment')
        if comment:
            if len(comment) < 3:
                raise ValidationError('Комментарий должен содержать не менее 3 символов.')
            elif len(comment) > 500:
                raise ValidationError('Комментарий не может содержать более 500 символов.')
        return comment

    class Meta:
        model = Comment
        fields = ['comment']
