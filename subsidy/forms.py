from django import forms
from .models import Inquiry, UserAlert


class InquiryCreateForm(forms.ModelForm):
    """問い合わせフォーム"""
    class Meta:
        model = Inquiry
        fields = ('name', 'email', 'phone', 'title', 'content')


class UserAlertForm(forms.ModelForm):
    """ユーザーアラート"""
    class Meta:
        model = UserAlert
        fields = ('problem_found', 'applicable_url', 'other_note')
