# Generated by Django 4.2 on 2025-01-14 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0016_userhistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='userhistory',
            name='result',
            field=models.CharField(choices=[('win', 'Victoire'), ('lose', 'Défaite')], default='win', max_length=10),
        ),
    ]
