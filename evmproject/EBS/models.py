from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class OwnerSignup(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    ownermobile = models.CharField(max_length=15, null=False)
    ownerimage = models.FileField(null=True)
    owneraddress = models.CharField(max_length=300, null=True, default=None)
    ownerregdate = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.owner.username

    class Meta:
        db_table = "OwnerSignup_table"

# class OwnerEvent(models.Model):
#     eventname=models.CharField(max_length=100,null=True)
#     image = models.FileField(null=True)
#     category=models.CharField(max_length=100,null=True)
#     description = models.CharField(max_length=300,null=True)
#     startdate=models.DateField(null=True)
#     enddate=models.DateField(null=True)
#     venue=models.CharField(max_length=300,null=True)
#     entryprice=models.CharField(max_length=100,null=True)
#     creationdate = models.DateTimeField(default=datetime.now, blank=True)
#     status = models.CharField(max_length=20,null=True)
#
#     def __str__(self):
#         return self.eventname
#
#     class Meta:
#         db_table = "OwnerEvent_table"

class Event(models.Model):
    eventname=models.CharField(max_length=100,null=True)
    image = models.FileField(null=True)
    category=models.CharField(max_length=100,null=True)
    description = models.CharField(max_length=300,null=True)
    startdate=models.DateField(null=True)
    enddate=models.DateField(null=True)
    venue=models.CharField(max_length=300,null=True)
    entryprice=models.CharField(max_length=100,null=True)
    creationdate = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.eventname

    class Meta:
        db_table = "Event_table"


class UserSignup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15, null=True)
    image = models.FileField(null=True)
    address = models.CharField(max_length=300, null=True, default=None)
    regdate = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = "UserSignup_table"

class SponsorTbl(models.Model):
    event =models.ForeignKey(Event,on_delete=models.CASCADE)
    sponsorimage = models.FileField(null=True)
    creationdate = models.DateTimeField(default=datetime.now, blank=True)

    def _str_(self):
        return self.event.eventname

    class Meta:
        db_table = "SponsorTbl_table"

class Category(models.Model):
    categoryname=models.CharField(max_length=100,null=True)
    creationdate = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.categoryname

    class Meta:
        db_table = "Category_table"

class Booking(models.Model):
    userinfo =models.ForeignKey(UserSignup,on_delete=models.CASCADE)
    eventinfo = models.ForeignKey(Event, on_delete=models.CASCADE)
    person=models.CharField(max_length=100,null=True)
    total=models.CharField(max_length=100,null=True)
    status = models.CharField(max_length=20,null=True)
    bookingdate = models.DateField(null=True)
    cardno = models.CharField(max_length=20,null=True)
    cvv = models.CharField(max_length=10,null=True)
    expirydate = models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.id

    class Meta:
        db_table = "Booking_table"