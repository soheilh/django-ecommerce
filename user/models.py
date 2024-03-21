from django.db import models
from django.contrib.auth.models import User

# Model for Admins
class AdminUser(User):
    phone = models.CharField(max_length=11)
    postal_code = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    field= models.CharField(max_length=20)
    def save(self, *args, **kwargs):
        self.is_staff = True
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Admin"
        verbose_name_plural = "Admins"

    def __str__(self):
        user = self.get_full_name()
        if user:
            return user
        else:
            return self.username

# Model for Customers
class CustomerUser(User):
    username = None
    phone = models.CharField(max_length=11, unique=True)
    home_state = models.CharField(max_length=20)
    home_city = models.CharField(max_length=50)
    home_address = models.CharField(max_length=200)
    home_postal_code = models.CharField(max_length=20)
    shaba = models.CharField(max_length=30)
    favorite = models.ManyToManyField("product.Product", related_name="customerUser")
    USERNAME_FIELD = "phone"

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"
