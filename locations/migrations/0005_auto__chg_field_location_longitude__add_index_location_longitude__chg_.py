# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Location.longitude'
        db.alter_column('locations', 'longitude', self.gf('django.db.models.fields.CharField')(max_length=50))
        # Adding index on 'Location', fields ['longitude']
        db.create_index('locations', ['longitude'])


        # Changing field 'Location.latitude'
        db.alter_column('locations', 'latitude', self.gf('django.db.models.fields.CharField')(max_length=50))
        # Adding index on 'Location', fields ['latitude']
        db.create_index('locations', ['latitude'])


    def backwards(self, orm):
        # Removing index on 'Location', fields ['latitude']
        db.delete_index('locations', ['latitude'])

        # Removing index on 'Location', fields ['longitude']
        db.delete_index('locations', ['longitude'])


        # Changing field 'Location.longitude'
        db.alter_column('locations', 'longitude', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=6))

        # Changing field 'Location.latitude'
        db.alter_column('locations', 'latitude', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=6))

    models = {
        'locations.location': {
            'Meta': {'object_name': 'Location', 'db_table': "'locations'"},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'longitude': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        }
    }

    complete_apps = ['locations']