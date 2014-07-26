# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Location.latitude'
        db.add_column('locations', 'latitude',
                      self.gf('django.db.models.fields.DecimalField')(default=None, max_digits=10, decimal_places=6),
                      keep_default=False)

        # Adding field 'Location.longitude'
        db.add_column('locations', 'longitude',
                      self.gf('django.db.models.fields.DecimalField')(default=None, max_digits=10, decimal_places=6),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Location.latitude'
        db.delete_column('locations', 'latitude')

        # Deleting field 'Location.longitude'
        db.delete_column('locations', 'longitude')


    models = {
        'locations.location': {
            'Meta': {'object_name': 'Location', 'db_table': "'locations'"},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '6'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '6'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['locations']