from django.contrib.sitemaps import ping_google
from django.db import models

PROBLEMATIC_POINT = (('1', 'URLのリンクが切れている'),
                     ('2', '内容が誤っている'),
                     ('3', 'その他'))

STATUS_CODE= (('1', '未対応'), ('2', '対応中'), ('3', '完了'))

TARGET_CODE= (('1', '個人向け'), ('2', '事業者向け'))

<<<<<<< HEAD
PREFECTURE_CODE= (('1', '東京都23区'),)

=======
>>>>>>> origin/master

class UserAlert(models.Model):
    problem_found = models.CharField(verbose_name='問題', choices=PROBLEMATIC_POINT, max_length=100)
    applicable_url = models.CharField(verbose_name='該当URL', max_length=1000)
    other_note = models.TextField(verbose_name='その他自由記載', blank=True, null=True)
    response_completed = models.CharField(verbose_name='対応ステータス', choices=STATUS_CODE, max_length=100, null=True, blank=True)
    response_note = models.CharField(verbose_name='対応メモ', max_length=300, blank=True, null=True)
    updated_at = models.DateTimeField(verbose_name='更新日', auto_now=True)

    def __str__(self):
        return self.problem_found

    class Meta:
        verbose_name = "99.ユーザーアラート"
        verbose_name_plural = "99.ユーザーアラート"

class Inquiry(models.Model):
    name = models.CharField(verbose_name='お名前', max_length=50)
    email = models.EmailField(verbose_name='メールアドレス')
    phone = models.CharField(verbose_name='電話番号', max_length=11, blank=True, null=True)
    title = models.CharField(verbose_name='件名', max_length=50)
    content = models.TextField(verbose_name='お問合せ内容')
    status = models.CharField(verbose_name='対応ステータス', choices=STATUS_CODE, max_length=100, null=True, blank=True)
    updated_at = models.DateTimeField(verbose_name='更新日', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "98.お問合せ"
        verbose_name_plural = "98.お問合せ"

class Theme(models.Model):
    theme = models.CharField(verbose_name='テーマタグ', max_length=30)

    def __str__(self):
        return self.theme

    class Meta:
        verbose_name = "02.テーマタグ"
        verbose_name_plural = "02.テーマタグ"

class Subsidy(models.Model):
<<<<<<< HEAD
    name = models.CharField(verbose_name='制度名', max_length=50)
    prefecture = models.CharField(verbose_name='都道府県', choices=PREFECTURE_CODE, max_length=31)
    city = models.CharField(verbose_name='市区町村', max_length=31)
    target = models.CharField(verbose_name='対象者', choices=TARGET_CODE, max_length=10)
    condition = models.TextField(verbose_name='支給条件', max_length=3000)
    overview = models.TextField(verbose_name='制度の概要', null=True, blank=True, max_length=100)
    description = models.TextField(verbose_name='支援内容', max_length=3000)
    maximum_support_amount = models.CharField(verbose_name='上限金額', null=True, max_length=30, blank=True)
    support_amount_note = models.TextField(verbose_name='助成額', null=True, max_length=3000, blank=True)
    how_to_apply = models.TextField(verbose_name='利用・申請方法', max_length=3000, null=True, blank=True)
    start_at = models.DateField(verbose_name='開始日', null=True, blank=True)
    end_at = models.DateField(verbose_name='終了日', null=True, blank=True)
    referrer = models.CharField(verbose_name='お問合せ先', max_length=30)
    official_page = models.URLField(verbose_name='公式ページ')
    is_published = models.BooleanField(verbose_name='公開')
=======
    name = models.CharField(verbose_name='制度名(ex.移住支援制度)', max_length=50)
    prefecture = models.CharField(verbose_name='都道府県(ex.東京都)', max_length=10)
    city = models.CharField(verbose_name='市区町村(ex.世田谷区)', max_length=31)
    target = models.CharField(verbose_name='対象者', choices=TARGET_CODE, max_length=10)
    condition = models.TextField(verbose_name='支給条件(1000字まで)', max_length=1000)
    overview = models.TextField(verbose_name='制度の概要(100字まで)', null=True, blank=True, max_length=100)
    description = models.TextField(verbose_name='支援内容(3000字まで)', max_length=3000)
    maximum_support_amount = models.CharField(verbose_name='上限金額(ex.10000)', null=True, max_length=30, blank=True)
    support_amount_note = models.TextField(verbose_name='助成額(3000字まで)', null=True, max_length=3000, blank=True)
    how_to_apply = models.TextField(verbose_name='利用・申請方法(1000字まで)', max_length=1000, null=True, blank=True)
    start_at = models.DateField(verbose_name='開始日', null=True, blank=True)
    end_at = models.DateField(verbose_name='終了日', null=True, blank=True)
    referrer = models.CharField(verbose_name='お問合せ先(ex.東京都世田谷区)', max_length=30)
    official_page = models.URLField(verbose_name='公式ページ(ex.https://aid-tree.com)')
    is_published = models.BooleanField(verbose_name='公開設定')
>>>>>>> origin/master
    created_at = models.DateTimeField(verbose_name='登録日', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日', auto_now=True)
    themes = models.ManyToManyField(Theme, verbose_name='テーマタグ', blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        try:
            ping_google()
        except Exception:
            pass

    class Meta:
        verbose_name = "01.支援金"
        verbose_name_plural = "01.支援金"