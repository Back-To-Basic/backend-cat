# Generated by Django 3.2 on 2022-01-24 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='이름')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='생성일시')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='수정일시')),
            ],
        ),
        migrations.CreateModel(
            name='AnimalImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seq', models.IntegerField(default=0, verbose_name='순서')),
                ('image', models.ImageField(upload_to='%Y/animals/%m', verbose_name='사진')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='생성일시')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='수정일시')),
                ('animal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='image_set', related_query_name='images', to='animals.animal', verbose_name='동물')),
            ],
        ),
    ]