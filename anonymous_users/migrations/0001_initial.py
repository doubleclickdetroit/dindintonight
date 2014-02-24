# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'AnonymousUser'
        db.create_table('anonymous_users', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(related_name='anonymous_users', to=orm['locations.Location'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('anonymous_users', ['AnonymousUser'])

        # Adding model 'AnonymousUserMealPurchaseHistory'
        db.create_table('anonymous_user_meal_purchase_history', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('anonymous_user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='meal_purchase_history', to=orm['anonymous_users.AnonymousUser'])),
            ('meal', self.gf('django.db.models.fields.related.ForeignKey')(related_name='anonymous_user_purchase_history', to=orm['meals.Meal'])),
            ('purchased_on', self.gf('django.db.models.fields.DateTimeField')()),
            ('deliver_on', self.gf('django.db.models.fields.DateTimeField')()),
            ('delivered_on', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('cancelled_on', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('is_delivered', self.gf('django.db.models.fields.IntegerField')()),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('anonymous_users', ['AnonymousUserMealPurchaseHistory'])

        # Adding model 'AnonymousUserPaymentInfo'
        db.create_table('anonymous_user_payment_info', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('anonymous_user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='payment_info', to=orm['anonymous_users.AnonymousUser'])),
            ('card', self.gf('django.db.models.fields.related.ForeignKey')(related_name='anonymous_user_payment_info', to=orm['cards.Card'])),
            ('stripe_token', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('anonymous_users', ['AnonymousUserPaymentInfo'])


    def backwards(self, orm):
        # Deleting model 'AnonymousUser'
        db.delete_table('anonymous_users')

        # Deleting model 'AnonymousUserMealPurchaseHistory'
        db.delete_table('anonymous_user_meal_purchase_history')

        # Deleting model 'AnonymousUserPaymentInfo'
        db.delete_table('anonymous_user_payment_info')


    models = {
        'anonymous_users.anonymoususer': {
            'Meta': {'object_name': 'AnonymousUser', 'db_table': "'anonymous_users'"},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'anonymous_users'", 'to': "orm['locations.Location']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'anonymous_users.anonymoususermealpurchasehistory': {
            'Meta': {'object_name': 'AnonymousUserMealPurchaseHistory', 'db_table': "'anonymous_user_meal_purchase_history'"},
            'anonymous_user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'meal_purchase_history'", 'to': "orm['anonymous_users.AnonymousUser']"}),
            'cancelled_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'deliver_on': ('django.db.models.fields.DateTimeField', [], {}),
            'delivered_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_delivered': ('django.db.models.fields.IntegerField', [], {}),
            'meal': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'anonymous_user_purchase_history'", 'to': "orm['meals.Meal']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'purchased_on': ('django.db.models.fields.DateTimeField', [], {})
        },
        'anonymous_users.anonymoususerpaymentinfo': {
            'Meta': {'object_name': 'AnonymousUserPaymentInfo', 'db_table': "'anonymous_user_payment_info'"},
            'anonymous_user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'payment_info'", 'to': "orm['anonymous_users.AnonymousUser']"}),
            'card': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'anonymous_user_payment_info'", 'to': "orm['cards.Card']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'stripe_token': ('django.db.models.fields.CharField', [], {'max_length': '45'})
        },
        'cards.card': {
            'Meta': {'object_name': 'Card', 'db_table': "'cards'"},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'locations.location': {
            'Meta': {'object_name': 'Location', 'db_table': "'locations'"},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'meals.meal': {
            'Meta': {'object_name': 'Meal', 'db_table': "'meals'"},
            'available_ending': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'available_starting': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'vendor_location': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'meals'", 'to': "orm['vendors.VendorLocation']"})
        },
        'vendors.vendor': {
            'Meta': {'object_name': 'Vendor', 'db_table': "'vendors'"},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'vendors.vendorlocation': {
            'Meta': {'object_name': 'VendorLocation', 'db_table': "'vendor_locations'"},
            'address1': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'address3': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['locations.Location']"}),
            'manager': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'vendor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'locations'", 'to': "orm['vendors.Vendor']"}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['anonymous_users']