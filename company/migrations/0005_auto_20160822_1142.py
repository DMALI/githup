# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-22 11:42
from __future__ import unicode_literals

import company.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_designation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(help_text='Please enter up to 9 characters only', max_length=250, validators=[company.models.validate_excess])),
                ('name', models.CharField(max_length=250)),
                ('wef', models.DateField(verbose_name='With effect from')),
                ('session_two_days', models.BooleanField(verbose_name='Session across 2 days')),
                ('week_off', models.CharField(choices=[('1', 'Sunday'), ('2', 'Monday'), ('3', 'Tuesday'), ('4', 'Wednesday'), ('5', 'Thursday'), ('6', 'Friday'), ('7', 'Saturday')], max_length=250, verbose_name='Shift week off')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Company')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AlterField(
            model_name='designation',
            name='division',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='company.Division'),
        ),
    ]
