# Generated by Django 5.1.1 on 2025-05-02 14:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_case_updated_at'),
        ('intel', '0003_intelligencesource_tags_remove_intelreport_tags_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='intelreport',
            name='case',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='intel_reports', to='core.case'),
            preserve_default=False,
        ),
    ]
