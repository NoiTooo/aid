from django import forms
from .models import Inquiry


class InquiryCreateForm(forms.ModelForm):
   class Meta:
      model = Inquiry
      fields = ('name', 'email', 'phone', 'title', 'content')