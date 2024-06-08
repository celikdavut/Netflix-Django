from django.db import models

# Create your models here.

class Kategoriler(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Movies(models.Model):
    isim=models.CharField(max_length=200)
    aciklama=models.TextField(max_length=500)
    afis=models.FileField(upload_to='afis')
    kategori=models.ForeignKey(Kategoriler,on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self):
        return self.isim