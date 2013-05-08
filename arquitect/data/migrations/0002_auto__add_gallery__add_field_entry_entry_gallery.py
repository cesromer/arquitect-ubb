# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Gallery'
        db.create_table('data_gallery', (
            ('gallery_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('gallery_author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True)),
            ('gallery_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('data', ['Gallery'])

        # Adding field 'Entry.entry_gallery'
        db.add_column('data_entry', 'entry_gallery',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['data.Gallery']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Gallery'
        db.delete_table('data_gallery')

        # Deleting field 'Entry.entry_gallery'
        db.delete_column('data_entry', 'entry_gallery_id')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'data.document': {
            'Meta': {'object_name': 'Document', '_ormbases': ['data.Entry']},
            'entry_document': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'entry_imagen': ('django.db.models.fields.files.ImageField', [], {'default': "'documents/doc_default.jpg'", 'max_length': '100'}),
            'entry_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['data.Entry']", 'unique': 'True', 'primary_key': 'True'})
        },
        'data.entry': {
            'Meta': {'object_name': 'Entry'},
            'entry_author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'entry_desc': ('django.db.models.fields.TextField', [], {}),
            'entry_gallery': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': "orm['data.Gallery']"}),
            'entry_slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'entry_title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'is_mainphoto': ('django.db.models.fields.CharField', [], {'default': "'NO'", 'max_length': '2'}),
            'object_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'data.gallery': {
            'Meta': {'object_name': 'Gallery'},
            'gallery_author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'gallery_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'gallery_name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'data.image': {
            'Meta': {'object_name': 'Image', '_ormbases': ['data.Entry']},
            'entry_imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'entry_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['data.Entry']", 'unique': 'True', 'primary_key': 'True'})
        },
        'taggit.tag': {
            'Meta': {'object_name': 'Tag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'})
        },
        'taggit.taggeditem': {
            'Meta': {'object_name': 'TaggedItem'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'taggit_taggeditem_tagged_items'", 'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'taggit_taggeditem_items'", 'to': "orm['taggit.Tag']"})
        }
    }

    complete_apps = ['data']