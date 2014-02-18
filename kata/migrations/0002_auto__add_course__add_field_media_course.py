# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Course'
        db.create_table(u'kata_course', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal(u'kata', ['Course'])

        # Adding field 'Media.course'
        db.add_column(u'kata_media', 'course',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['kata.Course'], null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Course'
        db.delete_table(u'kata_course')

        # Deleting field 'Media.course'
        db.delete_column(u'kata_media', 'course_id')


    models = {
        u'kata.course': {
            'Meta': {'object_name': 'Course'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'kata.media': {
            'Meta': {'object_name': 'Media'},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['kata.Course']", 'null': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['kata']