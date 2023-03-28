from django.contrib.auth import get_user_model
from django.db import models
from pytils.translit import slugify
from phonenumber_field.modelfields import PhoneNumberField

User = get_user_model()


class Engine(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(blank=True, unique=True)
    cylinders = models.PositiveIntegerField()

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)[:100]
        super().save(*args, **kwargs)

    class Meta:
        ordering = ('pk',)


class RepairType(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)[:100]
        super().save(*args, **kwargs)

    class Meta:
        ordering = ('pk',)


class Customer(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(blank=True, unique=True)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)[:100]
        super().save(*args, **kwargs)

    class Meta:
        ordering = ('pk',)


class CustomerContact(models.Model):
    last_name = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200, blank=True, null=True,)
    phone_number = PhoneNumberField(unique = True, blank=True, null=True,)
    customer = models.ForeignKey(
        Customer,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='contacts'
    )

    def __str__(self):
        return (f'{self.name} {self.last_name} {self.customer.name}')
    
    class Meta:
        ordering = ('last_name',)


class Repair(models.Model):
    repair_number = models.PositiveIntegerField(unique = True,)
    engine_number = models.CharField(max_length=50, unique = True,)
    customer = models.ForeignKey(
        Customer,
        null=True,
        on_delete = models.PROTECT,
        related_name='repairs'
    )
    customer_contacts = models.ForeignKey(
        CustomerContact,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='repairs'
    )
    repair_type = models.ForeignKey(
        RepairType,
        null=True,
        on_delete = models.PROTECT,
        related_name='repairs'
    )
    engine = models.ForeignKey(
        Engine,
        null=True,
        on_delete = models.PROTECT,
        related_name='repairs'
    )
    author = models.ForeignKey(
        User,
        null=True,
        on_delete=models.PROTECT,
        related_name='repairs'
    )
    description = models.TextField()
