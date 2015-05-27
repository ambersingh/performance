# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perform', '0003_auto_20150525_0452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_para',
            name='weightage',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
