import os
from django.contrib import admin
from data.models import Document, Gallery, Image, Entry

class AdminGallery(admin.ModelAdmin):
    fields = ['gallery_author','gallery_name']
    list_display = ('gallery_author','gallery_name')
    prepopulated_fields = {'gallery_name': ['gallery_author']}

    def save_model(self, request, obj, form, change):
        #if the 'gallery_author' fiels is empty the author is the current User
        if getattr(obj, 'gallert_author', None) is None:
            obj.entry_author = request.user
        obj.save()

class EntryAdminImage(admin.ModelAdmin):
    fields = ['entry_title', 'entry_slug', 'is_mainphoto', 'entry_desc', 'entry_imagen','entry_tag']
    list_display = ('entry_author', 'entry_title', 'entry_slug','is_mainphoto','entry_desc', 'miniatura')
    #prepopulated_fields = { 'entry_author' : 'cesar' }
    prepopulated_fields = { 'entry_slug': ['entry_title'] }

    def save_model(self, request, obj, form, change):
        #if the 'entry_author' fiels is empty the author is the current User
        if getattr(obj, 'entry_author', None) is None:
            obj.entry_author = request.user
        obj.save()


class EntryAdminDocument(admin.ModelAdmin):
    fields = ['entry_title', 'entry_slug', 'entry_desc', 'entry_document', 'entry_tag']
    list_display = ('entry_title', 'entry_desc', 'miniatura')
    prepopulated_fields = { 'entry_slug': ['entry_title'] }
    #prepopulated_fields = { 'entry_author' : 'cesar' }

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'entry_author', None) is None:
            obj.entry_author = request.user
        obj.save()

admin.site.register(Gallery, AdminGallery)
admin.site.register(Document, EntryAdminDocument)
admin.site.register(Image, EntryAdminImage)
