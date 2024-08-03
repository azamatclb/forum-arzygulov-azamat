from django import forms
from django.core.exceptions import ValidationError

from webapp.models import Comment


class CommentForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea, max_length=500, label="Комментарий", required=True)

    def clean_comment(self):
        comment = self.cleaned_data.get('description')
        if comment:
            if comment:
                if len(comment) < 3:
                    raise ValidationError('This field must contain at least 3 symbols')
                elif len(comment) > 500:
                    raise ValidationError('This field cant contain more then 3000 symbols')
        return comment

    class Meta:
        model = Comment
        fields = ['comment']
