# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Device'
        db.create_table(u'pesteh_device', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base.Member'], null=True)),
            ('token', self.gf('django.db.models.fields.CharField')(unique=True, max_length=127)),
        ))
        db.send_create_signal(u'pesteh', ['Device'])

        # Adding model 'Message'
        db.create_table(u'pesteh_message', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('message_id', self.gf('django.db.models.fields.CharField')(max_length=63, null=True)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2015, 5, 24, 0, 0))),
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('type', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base.Member'])),
        ))
        db.send_create_signal(u'pesteh', ['Message'])

        # Adding M2M table for field devices on 'Message'
        m2m_table_name = db.shorten_name(u'pesteh_message_devices')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('message', models.ForeignKey(orm[u'pesteh.message'], null=False)),
            ('device', models.ForeignKey(orm[u'pesteh.device'], null=False))
        ))
        db.create_unique(m2m_table_name, ['message_id', 'device_id'])


    def backwards(self, orm):
        # Deleting model 'Device'
        db.delete_table(u'pesteh_device')

        # Deleting model 'Message'
        db.delete_table(u'pesteh_message')

        # Removing M2M table for field devices on 'Message'
        db.delete_table(db.shorten_name(u'pesteh_message_devices'))


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'base.baby': {
            'Meta': {'object_name': 'Baby'},
            'birth_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'birth_time': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['base.City']"}),
            'doctor': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'father_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'gender': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'height': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'hospital': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'mother_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'pregnancy': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'relatives': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['base.Member']", 'through': u"orm['base.BabyFamilyMembers']", 'symmetrical': 'False'}),
            'show_in_search': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'weight': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'base.babyfamilymembers': {
            'Meta': {'object_name': 'BabyFamilyMembers'},
            'baby': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['base.Baby']"}),
            'confirmed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'member': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['base.Member']"}),
            'relationship': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['base.Relationship']"})
        },
        u'base.city': {
            'Meta': {'object_name': 'City'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'base.member': {
            'Meta': {'object_name': 'Member'},
            'birth_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['base.City']"}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'default_page': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'member_default_page'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['network.Page']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'gender': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '63', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'settings': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base.MemberSettings']", 'null': 'True', 'blank': 'True'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'base.membersettings': {
            'Meta': {'object_name': 'MemberSettings'},
            'feed_help': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page_help': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'search_help': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'base.relationship': {
            'Meta': {'object_name': 'Relationship'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_female': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1000'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'network.page': {
            'Meta': {'object_name': 'Page'},
            'baby': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'page'", 'unique': 'True', 'to': u"orm['base.Baby']"}),
            'blocked': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'blocked'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['base.Member']"}),
            'cover_photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'likes': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'pages_liked'", 'to': u"orm['base.Member']", 'through': u"orm['network.Page_likes']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pages'", 'to': u"orm['base.Member']"}),
            'setting': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'})
        },
        u'network.page_likes': {
            'Meta': {'object_name': 'Page_likes'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'member': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base.Member']"}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['network.Page']"})
        },
        u'pesteh.device': {
            'Meta': {'object_name': 'Device'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'token': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '127'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base.Member']", 'null': 'True'})
        },
        u'pesteh.message': {
            'Meta': {'object_name': 'Message'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'devices': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['pesteh.Device']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message_id': ('django.db.models.fields.CharField', [], {'max_length': '63', 'null': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 5, 24, 0, 0)'}),
            'type': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base.Member']"})
        }
    }

    complete_apps = ['pesteh']