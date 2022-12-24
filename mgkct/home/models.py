from datetime import datetime    

from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock

from wagtail.snippets.models import register_snippet


class HomePage(Page):
    
    subpage_types = ['CommonPage','NewsListPage','TimeTablePage']

    class Meta:
        verbose_name = "Главная страница"


class CommonPage(Page):
    
    date = models.DateField(default=datetime.now, blank=True, verbose_name="Дата публикации")

    body = StreamField([
        ('paragraf', blocks.RichTextBlock(label="Текстовый блок")),
        ('image', ImageChooserBlock(label="Изображение")),
        ('gallery', blocks.ListBlock(ImageChooserBlock(label="Изображение"), label="Галерея изображений")),
    ], use_json_field=True, blank=True, verbose_name="Содержание страницы")

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('body'),
    ]

    parent_page_types = ['HomePage','CommonPage']
    subpage_types = ['CommonPage','NewsListPage', 'TimeTablePage']

    class Meta:
        verbose_name = "Страница"
        verbose_name_plural = "Страницы"


class NewsListPage(Page):

    parent_page_types = ['HomePage','CommonPage']
    subpage_types = ['NewsPage']

    class Meta:
        verbose_name = "Страница архива новостей"
        verbose_name_plural = "Страницы архива новостей"


class NewsPage(Page):

    parent_page_types = ['NewsPage']
    subpage_types = []

    class Meta:
        verbose_name = "Страница новости"
        verbose_name_plural = "Страницы новостей"


class TimeTablePage(Page):

    parent_page_types = ['HomePage','CommonPage']
    subpage_types = []

    class Meta:
        verbose_name = "Страница расписания"
        verbose_name_plural = "Страницы расписаний"


class Employee(models.Model):

    class EmployeeType(models.TextChoices):
        PED = "педагог", "педагог"
        WORK = "рабочий", "рабочий"
        SLY = "служащий", "служащий"
        ADMIN = "администрация", "администрация"

    t = models.CharField(max_length=255, choices=EmployeeType.choices, default=EmployeeType.PED, verbose_name="Тип сотрудника", blank=False)

    pic = models.ImageField(verbose_name="Фотокарточка")

    fio = models.CharField(max_length=255, verbose_name="Ф.И.О.", blank=False)
    birthdate = models.DateField(auto_now=False, verbose_name="Дата рождения", blank=True)
    startworkdate = models.DateField(auto_now=False, verbose_name="Дата начала работы", blank=True)
    stud = models.TextField(verbose_name="Образование", blank=True)
    category = models.CharField(max_length=255, verbose_name="Категория", blank=True)
    disc = models.TextField(verbose_name="Дополнительно", blank=True)

    panels = [

        FieldPanel('t'),
        FieldPanel('pic'),
        FieldPanel('fio'),
        FieldPanel('birthdate'),
        FieldPanel('startworkdate'),
        FieldPanel('stud'),
        FieldPanel('category'),
        FieldPanel('disc'),
    ]

    def __str__(self) -> str:
        return f"({self.t}) {self.fio}"

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"

