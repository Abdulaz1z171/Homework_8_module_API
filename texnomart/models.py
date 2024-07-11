from django.db import models

# Create your models here.




class Product(models.Model):
    class RatingChoices(models.IntegerChoices):
        zero = 0
        one = 1
        two = 2
        three = 3
        four = 4
        five = 5

    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to='images/')
    rating = models.PositiveIntegerField(choices=RatingChoices.choices, default=RatingChoices.zero)
    discount = models.IntegerField(default=0)
    

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'

    @property
    def discount_priced(self):
        if self.discount > 0:
            return self.price * (1 - self.discount / 100)
        return self.price

    class Meta:
        verbose_name_plural = "Mahsulotlar"

