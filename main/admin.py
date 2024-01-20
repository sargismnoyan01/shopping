from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin


admin.site.register(BaseInfo)
admin.site.register(HomeCarousel)
admin.site.register(Category)
admin.site.register(AllProductModel)
admin.site.register(UserInfos)
admin.site.register(AboutShop)
admin.site.register(Saved)
admin.site.register(ReviewModel)
admin.site.register(Ordering)
admin.site.register(Govazd)


@admin.register(ContactUsModel)
class ContactUsModelAdmin(admin.ModelAdmin):
    list_display=['name','email']
    list_display_links=['name','email']
    search_fields=['name','email']