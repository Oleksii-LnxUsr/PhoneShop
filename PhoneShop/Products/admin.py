from django.contrib import admin

from .models import Phone, Brands, PhoneImage


admin.site.register(Brands)

class PhoneImageAdmin(admin.StackedInline):
    model = PhoneImage

@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    inlines = [PhoneImageAdmin]

    class Meta:
       model = Phone

@admin.register(PhoneImage)
class PhoneImageAdmin(admin.ModelAdmin):
    pass