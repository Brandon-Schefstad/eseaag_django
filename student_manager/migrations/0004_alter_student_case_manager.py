# Generated by Django 4.2.4 on 2023-08-16 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student_manager', '0003_alter_student_case_manager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='case_manager',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='student_manager.teacher'),
        ),
    ]
