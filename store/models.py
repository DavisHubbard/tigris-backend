from django.db import models

class Item(models.Model):
  owner = models.ForeignKey('auth.User', related_name='items', on_delete=models.CASCADE)

  created = models.DateTimeField(auto_now_add=True)
  title = models.CharField(max_length=100, blank=True, default='')
  description = models.CharField(max_length=500, blank=True, default='')
  price = models.DecimalField(max_digits=20, decimal_places=2)
  ITEM_TYPE_CHOICES = [
    ('electronic', 'Electronics'),
    ('entertainment', 'Movies, Music & Games'),
    ('clothing', 'Clothing, Shoes & Jewelry'),
    ('book', 'Books'),
    ('electronic', 'Electronics'),
    ('other', 'Other'),
  ]
  item_type = models.CharField(max_length=20, choices=ITEM_TYPE_CHOICES, default='other')

  class Meta:
    ordering = ['created']
