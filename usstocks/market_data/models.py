from django.db import models


class Stock(models.Model):
    stock_quote = models.CharField(max_length=20)

    def __str__(self):
        return self.stock_quote
