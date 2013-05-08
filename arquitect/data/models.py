from django.db import models
from django.contrib.auth.models import User
from easy_thumbnails.files import get_thumbnailer
from easy_thumbnails.fields import ThumbnailerImageField
from math import log
import datetime, os
from taggit.managers import TaggableManager
from django.template.defaultfilters import slugify

def get_image_path(instance, filename):
        return os.path.join('images/', str(instance.entry_author), filename)

class Gallery(models.Model):
    gallery_id      = models.AutoField(primary_key=True)
    gallery_author  = models.ForeignKey(User, verbose_name=u'Autor', null=True, blank=True)
    gallery_name    = models.CharField(verbose_name='Nombre', max_length=200)


class Entry(models.Model):
    object_id   = models.AutoField(primary_key=True)
    #entry_id    = models.IntegerField(primary_key=True)
    entry_author= models.ForeignKey(User, verbose_name=u'Autor', null=True, blank=True)
    entry_tag   = TaggableManager()
    entry_title = models.CharField(verbose_name='Titulo', max_length=200)
    entry_slug  = models.SlugField(verbose_name='Slug', unique=True)
    entry_desc  = models.TextField(verbose_name='Descripcion')
    SI = 'SI'
    NO = 'NO'
    OPTIONS = (
        (SI, 'Imagen Principal'),
        (NO, 'Imagen Normal'),
    )
    is_mainphoto = models.CharField(verbose_name="Es Foto Principal?", max_length=2,
                                      choices=OPTIONS,
                                      default=NO)
    entry_gallery = models.ForeignKey('Gallery', default=1)
    #entry_content = ContentType.objects.get_for_model(User)
    def __unicode__(self):
        return u'%s' % (self.entry_title)

    def get_tags(self):
        tags = []
        for t in self.entry_tag:
            tags.append(t.name)
        return tags
    get_tags.allow_tags = True

    def save(self, **kwargs):
        if self.is_mainphoto == 'SI':
            try:
                i = Image.objects.get(is_mainphoto='SI')
                i.is_mainphoto = 'NO'
                i.save()
                self.is_mainphoto = 'SI'
            except Image.DoesNotExist:
                pass
        if not self.entry_slug:
            self.entry_slug = slugify(self.entry_title, instance=self)
            self.is_mainphoto = 'NO'
        super(Entry, self).save(**kwargs)


class Document(Entry):
    #entry_imagen = models.ImageField(upload_to='documents', verbose_name=u'Imagen')
    entry_imagen = ThumbnailerImageField(upload_to='documents/', verbose_name=u'Document',
        default='documents/doc_default.jpg')
    entry_document = models.FileField(upload_to='documents/', verbose_name=u'Documento')
    def miniatura(self):
        image_path = get_thumbnailer(self.entry_imagen)['admin_thumb'].url
        return u'<img src="%s" alt="Link"/>' % image_path
    def documento(self):
        image_path = get_thumbnailer(self.entry_document)['admin_thumb'].url
        return u'<img src="%s" alt="Link"/>' % image_path
    miniatura.allow_tags = True #para poder visualizar la imagen y no se vea html
    documento.allow_tags = True

    class Meta:
        verbose_name = "Documento"
        verbose_name_plural="Documentos"

    def delete(self, *args, **kwargs):
        # You have to prepare what you need before delete the model
        storage, path = self.entry_imagen.storage, self.entry_imagen.path
        storage_doc, path_doc = self.entry_document.storage, self.entry_imagen.path
        # Delete the model before the file
        super(Document, self).delete(*args, **kwargs)
        # Delete the file after the model
        storage.delete(path)
        storage_doc.delete(path)


class Image(Entry):
    #entry_imagen = models.ImageField(upload_to='images', verbose_name=u'Imagen')
    entry_imagen = ThumbnailerImageField(upload_to=get_image_path, verbose_name=u'Imagen')

    def miniatura(self):
        image_path = get_thumbnailer(self.entry_imagen)['admin_thumb'].url
        return u'<img src="%s" alt="Link"/>' % image_path
    miniatura.allow_tags = True #para poder visualizar la imagen y no se vea html

    def site_thumb(self):
        image_path = get_thumbnailer(self.entry_imagen)['site_thumb'].url
        return image_path
    site_thumb.allow_tags = True #para poder visualizar la imagen y no se vea html

    def delete(self, *args, **kwargs):
        # You have to prepare what you need before delete the model
        storage, path = self.entry_imagen.storage, self.entry_imagen.path
        # Delete the model before the file
        super(Image, self).delete(*args, **kwargs)
        # Delete the file after the model
        storage.delete(path)

    class Meta:
        verbose_name = "Imagen"
        verbose_name_plural="Imagenes"
