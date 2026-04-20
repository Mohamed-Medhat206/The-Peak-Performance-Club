from django.contrib import admin
from .models import Branch, Member, Trainer, GymClass, Equipment, DamagedEquipments

# Register your models here.
admin.site.register(Branch)
admin.site.register(Member)
admin.site.register(Trainer)
# admin.site.register(GymClass)
admin.site.register(Equipment)


@admin.register(GymClass)
class GymClassAdmin(admin.ModelAdmin):
    list_display = ('title', 'base_price', 'start_date', 'discounted_price')

    def discounted_price(self, obj):
        return obj.calculate_discount()

    discounted_price.short_description = "Discounted Price"



@admin.register(DamagedEquipments)
class DamagedEquipments(admin.ModelAdmin):
    def get_queryset(self, request):
        return Equipment.objects.filter(is_damaged=True)
    