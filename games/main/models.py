from django.db import models

# Create your models here.
class Games(models.Model):
    title = models.CharField('Название', max_length=30, default='')
    game_url = models.URLField('Ссылка на игру' , max_length=250 , default='')
    description = models.CharField('Описание', max_length=160 , default='')
    thumbnail= models.URLField('Url иконки', max_length=250, default='')
    genre = models.URLField('Жанр', max_length=30, default='')
    
    def __str__(self):
        return self.title