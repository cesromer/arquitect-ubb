from django.contrib import admin
from data.models import Document, Image, Entry

class EntryAdminImage(admin.ModelAdmin):
    fields = ['entry_title', 'entry_slug', 'entry_desc', 'entry_imagen','entry_tag']
    list_display = ('entry_author', 'entry_title', 'entry_slug', 'entry_desc', 'miniatura')
    #prepopulated_fields = { 'entry_author' : 'cesar' }
    prepopulated_fields = { 'entry_slug': ['entry_title'] }

    def save_model(self, request, obj, form, change):
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

admin.site.register(Document, EntryAdminDocument)
admin.site.register(Image, EntryAdminImage)
