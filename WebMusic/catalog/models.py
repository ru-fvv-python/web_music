from django.db import models


# Create your models here.
class Style(models.Model):
    """Музыкальные стили"""
    name = models.CharField(max_length=20,
                            help_text='Введите музыкальный стиль',
                            verbose_name='Музыкальный стиль')

    def __str__(self):
        """возвращаяет музыкальный стиль"""
        return self.name


class Singer(models.Model):
    """"Певец или музыкальная группа"""
    name = models.CharField(max_length=50,
                            help_text='Введите название группы или певца',
                            verbose_name='Исполнитель песни')
    # image = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True, help_text='Выберите картинку',
    #                           verbose_name='Изображение',
    #                           width_field=100)
    style = models.ForeignKey('Style', on_delete=models.CASCADE,
                              help_text='Выберите стиль',
                              verbose_name='Музыкальный стиль')

    def __str__(self):
        """возвращаяет исполнителя"""
        return self.name


class Album(models.Model):
    """Альбом"""
    name = models.CharField(max_length=100,
                            help_text='Введите название альбома',
                            verbose_name='Альбом')
    year = models.IntegerField(help_text='Введите год альбома',
                               verbose_name='Год')
    singer = models.ForeignKey('Singer', on_delete=models.CASCADE,
                               help_text='Выберите исполнителя',
                               verbose_name='Исполнитель')

    def __str__(self):
        """возвращаяет название альбома"""
        return self.name


class Song(models.Model):
    """Песни"""
    name = models.CharField(max_length=100,
                            help_text='Введите название песни',
                            verbose_name='Песня')
    album = models.ForeignKey('Album', on_delete=models.CASCADE,
                              help_text='Выберите название альбома',
                              verbose_name='Альбом')
    file = models.FileField(help_text='Выберите файл песни',
                            verbose_name='Файл песни')

    def __str__(self):
        """возвращаяет название песни"""
        return self.name


class PlayList(models.Model):
    """play list"""
    name = models.CharField(max_length=50,
                            help_text='введите название плэй-листа',
                            verbose_name='Play-list')

    def __str__(self):
        """возвращаяет название плей-листа"""
        return self.name


class SongList(models.Model):
    """Состав песен в плей-листе"""
    playlist = models.ForeignKey('PlayList', on_delete=models.CASCADE)
    song = models.ForeignKey('Song', on_delete=models.CASCADE)

    def __str__(self):
        """возвращает пл и песню"""
        return '%s %s' % (self.playlist, self.song)
