from django.contrib import admin
from .models import PledgeType, Project, Category

# Register your models here.
from django.contrib import admin
from .models import Category, PledgeType, Project
# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'description', 'goal','category']

admin.site.register(Project, ProjectAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','category_name']

admin.site.register(Category, CategoryAdmin)


class PledgeTypeAdmin(admin.ModelAdmin):
    list_display = ['id','pledge_type_name']

admin.site.register(PledgeType, PledgeTypeAdmin)