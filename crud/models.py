from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=19, decimal_places=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    description = models.TextField()
    category = models.ManyToManyField(Category, related_name='category')

    def __str__(self):
        return self.name
    
class Reporter(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)

    def __str__(self):
        return self.firstName
    

class Article(models.Model):
    headLine = models.TextField(max_length=255)
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headLine