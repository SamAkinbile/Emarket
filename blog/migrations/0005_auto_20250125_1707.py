# Generated by Django 3.2.25 on 2025-01-25 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_contact_submitted_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='temp_field',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='submitted_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
