# Generated by Django 4.1.7 on 2023-04-25 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_rename_user_postcomments_commenter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postcomments',
            name='postId',
            field=models.IntegerField(),
        ),
    ]
