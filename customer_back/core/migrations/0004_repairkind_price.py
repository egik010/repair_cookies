# Generated by Django 4.2.3 on 2023-07-21 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0003_delete_category_remove_order_comments_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="RepairKind",
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
                ("name", models.CharField(max_length=100, verbose_name="Название")),
            ],
            options={
                "verbose_name": "Вид ремонта",
                "verbose_name_plural": "Виды ремонта",
            },
        ),
        migrations.CreateModel(
            name="Price",
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
                (
                    "equipment_category",
                    models.CharField(
                        choices=[
                            ("TELEPHONE", "телефон"),
                            ("LAPTOP", "ноутбук"),
                            ("TABLET", "планшет"),
                        ],
                        max_length=15,
                        verbose_name="Техника",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=100, verbose_name="Название ремонта"),
                ),
                (
                    "value",
                    models.DecimalField(
                        decimal_places=2,
                        default=0.0,
                        max_digits=12,
                        verbose_name="Цена",
                    ),
                ),
                (
                    "repair_kind",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="prices_for_kind",
                        to="core.repairkind",
                        verbose_name="Вид ремонта",
                    ),
                ),
                (
                    "repair_subkind",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="prices_for_subkind",
                        to="core.repairkind",
                        verbose_name="Подвид ремонта",
                    ),
                ),
            ],
            options={
                "verbose_name": "Расценка на ремонт",
                "verbose_name_plural": "Расценки на ремонт",
            },
        ),
    ]
