# Generated by Django 4.1.4 on 2022-12-24 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_commonpage_newslistpage_newspage_timetablepage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='commonpage',
            options={'verbose_name': 'Страница', 'verbose_name_plural': 'Страницы'},
        ),
        migrations.AlterModelOptions(
            name='homepage',
            options={'verbose_name': 'Главная страница'},
        ),
        migrations.AlterModelOptions(
            name='newslistpage',
            options={'verbose_name': 'Страница архива новостей', 'verbose_name_plural': 'Страницы архива новостей'},
        ),
        migrations.AlterModelOptions(
            name='newspage',
            options={'verbose_name': 'Страница новости', 'verbose_name_plural': 'Страницы новостей'},
        ),
        migrations.AlterModelOptions(
            name='timetablepage',
            options={'verbose_name': 'Страница расписания', 'verbose_name_plural': 'Страницы расписаний'},
        ),
    ]
