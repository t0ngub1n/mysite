from django.db import models

# My models are here.

cyrillic_letters = {
    'а': 'a',
    'б': 'b',
    'в': 'v',
    'г': 'g',
    'д': 'd',
    'е': 'e',
    'ё': 'e',
    'ж': 'zh',
    'з': 'z',
    'и': 'i',
    'й': 'j',
    'к': 'k',
    'л': 'l',
    'м': 'm',
    'н': 'n',
    'о': 'o',
    'п': 'p',
    'р': 'r',
    'с': 's',
    'т': 't',
    'у': '',
    'ф': 'f',
    'х': 'h',
    'ц': 'ts',
    'ч': 'ch',
    'ш': 'sh',
    'щ': 'sch',
    'ъ': '',
    'ы': 'y',
    'ь': '',
    'э': 'e',
    'ю': 'j',
    'я': 'ja',
    'А': 'A',
    'Б': 'B',
    'В': 'V',
    'Г': 'G',
    'Д': 'D',
    'Е': 'E',
    'Ё': 'E',
    'Ж': 'ZH',
    'З': 'Z',
    'И': 'I',
    'Й': 'J',
    'К': 'K',
    'Л': 'L',
    'М': 'M',
    'Н': 'N',
    'О': 'O',
    'П': 'P',
    'Р': 'R',
    'С': 'S',
    'Т': 'T',
    'У': '',
    'Ф': 'F',
    'Х': 'H',
    'Ц': 'TS',
    'Ч': 'CH',
    'Ш': 'SH',
    'Щ': 'SCH',
    'Ъ': '',
    'Ы': 'Y',
    'Ь': '',
    'Э': 'E',
    'Ю': 'J',
    'Я': 'JA',
    ' ': '_',
}


def cyrillic2latin(text):
    tmp = ''
    for ch in text:
        tmp += cyrillic_letters.get(ch, ch)
    return tmp


class User(models.Model,):
    id = models.IntegerField(verbose_name='ID', primary_key=True)
    nick = models.CharField(max_length=100,
                            verbose_name='Никнейм',
                            unique=True, blank=True)
    name = models.CharField(max_length=100,
                            verbose_name='Реальные имя и фамилия',
                            default='')
    password = models.CharField(max_length=100,
                                verbose_name='Пароль', default='123123')
    permissions = models.IntegerField(verbose_name='Возможности', default=0)
    slug = models.CharField(max_length=100,
                            verbose_name='Slug (не трогать)',
                            unique=True, blank=True, )

    class Meta:
        verbose_name = 'Информация о пользователе'
        verbose_name_plural = 'Информация о пользователях'

    def __str__(self, ):
        return self.name

    def save(self, *args, **kwargs):
        if not self.nick or self.nick == '' or self.nick == ' ':
            self.nick = self.name
        # self.nick = cyrillic2latin(self.nick) [i shall not convert nicks]
        self.slug = cyrillic2latin(self.nick)
        super().save(*args, **kwargs)


class Article(models.Model, ):
    id = models.IntegerField(verbose_name='ID', primary_key=True)
    date = models.DateTimeField(verbose_name='Время написания', unique=True)
    name = models.CharField(max_length=100,
                            verbose_name='Название статьи',
                            default='***')
    text = models.CharField(max_length=2 ** 10, verbose_name='Текст', default='Я опять забыл написать текст :(')
    slug = models.CharField(max_length=100,
                            verbose_name='Slug (не трогать)',
                            unique=True, blank=True, )

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.nick = None

    def __str__(self, ):
        return self.name

    def save(self, *args, **kwargs):
        if not self.nick or self.nick == '' or self.nick == ' ':
            self.nick = self.name
        # self.nick = cyrillic2latin(self.nick) [i shall not convert nicks]
        self.slug = cyrillic2latin(self.nick)
        super().save(*args, **kwargs)
