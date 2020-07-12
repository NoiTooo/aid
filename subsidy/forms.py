from django import forms
from .models import Inquiry, UserAlert
import csv
import io
from .models import Subsidy

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


class CSVUploadForm(forms.Form):
    file = forms.FileField(label='CSVファイル', help_text='※拡張子csvのファイルをアップロードしてください。')

    def clean_file(self):
        file = self.cleaned_data['file']

        # ファイル名が.csvかどうかの確認
        if not file.name.endswith('.csv'):
            raise forms.ValidationError('拡張子がcsvのファイルをアップロードしてください')

        # csv.readerに渡すため、TextIOWrapperでテキストモードなファイルに変換
        csv_file = io.TextIOWrapper(file, encoding='cp932')
        reader = csv.reader(csv_file)

        # 各行から作った保存前のモデルインスタンスを保管するリスト
        self._instances = []
        try:
            for row in reader:
                post = Subsidy(pk=row[0], name=row[1], prefecture=row[2], city=row[3], target=row[4], condition=row[5], overview=row[6], description=row[7], maximum_support_amount=row[8], support_amount_note=row[9], how_to_apply=row[10], start_at=row[11], end_at=row[12], referrer=row[13], official_page=row[14], is_published=row[15], created_at=row[16], updated_at=row[17])
                self._instances.append(post)
        except UnicodeDecodeError:
                raise forms.ValidationError('ファイルのエンコーディングや、正しいCSVファイルか確認ください。')

        return file

    def save(self):
        for post in self._instances:
            post.save()
