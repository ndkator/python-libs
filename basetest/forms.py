from django.forms import ModelForm
from basetest.models import Comments

# Конструктор форм. В данном случае - формирует форму для создания нового комментария.

class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ('CommentsText',)

