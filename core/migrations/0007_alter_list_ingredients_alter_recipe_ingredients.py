# Generated by Django 4.2.5 on 2023-12-28 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_quantity_ingredient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='ingredients',
            field=models.ManyToManyField(blank=True, related_name='lists', to='core.quantity'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(related_name='recipes', to='core.quantity'),
        ),
    ]
