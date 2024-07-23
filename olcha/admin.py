from django.contrib import admin
from olcha.models import  Product,Category,Group,Image

# Register your models here.

admin.site.register(Product)

admin.site.register(Group)
admin.site.register(Image)

@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    class Meta:
        list_display = ['category_name','slug']
        prepopulated_fields = {'slug':('categery_name',)}