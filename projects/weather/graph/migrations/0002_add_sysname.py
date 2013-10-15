# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Location.sysname'
        db.add_column('graph_location', 'sysname',
                      self.gf('django.db.models.fields.SlugField')(unique=True, blank=True, default='', max_length=200),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Location.sysname'
        db.delete_column('graph_location', 'sysname')


    models = {
        'graph.location': {
            'Meta': {'object_name': 'Location'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location_id': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'sysname': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'blank': 'True', 'default': "''", 'max_length': '200'})
        },
        'graph.weatherlog': {
            'Meta': {'object_name': 'WeatherLog', 'ordering': "('-timestamp',)"},
            'humidity': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['graph.Location']"}),
            'temperature': ('django.db.models.fields.IntegerField', [], {}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'visibility': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'wind_speed': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'})
        }
    }

    complete_apps = ['graph']