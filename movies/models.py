from django.db import models
from datetime import date

class Category(models.Model):
    # Категории
    name = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    url = models.SlugField(max_length=100)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Actor(models.Model):
    # Актеры и режиссеры
    name = models.CharField(max_length=100, verbose_name='Имя')
    age = models.PositiveSmallIntegerField(default=0, verbose_name='Возраст')
    description = models.TextField(verbose_name='Биография')
    image = models.ImageField(upload_to='actors/')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Актеры и режиссеры'
        verbose_name_plural = 'Актеры и режиссеры'


class Genre(models.Model):
    #Жанр
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    url = models.SlugField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

class Movie(models.Model):
    #Фильмы
    title = models.CharField(max_length=100, verbose_name='Название')
    tagline = models.CharField(max_length=100, default='', verbose_name='Слоган')
    description = models.TextField('Описание')
    poster = models.ImageField(upload_to='movies/')
    year = models.PositiveSmallIntegerField(default=2023, verbose_name='Год выпуска')
    country = models.CharField(max_length=30, verbose_name='Страна')
    directors = models.ManyToManyField(Actor, verbose_name='режиссер', related_name='film_director')
    actors = models.ManyToManyField(Actor, verbose_name='актеры', related_name='film_actor')
    genres = models.ManyToManyField(Genre, verbose_name='Жанры')
    world_premiere = models.DateField(default=date.today, verbose_name='Мировая премьера')
    budget = models.PositiveIntegerField(default=0, help_text='указывать сумму в долларах')
    fees_in_usa = models.PositiveIntegerField(default=0, help_text='указывать сумму в долларах', verbose_name='Сборы в США')
    fees_in_world = models.PositiveIntegerField(default=0, help_text='указывать сумму в долларах', verbose_name='Сборы в Мире')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name='Категория')
    url = models.SlugField(max_length=100, unique=True)
    draft = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'


class MovieShots(models.Model):
    #Кадры из фильма
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='movie_shots/', verbose_name='Изображение')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name='Фильм')

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Кадр из фильма'
        verbose_name_plural = 'Кадры из фильма'


class RatingStar(models.Model):
    #Звезда рейтинга
    value = models.SmallIntegerField(default=0, verbose_name='Рейтинг')

    def __str__(self) -> str:
        return self.value
    
    class Meta:
        verbose_name = 'Звезда рейтинга'
        verbose_name_plural = 'Звезды рейтинга'


class Rating(models.Model):
   #Рейтинг
   ip = models.CharField(max_length=15)
   star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name='Звезда')
   movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name='фильм')

   def __str__(self) -> str:
       return f'{self.star} - {self.movie}'
   
   class Meta:
       verbose_name = 'Рейтинг'
       verbose_name_plural = 'Рейтинги'

class Reviews(models.Model):
    #Отзывы
    email = models.EmailField(verbose_name='Почта')
    name = models.CharField(max_length=100, verbose_name='Наименование')
    text = models.TextField(max_length=5000)
    parent = models.ForeignKey('self', verbose_name='родитель', on_delete=models.SET_NULL, blank=True, null=True)
    movie = models.ForeignKey(Movie, verbose_name='фильм', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.name} - {self.movie}'
    
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

            
        
    








