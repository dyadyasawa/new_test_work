# Generated by Django 4.2.2 on 2024-08-29 04:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0001_initial"),
        ("comments", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="post",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="posts.post",
                verbose_name="Пост",
            ),
        ),
    ]
