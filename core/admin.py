from django.contrib import admin
from .models import Branch, Member, Trainer, GymClass

# Register your models here.
admin.site.register(Branch)
admin.site.register(Member)
admin.site.register(Trainer)
admin.site.register(GymClass)
