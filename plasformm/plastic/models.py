from django.db import models

class ContactModel(models.Model):
    '''модель формы обратной связи'''
    name = models.CharField("Имя", max_length=100)
    company = models.CharField("Компания", max_length=100)
    email = models.EmailField()
    number = models.PositiveIntegerField("Телефон", default=0)
    description = models.TextField("Сообщение")

    
