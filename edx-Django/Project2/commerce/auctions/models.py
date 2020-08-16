from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

Categories = [
    ('FS', 'Fashion'),
    ('EC', 'Electronics'),
    ('BE', 'Beauty'),
    ('HF', 'Home & Furniture'),
    ('SP', 'Sports'),
    ('BK', 'Books'),
    ('CR', 'Cars'),
    ('OT', 'Others')
]

class User(AbstractUser):
    pass

class listings(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_image = models.URLField(blank=True)
    item_title = models.CharField(max_length=128)
    item_des = models.TextField()
    item_price = models.FloatField()
    create_time = models.DateTimeField(auto_now_add=True)
    item_category = models.CharField(choices = Categories, max_length=2)
    avail_item = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    item_starting_bid = models.FloatField(null=True)
    item_winner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="Winner")

    def __str__(self):
        return f"{self.item_title}, {self.item_des}, {self.item_price}, {self.item_image}, {self.item_category}"

class bid(models.Model):
    item_bid = models.FloatField(null=True)
    listing = models.ForeignKey(listings, on_delete=models.CASCADE, null=True, related_name="bid")
    bid_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class comments(models.Model):
    comment = models.TextField()
    c_listings = models.ForeignKey(listings, on_delete=models.CASCADE, null=True, related_name="comment")
    user_commented = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class watch_list(models.Model):
    watch_list_item = models.ForeignKey(listings, on_delete=models.CASCADE, null=True)
    watchlistuser = models.ForeignKey(User, on_delete=models.CASCADE, null=True)