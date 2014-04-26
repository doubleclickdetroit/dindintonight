# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding index on 'Location', fields ['city']
        db.create_index('locations', ['city'])

        # Adding index on 'Location', fields ['state']
        db.create_index('locations', ['state'])

        # Adding index on 'Location', fields ['zip_code']
        db.create_index('locations', ['zip_code'])


    def backwards(self, orm):
        # Removing index on 'Location', fields ['zip_code']
        db.delete_index('locations', ['zip_code'])

        # Removing index on 'Location', fields ['state']
        db.delete_index('locations', ['state'])

        # Removing index on 'Location', fields ['city']
        db.delete_index('locations', ['city'])


    models = {
        'locations.location': {
            'Meta': {'object_name': 'Location', 'db_table': "'locations'"},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '6'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '6'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        }
    }

    complete_apps = ['locations']