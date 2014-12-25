from django.db import models
from guest.models import BuyerProfile, SellerProfile 


class Product(models.Model):
    sharers = models.ManyToManyField(BuyerProfile, blank=True)
    owner = models.ForeignKey(SellerProfile)
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='item_Photos')
    caption = models.TextField(max_length=250)
    
    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name
# Create your models here.
class Mote(models.Model):
    products = models.ForeignKey(Product)
    height = models.IntegerField()
    weight = models.IntegerField()
    bust = models.IntegerField()
    waist = models.IntegerField()
    hip = models.IntegerField()
    arm_length = models.IntegerField()
    shoulder_width = models.IntegerField()
    leg_length = models.IntegerField()
    photo = models.ImageField(upload_to='mote_Photos')
    
