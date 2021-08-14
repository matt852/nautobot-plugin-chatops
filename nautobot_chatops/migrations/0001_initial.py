# Generated by Django 3.1.3 on 2021-02-22 02:18

import django.contrib.postgres.fields
from django.db import migrations, models, connection
import nautobot.utilities.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AccessGrant",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("created", models.DateField(auto_now_add=True, null=True)),
                ("last_updated", models.DateTimeField(auto_now=True, null=True)),
                ("command", models.CharField(max_length=64)),
                ("subcommand", models.CharField(max_length=64)),
                ("grant_type", models.CharField(max_length=32)),
                ("name", models.CharField(max_length=255)),
                ("value", models.CharField(max_length=255)),
            ],
            options={
                "ordering": ["command", "subcommand", "grant_type"],
            },
        ),
        migrations.CreateModel(
            name="CommandLog",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("start_time", models.DateTimeField(null=True)),
                ("runtime", models.DurationField(null=True)),
                ("user_name", models.CharField(max_length=255)),
                ("user_id", models.CharField(max_length=255)),
                ("platform", models.CharField(max_length=64)),
                ("platform_color", nautobot.utilities.fields.ColorField(max_length=6)),
                ("command", models.CharField(max_length=64)),
                ("subcommand", models.CharField(max_length=64)),
                ("status", models.CharField(default="succeeded", max_length=32)),
                ("details", models.CharField(default="", max_length=255)),
            ],
            options={
                "ordering": ["start_time"],
            },
        ),
        migrations.CreateModel(
            name="CommandToken",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("created", models.DateField(auto_now_add=True, null=True)),
                ("last_updated", models.DateTimeField(auto_now=True, null=True)),
                ("comment", models.CharField(blank=True, default="", max_length=255)),
                ("platform", models.CharField(max_length=32)),
                ("token", models.CharField(max_length=255)),
            ],
            options={
                "ordering": ["platform", "token", "comment"],
            },
        ),
    ]

    if connection.vendor == 'postgresql':
        operations.append(
            migrations.AddField(
                model_name='commandlog',
                name='params',
                field=django.contrib.postgres.fields.ArrayField(
                    base_field=django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(default="", max_length=255), size=None
                    ),
                    default=list,
                    size=None,
                )
            ),
        )
