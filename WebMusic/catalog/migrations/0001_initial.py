# Generated by Django 4.1.7 on 2023-03-16 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название альбома', max_length=100, verbose_name='Альбом')),
                ('year', models.IntegerField(help_text='Введите год альбома', verbose_name='Год')),
            ],
        ),
        migrations.CreateModel(
            name='PlayList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='введите название плэй-листа', max_length=50, verbose_name='Play-list')),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название песни', max_length=100, verbose_name='Песня')),
                ('file', models.FileField(help_text='Выберите файл песни', upload_to='', verbose_name='Файл песни')),
                ('album', models.ForeignKey(help_text='Выберите название альбома', on_delete=django.db.models.deletion.CASCADE, to='catalog.album', verbose_name='Альбом')),
            ],
        ),
        migrations.CreateModel(
            name='Style',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите музыкальный стиль', max_length=20, verbose_name='Музыкальный стиль')),
            ],
        ),
        migrations.CreateModel(
            name='SongList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.playlist')),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.song')),
            ],
        ),
        migrations.CreateModel(
            name='Singer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название группы или певца', max_length=50, verbose_name='Исполнитель песни')),
                ('image', models.ImageField(help_text='Выберите картинку', null=True, upload_to='', verbose_name='Изображение', width_field=100)),
                ('style', models.ForeignKey(help_text='Выберите стиль', on_delete=django.db.models.deletion.CASCADE, to='catalog.style', verbose_name='Музыкальный стиль')),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='singer',
            field=models.ForeignKey(help_text='Выберите исполнителя', on_delete=django.db.models.deletion.CASCADE, to='catalog.singer', verbose_name='Исполнитель'),
        ),
    ]
