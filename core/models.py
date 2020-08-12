from django.db import models

# Create your models here.


class Text(models.Model):

    text = models.CharField('text', max_length=5000)
    date = models.DateTimeField('date', auto_now_add=True)

    def __str__(self):
        return "Text №{}".format(self.id)
