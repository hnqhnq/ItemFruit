# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-07-06 06:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('area_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=128, null=True)),
            ],
            options={
                'db_table': 'area',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Collect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'collect',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Count',
            fields=[
                ('count_id', models.AutoField(primary_key=True, serialize=False)),
                ('look_times', models.IntegerField(blank=True, null=True)),
                ('area_look_times', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'count',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('facility_id', models.AutoField(primary_key=True, serialize=False)),
                ('facility_name', models.CharField(blank=True, max_length=128, null=True)),
                ('css', models.CharField(blank=True, max_length=512, null=True)),
            ],
            options={
                'db_table': 'facility',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('house_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=1024, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=512, null=True)),
                ('acreage', models.IntegerField(blank=True, null=True)),
                ('index_img_url', models.CharField(blank=True, max_length=1024, null=True)),
            ],
            options={
                'db_table': 'house',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HouseDetail',
            fields=[
                ('detail_id', models.AutoField(primary_key=True, serialize=False)),
                ('lease', models.CharField(blank=True, max_length=512, null=True)),
                ('pay_way', models.CharField(blank=True, max_length=512, null=True)),
                ('floor', models.CharField(blank=True, max_length=512, null=True)),
                ('house_head', models.CharField(blank=True, max_length=128, null=True)),
                ('community', models.CharField(blank=True, max_length=512, null=True)),
                ('surround_facility', models.CharField(blank=True, max_length=1024, null=True)),
                ('transportation', models.CharField(blank=True, max_length=1024, null=True)),
            ],
            options={
                'db_table': 'house_detail',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HouseFacility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'house_facility',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HouseImg',
            fields=[
                ('img_id', models.AutoField(primary_key=True, serialize=False)),
                ('url', models.CharField(blank=True, max_length=2048, null=True)),
            ],
            options={
                'db_table': 'house_img',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HouseType',
            fields=[
                ('type_id', models.AutoField(primary_key=True, serialize=False)),
                ('type_name', models.CharField(blank=True, max_length=128, null=True)),
            ],
            options={
                'db_table': 'house_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('role_id', models.AutoField(primary_key=True, serialize=False)),
                ('vip', models.IntegerField(blank=True, null=True)),
                ('admin', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'role',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('account', models.CharField(blank=True, max_length=128, null=True, unique=True)),
                ('password', models.CharField(blank=True, max_length=128, null=True)),
                ('phone', models.CharField(blank=True, max_length=128, null=True)),
                ('nick_name', models.CharField(blank=True, max_length=128, null=True)),
                ('avatar', models.CharField(blank=True, max_length=1024, null=True)),
                ('id_name', models.CharField(blank=True, max_length=64, null=True)),
                ('id_card', models.CharField(blank=True, max_length=64, null=True)),
                ('ticket', models.CharField(blank=True, max_length=255, null=True)),
                ('out_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
    ]
