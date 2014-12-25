from django.db import models
# Create your models here.
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class BuyerProfile(models.Model):
    buyer = models.OneToOneField(User, related_name='buyerprofile')
    height = models.PositiveSmallIntegerField()
    weight = models.PositiveSmallIntegerField()
    bust = models.PositiveSmallIntegerField()
    waist = models.PositiveSmallIntegerField()
    hip = models.PositiveSmallIntegerField()
    arm_length = models.PositiveSmallIntegerField()
    shoulder_width = models.PositiveSmallIntegerField()
    leg_length = models.PositiveSmallIntegerField()
    sculpture = models.ImageField(upload_to='buyer_photos', blank=True, null=True)
    introduction = models.TextField(blank=True)

    def __unicode__(self):
        return self.buyer.username

class SellerProfile(models.Model):
    seller = models.OneToOneField(User, related_name='sellerprofile')
    nickname = models.CharField(max_length=30)
    storename = models.CharField(max_length=30)
    telephone = models.CharField(max_length=11)
    company = models.CharField(blank=True, max_length=100)
    link = models.URLField(unique=True)
    sculpture = models.ImageField(blank=True, null=True, upload_to='seller_photos') 
    introduction = models.TextField(blank=True)

    def __unicode__(self):
        return self.seller.username
