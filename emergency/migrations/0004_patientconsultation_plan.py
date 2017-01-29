# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emergency', '0003_auto_20170129_1402'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientconsultation',
            name='plan',
            field=models.TextField(null=True, blank=True),
        ),
    ]
