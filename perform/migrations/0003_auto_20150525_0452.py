# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perform', '0002_auto_20150523_0548'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee_Para',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('weightage', models.PositiveIntegerField()),
                ('score', models.PositiveIntegerField()),
                ('pub_month', models.CharField(max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('paraname', models.CharField(max_length=30)),
            ],
        ),
        migrations.RenameModel(
            old_name='Person',
            new_name='Employee',
        ),
        migrations.RemoveField(
            model_name='marksheet',
            name='person',
        ),
        migrations.DeleteModel(
            name='Marksheet',
        ),
        migrations.AddField(
            model_name='employee_para',
            name='employee',
            field=models.ForeignKey(to='perform.Employee'),
        ),
        migrations.AddField(
            model_name='employee_para',
            name='parameter',
            field=models.ForeignKey(to='perform.Parameter'),
        ),
    ]
