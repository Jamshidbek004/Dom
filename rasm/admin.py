from django.contrib import admin
from .models import ImageKirish, ImagemMaket, ImagemOrqafon, ImagemMatn, House, Video, Contact, NashiUslugi, HouseDesign, Contact2

# ImageKirish modelini admin panelga qo'shish
@admin.register(ImageKirish)
class ImageKirishAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'uploaded_at']  # Ro'yxatda ko'rsatiladigan ustunlar
    list_filter = ['uploaded_at']  # Filtrlash uchun ustunlar
    search_fields = ['title']  # Qidiruv uchun ustunlar

# ImagemMaket modelini admin panelga qo'shish
@admin.register(ImagemMaket)
class ImagemMaketAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'uploaded_at']
    list_filter = ['uploaded_at']
    search_fields = ['title']

# ImagemOrqafon modelini admin panelga qo'shish
@admin.register(ImagemOrqafon)
class ImagemOrqafonAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'uploaded_at']
    list_filter = ['uploaded_at']
    search_fields = ['title']

# ImagemMatn modelini admin panelga qo'shish
@admin.register(ImagemMatn)
class ImagemMatnAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'text', 'uploaded_at']
    list_filter = ['uploaded_at']
    search_fields = ['title']

# House modelini admin panelga qo'shish
@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ['title', 'material', 'technology', 'size', 'price', 'image']
    list_filter = ['material', 'technology']
    search_fields = ['title']

# Video modelini admin panelga qo'shish
@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'video_url', 'text', 'uploaded_at']
    list_filter = ['uploaded_at']
    search_fields = ['title']

# Contact modelini admin panelga qo'shish
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'message']
    search_fields = ['name', 'email', 'phone']

# NashiUslugi modelini admin panelga qo'shish
@admin.register(NashiUslugi)
class NashiUslugiAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'uploaded_at']
    list_filter = ['uploaded_at']
    search_fields = ['title']

# HouseDesign modelini admin panelga qo'shish
@admin.register(HouseDesign)
class HouseDesignAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'image', 'video_url', 'additional_features']
    search_fields = ['title']

# Contact2 modelini admin panelga qo'shish
@admin.register(Contact2)
class Contact2Admin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'message']
    search_fields = ['name', 'phone']

# Qo'shimcha sozlamalar
admin.site.site_header = "Admin Panel"
admin.site.site_title = "Admin Panel"



