from django.db import models

class Event(models.Model):
    event = models.CharField(verbose_name='イベントタグ', max_length=30)

    def __str__(self):
        return self.event

    class Meta:
        verbose_name = "04.イベントタグ"
        verbose_name_plural = "04.イベントタグ"

class Prefecture(models.Model):
    prefecture = models.CharField(verbose_name='都道府県タグ', max_length=4)

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
    start_at = models.DateTimeField(verbose_name='開始日', null=True, blank=True)
    end_at = models.DateTimeField(verbose_name='終了日', null=True, blank=True)
    maximum_amount = models.CharField(verbose_name='上限金額', null=True, max_length=30, blank=True)
    condition = models.TextField(verbose_name='条件', null=True, blank=True)
    description = models.TextField(verbose_name='説明文', null=True, blank=True)
    official_page = models.URLField(verbose_name='公式ページ')
    created_at = models.DateTimeField(verbose_name='登録日', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日', auto_now=True)
    prefectures = models.ManyToManyField(Prefecture, verbose_name='都道府県タグ', blank=True)
    cities = models.ManyToManyField(City, verbose_name='市区町村タグ', blank=True)
    events = models.ManyToManyField(Event, verbose_name='イベントタグ', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "01.支援金"
        verbose_name_plural = "01.支援金"
