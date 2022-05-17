from django.contrib import admin

# Register your models here.
from .models import Category, Depency, Salary 

admin.site.register(Salary)
admin.site.register(Category)
admin.site.register(Depency)

# @admin.register(Salary)
# class SalaryAdmin(admin.ModelAdmin):
#     pass

# @admin.register(Depency)
# class DepencyAdmin(admin.ModelAdmin):
#     pass

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     pass



