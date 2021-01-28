from django.db import models

from django.urls import reverse


class Buyers(models.Model):
    """Покупатели"""
    name = models.CharField("Имя", max_length=100)
    age = models.PositiveSmallIntegerField("Возраст", default=0)
    description = models.TextField("Описание")


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Покупатели"
        verbose_name_plural = "Покупатели"


class Seller(models.Model):
    """Продавец"""
    title = models.CharField("Имя", max_length=100)
    tagline = models.CharField("Фамилия", max_length=100, default='')
    description = models.TextField("Описание")
    name = models.ManyToManyField(Buyers, verbose_name="покупатель", related_name="shop_buyers")


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("shop_detail", kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Продавец"
        verbose_name_plural = "Продавцы"
