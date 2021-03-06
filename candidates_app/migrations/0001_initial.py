# Generated by Django 3.1.7 on 2021-04-03 15:04
import django.core.validators
import django.db.models.deletion
from django.db import migrations
from django.db import models

import candidates_app.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('name', models.CharField(max_length=100)),
                (
                    'reference_code',
                    models.CharField(
                        max_length=8,
                        validators=[
                            candidates_app.validators.reference_code_validator,
                        ],
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'value',
                    models.FloatField(
                        validators=[
                            django.core.validators.MinValueValidator(0.0),
                            django.core.validators.MaxValueValidator(100.0),
                        ],
                    ),
                ),
                (
                    'candidate',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='scores',
                        to='candidates_app.candidate',
                    ),
                ),
            ],
        ),
        migrations.AddConstraint(
            model_name='candidate',
            constraint=models.UniqueConstraint(
                fields=('name', 'reference_code'),
                name='unique candidate',
            ),
        ),
    ]
