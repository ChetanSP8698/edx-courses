from django.contrib.auth.models import AbstractUser
from django.db import models

Categories = [
    ('FS', 'Fashion'),
    ('EC', 'Electronics'),
    ('BE', 'Beauty'),
    ('HF', 'Home & Furniture'),
    ('SP', 'Sports'),
    ('BK', 'Books'),
    ('CR', 'Cars')
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
    item_winner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="winner")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.item_id}, {self.item_title}"

class bid(models.Model):
    pass

class comments(models.Model):
    pass