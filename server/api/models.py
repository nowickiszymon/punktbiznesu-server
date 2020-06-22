from django.db import models

from ckeditor.fields import RichTextField


class Wiadomosci(models.Model):
        id = models.AutoField(primary_key=True)
        email = models.EmailField()
        phone = models.CharField(max_length=12)
        content = models.CharField(max_length=2000)
        def __str__(self):
                    return self.email

class Newsletter(models.Model):
        id = models.AutoField(primary_key=True)
        email = models.EmailField()
        def __str__(self):
                    return self.email

class Zamowienia(models.Model):
        id = models.AutoField(primary_key=True)
        name = models.CharField(max_length = 20)
        email = models.EmailField()
        phone = models.CharField(max_length=12)     
        def __str__(self):
                    return self.name

class Rekomendacje(models.Model):
        id = models.AutoField(primary_key=True)
        name = models.CharField(max_length = 20)
        content = models.CharField(max_length=200)
        def __str__(self):
                    return self.name


class Blog(models.Model):
        id = models.AutoField(primary_key=True)
        image = models.ImageField(upload_to='images/')
        title = models.CharField(max_length=100)
        content = RichTextField()
        
        def __str__(self):
                    return self.title