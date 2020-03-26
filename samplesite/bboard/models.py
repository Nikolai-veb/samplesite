from django.db import models


# Create your models here.

class Bb(models.Model):
    title = models.CharField(max_length = 50, verdose_name="Товар")
    content = models.TextField(null=True, blank=True, verdose_name="Описание товара"))
    price = models.FloatField(null=True, blank=True, verdose_name="Цена товара"))
    pablished = models.DateTimeField(auto_now_add=True, db_index=True, verdose_name="Время публикацыи"))

class Meta:
    verdose_name_pijral = "Объявьение"
    verdose_name = "Объявление"
    ordering = ['-published']

