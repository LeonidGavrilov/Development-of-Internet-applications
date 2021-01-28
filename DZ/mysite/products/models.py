from django.db import models

# Create your models here.

class Artiles(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')
    image = models.ImageField('Изображение', upload_to="images/", null=True, blank=True)

    def __str__(self):
        return f'Название: {self.title}'
    
    def get_absolute_url(self):
        return f'/products/{self.id}'
    
    def bit (self):
        if self.image:
            return u'<img src="%s" width="70"/>'% self.image.url
        else:
            return u'(none)'
    bit.short_descriptio = u'Изображение'
    bit.allow_tags = True

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
