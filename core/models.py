from django.db import models
from django.utils import timezone

class baseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Branch(baseModel):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Member(baseModel):
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    @property
    def is_vip(self):
        return self.balance > 1000

class Trainer(baseModel):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class GymClass(baseModel):
    title = models.CharField(max_length=100)
    base_price = models.FloatField()
    start_date = models.DateField()
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    members = models.ManyToManyField(Member, related_name='gym_classes')

    def __str__(self):
        return self.title


    def calculate_discount(self):
        if self.start_date > (timezone.now().date() + timezone.timedelta(days=30)):
            return self.base_price * 0.8
        return self.base_price

class Equipment(baseModel):
    name = models.CharField(max_length=100)
    is_damaged = models.BooleanField(default=False)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

