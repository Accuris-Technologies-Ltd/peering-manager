# Generated by Django 4.1.8 on 2023-04-30 10:42

import django.core.serializers.json
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("contenttypes", "0002_remove_content_type_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="Job",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("object_id", models.PositiveBigIntegerField(blank=True, null=True)),
                ("name", models.CharField(max_length=255)),
                ("created", models.DateTimeField()),
                ("started", models.DateTimeField(blank=True, null=True)),
                ("completed", models.DateTimeField(blank=True, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("pending", "Pending"),
                            ("running", "Running"),
                            ("completed", "Completed"),
                            ("errored", "Errored"),
                            ("failed", "Failed"),
                        ],
                        default="pending",
                        max_length=30,
                    ),
                ),
                (
                    "data",
                    models.JSONField(
                        blank=True,
                        encoder=django.core.serializers.json.DjangoJSONEncoder,
                        null=True,
                    ),
                ),
                ("job_id", models.UUIDField(unique=True)),
                (
                    "object_type",
                    models.ForeignKey(
                        help_text="The object type to which this job applies",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="jobs",
                        to="contenttypes.contenttype",
                        verbose_name="Object type",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"ordering": ["-created"]},
        ),
    ]
