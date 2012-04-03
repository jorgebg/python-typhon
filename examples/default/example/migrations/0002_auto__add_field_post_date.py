# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Post.date'
        db.add_column('example_post', 'date',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime.today()),
                      keep_default=False)

    def backwards(self, orm):
        # Deleting field 'Post.date'
        db.delete_column('example_post', 'date')

    models = {
        'example.post': {
            'Meta': {'object_name': 'Post'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['example']