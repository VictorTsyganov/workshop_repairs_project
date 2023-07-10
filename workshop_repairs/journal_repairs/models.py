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
        ordering = ('title',)


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
        ordering = ('title',)


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
        ordering = ('name',)


class CustomerContact(models.Model):
    last_name = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200, blank=True, null=True,)
    phone_number = PhoneNumberField(unique=True, blank=True, null=True,)
    customer = models.ForeignKey(
        Customer,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='contacts'
    )

    def __str__(self):
        return (f'{self.last_name} {self.name} - {self.customer.name}')

    class Meta:
        ordering = ('last_name',)


class AddressOperation(models.Model):
    address = models.CharField(max_length=400, unique=True)
    slug = models.SlugField(blank=True, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.address)[:100]
        super().save(*args, **kwargs)

    class Meta:
        ordering = ('address',)

    def __str__(self):
        return self.address[:100]


class Еquipment(models.Model):
    title = models.CharField(max_length=100, unique=True)
    name_equipment = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(blank=True, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name_equipment)[:100]
        super().save(*args, **kwargs)

    class Meta:
        ordering = ('name_equipment',)

    def __str__(self):
        return self.name_equipment


class EngineNumber(models.Model):
    engine_number = models.CharField(max_length=50, unique=True,)
    slug = models.SlugField(blank=True, unique=True)
    engine = models.ForeignKey(
        Engine,
        null=True,
        on_delete=models.PROTECT,
        related_name='engine_numbers'
    )
    equipment = models.ForeignKey(
        Еquipment,
        null=True,
        on_delete=models.PROTECT,
        related_name='engine_numbers'
    )
    equipment_number = models.CharField(
        max_length=400, blank=True)
    owner = models.ForeignKey(
        Customer,
        null=True,
        on_delete=models.PROTECT,
        related_name='engine_numbers'
    )
    address = models.ForeignKey(
        AddressOperation,
        null=True,
        on_delete=models.PROTECT,
        related_name='engine_numbers'
    )
    start_date = models.DateField(null=True,)

    def __str__(self):
        return str(self.engine_number)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.engine_number)[:100]
        super().save(*args, **kwargs)

    class Meta:
        ordering = ('pk',)


class EngineHours(models.Model):
    pub_date = models.DateField(auto_now_add=True)
    engine_hours = models.PositiveIntegerField(null=True,)
    engine_number = models.ForeignKey(
        EngineNumber,
        on_delete=models.PROTECT,
        related_name='hours'
    )

    def __str__(self):
        return (f'{self.engine_hours} м.ч./(км)')

    class Meta:
        ordering = ('-pub_date',)


class Repair(models.Model):
    pub_date = models.DateTimeField(auto_now_add=True,)
    repair_number = models.CharField(
        max_length=10, unique=True,)
    engine_numbers = models.ManyToManyField(
        EngineNumber,
        through='EngineNumberRepair',
        related_name='repairs'
    )
    customer = models.ForeignKey(
        Customer,
        null=True,
        on_delete=models.PROTECT,
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
        on_delete=models.PROTECT,
        related_name='repairs'
    )
    address = models.ForeignKey(
        AddressOperation,
        null=True,
        on_delete=models.PROTECT,
        related_name='repairs'
    )
    author = models.ForeignKey(
        User,
        null=True,
        on_delete=models.PROTECT,
        related_name='repairs'
    )
    description = models.TextField()

    def __str__(self):
        return str(self.repair_number)

    class Meta:
        ordering = ('-pub_date',)


class EngineNumberRepair(models.Model):
    engine_number = models.ForeignKey(EngineNumber, on_delete=models.CASCADE)
    repair = models.ForeignKey(Repair, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.repair} {self.engine_number}'
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['engine_number', 'repair'], name='unique_rep_engine')
        ]


class Comment(models.Model):
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    repair = models.ForeignKey(
        Repair,
        on_delete=models.CASCADE,
        related_name='comments'
    )

    def __str__(self):
        return self.text[:100]

    class Meta:
        ordering = ('-created',)
