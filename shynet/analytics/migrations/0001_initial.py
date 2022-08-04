# Generated by Django 3.0.5 on 2020-04-14 14:40

import django.db.models.deletion
from django.db import migrations, models

import analytics.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Session",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=analytics.models._default_uuid,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("identifier", models.TextField(blank=True, db_index=True)),
                ("start_time", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("last_seen", models.DateTimeField(auto_now_add=True)),
                ("user_agent", models.TextField()),
                ("browser", models.TextField()),
                ("device", models.TextField()),
                (
                    "device_type",
                    models.CharField(
                        choices=[
                            ("PHONE", "Phone"),
                            ("TABLET", "Tablet"),
                            ("DESKTOP", "Desktop"),
                            ("ROBOT", "Robot"),
                            ("OTHER", "Other"),
                        ],
                        default="OTHER",
                        max_length=7,
                    ),
                ),
                ("os", models.TextField()),
                ("ip", models.GenericIPAddressField(db_index=True)),
                ("asn", models.TextField(blank=True)),
                ("country", models.TextField(blank=True)),
                ("longitude", models.FloatField(null=True)),
                ("latitude", models.FloatField(null=True)),
                ("time_zone", models.TextField(blank=True)),
                (
                    "service",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.Service"
                    ),
                ),
            ],
            options={
                "ordering": ["-start_time"],
            },
        ),
        migrations.CreateModel(
            name="Hit",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("initial", models.BooleanField(db_index=True, default=True)),
                ("start_time", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("last_seen", models.DateTimeField(auto_now_add=True)),
                ("heartbeats", models.IntegerField(default=0)),
                ("tracker", models.TextField()),
                ("location", models.TextField(blank=True, db_index=True)),
                ("referrer", models.TextField(blank=True, db_index=True)),
                ("load_time", models.FloatField(null=True)),
                (
                    "session",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="analytics.Session",
                    ),
                ),
            ],
            options={
                "ordering": ["-start_time"],
            },
        ),
        migrations.AddIndex(
            model_name="session",
            index=models.Index(
                fields=["service", "-start_time"], name="analytics_s_service_4b1137_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="session",
            index=models.Index(
                fields=["service", "identifier"], name="analytics_s_service_82ab21_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="hit",
            index=models.Index(
                fields=["session", "-start_time"], name="analytics_h_session_b2667f_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="hit",
            index=models.Index(
                fields=["session", "location"], name="analytics_h_session_775f5a_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="hit",
            index=models.Index(
                fields=["session", "referrer"], name="analytics_h_session_98b8bf_idx"
            ),
        ),
    ]
