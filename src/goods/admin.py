from django.contrib import admin
from .models import Token, Good


# Register your models here.
@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    pass


@admin.register(Good)
class GoodAdmin(admin.ModelAdmin):
    pass
