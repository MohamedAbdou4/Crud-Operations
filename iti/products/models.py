from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, null=True)
    image = models.CharField(max_length=200, null=True)
    no_of_items = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    
    def get_show_url(self):
        return reverse("products.show", kwargs={"id":self.id})

    def get_delete_url(self):
        return reverse("products.delete", kwargs={"id":self.id})

    def get_edit_url(self):
        return reverse("products.edit", kwargs={"pk":self.id})

    # def get_create_url(self):
    #     return reverse("products.create", kwargs={"id":self.id})