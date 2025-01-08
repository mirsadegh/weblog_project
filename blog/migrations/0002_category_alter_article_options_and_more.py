# Generated by Django 5.1.4 on 2025-01-06 18:24

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        max_length=200, verbose_name="عنوان دسته\u200cبندی"
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        max_length=100, unique=True, verbose_name="آدرس دسته\u200cبندی"
                    ),
                ),
                (
                    "status",
                    models.BooleanField(
                        default=True, verbose_name="آیا نمایش داده شود؟"
                    ),
                ),
                ("position", models.IntegerField(verbose_name="پوزیشن")),
            ],
            options={
                "verbose_name": "دسته\u200cبندی",
                "verbose_name_plural": "دسته\u200cبندی ها",
                "ordering": ["position"],
            },
        ),
        migrations.AlterModelOptions(
            name="article",
            options={"verbose_name": "مقاله", "verbose_name_plural": "مقالات"},
        ),
        migrations.AlterField(
            model_name="article",
            name="description",
            field=models.TextField(verbose_name="توضیحات مقاله"),
        ),
        migrations.AlterField(
            model_name="article",
            name="publish",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="تاریخ انتشار"
            ),
        ),
        migrations.AlterField(
            model_name="article",
            name="slug",
            field=models.SlugField(
                max_length=100, unique=True, verbose_name="آدرس مقاله"
            ),
        ),
        migrations.AlterField(
            model_name="article",
            name="status",
            field=models.CharField(
                choices=[("d", "پیشنویس"), ("p", "منتشر شده")],
                max_length=1,
                verbose_name="وضعیت",
            ),
        ),
        migrations.AlterField(
            model_name="article",
            name="thumbnail",
            field=models.ImageField(upload_to="images", verbose_name="تصویر مقاله"),
        ),
        migrations.AlterField(
            model_name="article",
            name="title",
            field=models.CharField(max_length=200, verbose_name="عنوان مقاله"),
        ),
    ]
