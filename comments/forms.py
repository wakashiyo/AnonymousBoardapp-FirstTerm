from django import forms
from .models import Comment
from django.core.validators import RegexValidator
from django.forms.widgets import ClearableFileInput

class CommentForm(forms.ModelForm):
    password = forms.CharField(
    # widget=forms.PasswordInput(attrs={
    # 'placeholder': '6桁以下の数字（任意）'}),
    validators=[RegexValidator(r'^\d{1,6}$', '6桁以下の数字を入力してください。')],
    label='パスワード（任意）',
    required=False
)

    class Meta:
        model = Comment
        fields = ('body', 'file', 'password',)
        widgets = {
            'body': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': '質問の内容を入力してください。画像添付の場合も何か記入してください。',
                'rows': '10'
            }),
            'file': ClearableFileInput(attrs={
                'class': 'form-control-file',
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
            }),
        }
        labels = {
            'body': '',
            'file': '',
            'password': 'パスワード',
        }

    def clean(self):
        data = super().clean()
        body = data.get('body')
        if body is None:
            msg = "本文が入力されていません"
            self.add_error('body', msg)
        elif len(body) > 1000:
            msg = "本文の最大文字数は1000文字です"
            self.add_error('body', msg)