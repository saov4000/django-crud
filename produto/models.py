from django.db import models

class Produto(models.Model):
    descricao = models.CharField(max_length=50,null=False)
    preco = models.IntegerField(null=False)

    def __str__(self):
        return self.descricao