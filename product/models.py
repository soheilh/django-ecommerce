from django.db import models
from user.models import CustomerUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.html import format_html

# Model for Category of products
class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "Categories"

# Model for color of products
class Color(models.Model):
    color_name = models.CharField(max_length=20)
    code = models.CharField(max_length=7)

    def __str__(self):
        return self.color_name

# Model for Brand of products
class Brand(models.Model):
    title = models.CharField(max_length=255)
    picture = models.ImageField(upload_to="brands")

    def __str__(self):
        return self.title

    def picture_tag(self):
        return format_html(f"<img width=60 src='{self.picture.url}'/>")
    picture_tag.short_description = "logo"


# Model for Products
STATUS_CHOICES =(
    ('d', 'Draft'),
    ('p', 'Published'),
    ('o', 'Out of Stock'),
    ('d', 'Discontinued'),
)

class Product(models.Model):
    name = models.CharField(max_length=100, blank=False)
    category = models.ManyToManyField(Category, related_name="products")
    color = models.ForeignKey(Color, on_delete=models.DO_NOTHING, related_name="products")
    code = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.DO_NOTHING, null=True)
    count_sold = models.IntegerField(default=0)
    price = models.DecimalField(decimal_places=0, max_digits=10)
    offer = models.IntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])
    sales_limit = models.IntegerField(default=5)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    weight = models.IntegerField()

# Model for pictures of products
class Picture(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="pictures")
    file = models.ImageField()

# Model for Comments of products
class Comment(models.Model):
    user = models.ForeignKey(CustomerUser, on_delete=models.DO_NOTHING, related_name="comments")
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, related_name="comments")
    body = models.TextField(blank=False)
    score = models.IntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])
    COMMENT_STATUS = (
        ('p', 'Pending'),
        ('a', 'Approved'),
        ('r', 'Rejected'),
    )
    status = models.CharField(max_length=1, choices=COMMENT_STATUS, default='p')