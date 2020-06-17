from django.contrib.sitemaps import ping_google
from django.db import models

PROBLEMATIC_POINT = (('1', 'URLのリンクが切れている'),
                     ('2', '内容が誤っている'),
                     ('3', 'その他'))

class UserAlert(models.Model):
    problem_found = models.CharField(verbose_name='問題', choices=PROBLEMATIC_POINT, max_length=100)
    applicable_url = models.CharField(verbose_name='該当URL', max_length=1000)
    other_note = models.TextField(verbose_name='その他自由記載', blank=True, null=True)
    response_completed = models.BooleanField(verbose_name='対応完了', blank=True, null=True)
    response_note = models.CharField(verbose_name='対応メモ', max_length=300, blank=True, null=True)

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
        verbose_name = "04.テーマタグ"
        verbose_name_plural = "04.テーマタグ"

class Prefecture(models.Model):
    prefecture = models.CharField(verbose_name='都道府県タグ', max_length=10)

    def __str__(self):
        return self.prefecture

    class Meta:
        verbose_name = "02.都道府県タグ"
        verbose_name_plural = "02.都道府県タグ"


class City(models.Model):
    city = models.CharField(verbose_name='市区町村タグ', max_length=30)

    def __str__(self):
        return self.city

    class Meta:
        verbose_name = "03.市区町村タグ"
        verbose_name_plural = "03.市区町村タグ"


class Subsidy(models.Model):
    name = models.CharField(verbose_name='制度名', max_length=50)
    applicable_area = models.CharField(verbose_name='適用地域', max_length=31)
    target = models.CharField(verbose_name='対象', max_length=10, null=True, blank=True)
    start_at = models.DateTimeField(verbose_name='開始日', null=True, blank=True)
    end_at = models.DateTimeField(verbose_name='終了日', null=True, blank=True)
    maximum_support_amount = models.CharField(verbose_name='最大支給額', null=True, max_length=30, blank=True)
    support_amount_note = models.TextField(verbose_name='支給額補足', null=True, max_length=3000, blank=True)
    description = models.TextField(verbose_name='説明文', max_length=3000, null=True, blank=True)
    condition = models.TextField(verbose_name='条件', max_length=3000, null=True, blank=True)
    referrer = models.CharField(verbose_name='参照元', null=True, max_length=30, blank=True)
    official_page = models.URLField(verbose_name='公式ページ')
    is_published = models.BooleanField(verbose_name='公開')
    created_at = models.DateTimeField(verbose_name='登録日', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日', auto_now=True)
    prefectures = models.ManyToManyField(Prefecture, verbose_name='都道府県タグ', blank=True)
    cities = models.ManyToManyField(City, verbose_name='市区町村タグ', blank=True)
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