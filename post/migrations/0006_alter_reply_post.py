# Generated by Django 3.2.6 on 2021-08-20 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_alter_reply_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='post.post'),
        ),
    ]
