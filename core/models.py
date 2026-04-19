from django.db import models

class baseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Branch(baseModel):
    name = models.CharField()
    location = models.CharField()
    
    def __str__(self):
        return self.name

class Member(baseModel):
    name = models.CharField()
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Trainer(baseModel):
    name = models.CharField()
    specialization = models.CharField()

    def __str__(self):
        return self.name

class GymClass(baseModel):
    title = models.CharField()
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    members = models.ManyToManyField(Member, related_name='gym_classes')

    def __str__(self):
        return self.title

class Equipment(baseModel):
    name = models.CharField()
    is_damaged = models.BooleanField(default=False)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

    def __str__(self):
        return self.name