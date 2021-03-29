# Generated by Django 2.2.14 on 2021-03-25 17:37

import json
import uuid

import django.db.models.deletion
from django.db import migrations, models

jasmine_defaults = {
    "option": "daily",
    "tz_str": "America/New_York",
    "save_traj": "",  # intentionally left as a falsy value
    # "study_folder": "",
    # "output_folder": "",
    # "parameters": "",
    # "beiwe_id": "",
}

willow_defaults = {
    "option": "daily",
    "tz_str": "America/New_York",
    # "study_folder": "",
    # "output_folder": "",
}


def seed_forest_metadata(apps, schema_editor):
    """
    Seed initial default ForestMetadata objects
    """
    db_alias = schema_editor.connection.alias
    ForestMetadata = apps.get_model("database", "ForestMetadata")
    ForestMetadata.objects.using(db_alias).create(
        default=True,
        notes="The default parameters",
        name="default",
        jasmine_json_string=json.dumps(jasmine_defaults),
        willow_json_string=json.dumps(willow_defaults),
    )


def seed_study_forest_metadata(apps, schema_editor):
    """
    Add the default metadata to all existing studies
    """
    db_alias = schema_editor.connection.alias
    ForestMetadata = apps.get_model("database", "ForestMetadata")
    Study = apps.get_model("database", "Study")
    default_metadata = ForestMetadata.objects.get(default=True)
    Study.objects.using(db_alias).all().update(
        forest_metadata=default_metadata
    )


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0049_auto_20210223_2005'),
    ]

    operations = [
        migrations.CreateModel(
            name='ForestMetadata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('default', models.NullBooleanField(unique=True)),
                ('notes', models.TextField(blank=True)),
                ('name', models.TextField(blank=True)),
                ('jasmine_json_string', models.TextField()),
                ('willow_json_string', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RenameField(
            model_name='foresttracker',
            old_name='date_end',
            new_name='data_date_end',
        ),
        migrations.RenameField(
            model_name='foresttracker',
            old_name='date_start',
            new_name='data_date_start',
        ),
        migrations.RemoveField(
            model_name='foresttracker',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='foresttracker',
            name='metadata_hash',
        ),
        migrations.RemoveField(
            model_name='foresttracker',
            name='start_time',
        ),
        migrations.RemoveField(
            model_name='summarystatisticdaily',
            name='study',
        ),
        migrations.AddField(
            model_name='foresttracker',
            name='external_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AddField(
            model_name='foresttracker',
            name='process_download_end_time',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='foresttracker',
            name='process_end_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='foresttracker',
            name='process_start_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='foresttracker',
            name='forest_tree',
            field=models.TextField(choices=[('jasmine', 'jasmine'), ('willow', 'willow')]),
        ),
        migrations.AlterField(
            model_name='foresttracker',
            name='metadata',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='database.ForestMetadata'),
        ),
        migrations.AlterField(
            model_name='foresttracker',
            name='status',
            field=models.TextField(choices=[('Queued', 'Queued'), ('Running', 'Running'), ('Success', 'Success'), ('Error', 'Error'), ('Cancelled', 'Cancelled')]),
        ),
        migrations.AlterField(
            model_name='summarystatisticdaily',
            name='acceleration_direction',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='summarystatisticdaily',
            name='accelerometer_coverage_fraction',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='summarystatisticdaily',
            name='accelerometer_signal_variability',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='summarystatisticdaily',
            name='accelerometer_univariate_summaries',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='summarystatisticdaily',
            name='awake_onset_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='summarystatisticdaily',
            name='call_incoming_count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='summarystatisticdaily',
            name='call_incoming_degree',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='summarystatisticdaily',
            name='call_incoming_duration',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='summarystatisticdaily',
            name='call_incoming_responsiveness',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='summarystatisticdaily',
            name='call_outgoing_count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='summarystatisticdaily',
            name='call_outgoing_degree',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='summarystatisticdaily',
            name='call_outgoing_duration',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='summarystatisticdaily',
            name='device_proximity',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='summarystatisticdaily',
            name='distance_diameter',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='summarystatisticdaily',
            name='distance_from_home',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='summarystatisticdaily',
            name='distance_traveled',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='summarystatisticdaily',
            name='flight_distance_average',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='summarystatisticdaily',
            name='flight_distance_standard_deviation',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='summarystatisticdaily',
            name='flight_duration_average',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='summarystatisticdaily',
            name='flight_duration_standard_deviation',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='summarystatisticdaily',
            name='gps_data_missing_duration',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='summarystatisticdaily',
            name='home_duration',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='summarystatisticdaily',
            name='physical_circadian_rhythm',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='summarystatisticdaily',
            name='physical_circadian_rhythm_stratified',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='summarystatisticdaily',
            name='radius_of_gyration',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='summarystatisticdaily',
            name='significant_location_count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='summarystatisticdaily',
            name='significant_location_entropy',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='summarystatisticdaily',
            name='sleep_duration',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='summarystatisticdaily',
            name='sleep_onset_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='summarystatisticdaily',
            name='stationary_fraction',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='summarystatisticdaily',
            name='text_incoming_count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='summarystatisticdaily',
            name='text_incoming_degree',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='summarystatisticdaily',
            name='text_incoming_length',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='summarystatisticdaily',
            name='text_incoming_responsiveness',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='summarystatisticdaily',
            name='text_outgoing_count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='summarystatisticdaily',
            name='text_outgoing_degree',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='summarystatisticdaily',
            name='text_outgoing_length',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='summarystatisticdaily',
            name='text_reciprocity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='summarystatisticdaily',
            name='total_power_events',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='summarystatisticdaily',
            name='total_screen_events',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='summarystatisticdaily',
            name='total_unlock_events',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='study',
            name='forest_metadata',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='database.ForestMetadata'),
        ),
        migrations.RunPython(seed_forest_metadata, migrations.RunPython.noop),
        migrations.RunPython(seed_study_forest_metadata, migrations.RunPython.noop),
        migrations.AlterField(
            model_name='study',
            name='forest_metadata',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT,
                                    to='database.ForestMetadata'),
        ),
        migrations.AddField(
            model_name='summarystatisticdaily',
            name='jasmine_tracker',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='jasmine_summary_statistics', to='database.ForestMetadata'),
        ),
        migrations.AddField(
            model_name='summarystatisticdaily',
            name='willow_tracker',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='willow_summary_statistics', to='database.ForestMetadata'),
        ),
    ]
