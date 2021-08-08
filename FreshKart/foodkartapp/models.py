from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    img = models.ImageField(upload_to='category_pic')
    def __str__(self):
        return '{}'.format(self.name)

    def get_url(self):
        return reverse('prod_cat',args=[self.slug])

class product(models.Model):
    name = models.CharField(max_length=50,unique=True)
    slug = models.SlugField(max_length=50,unique=True)
    img = models.ImageField(upload_to='pictures')
    desc = models.TextField()
    price = models.IntegerField()
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    category = models.ForeignKey(category,on_delete=models.CASCADE)
    def __str__(self):
        return '{}'.format(self.name)

    def get_url(self):
        return reverse('details',args=[self.category.slug,self.slug])

class cartlist(models.Model):
    cart_id = models.CharField(max_length=60,unique=True)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.cart_id

class items(models.Model):
    prod = models.ForeignKey(product,on_delete=models.CASCADE)
    cart = models.ForeignKey(cartlist, on_delete=models.CASCADE)
    quant = models.IntegerField()
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.prod

    def total(self):
        return self.prod.price*self.quant