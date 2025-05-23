# Generated by Django 4.1.6 on 2023-06-15 07:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Assessment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('img', models.ImageField(upload_to='pics')),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Questiontext', models.TextField()),
                ('option1', models.CharField(max_length=1000)),
                ('option2', models.CharField(max_length=1000)),
                ('option3', models.CharField(blank=True, max_length=1000, null=True)),
                ('option4', models.CharField(blank=True, max_length=1000, null=True)),
                ('answer', models.CharField(choices=[('option1', models.CharField(max_length=1000)), ('option2', models.CharField(max_length=1000)), ('option3', models.CharField(blank=True, max_length=1000, null=True)), ('option4', models.CharField(blank=True, max_length=1000, null=True))], max_length=1000)),
                ('assessment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='deekshaapp.assessment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
