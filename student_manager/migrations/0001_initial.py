# Generated by Django 4.2.4 on 2023-08-15 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accommodation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('domain', models.CharField(choices=[('DOMAIN_PRESENTATION', 'Presentation'), ('DOMAIN_RESPONSE', 'Response'), ('DOMAIN_SETTING', 'Setting'), ('DOMAIN_SCHEDULING', 'Scheduling')], max_length=20)),
                ('subdomain', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=31)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('student_id', models.CharField(max_length=12)),
                ('id', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('grade', models.CharField(choices=[('GRADE_K', 'Kindergarten'), ('GRADE_1', 'First'), ('GRADE_2', 'Second'), ('GRADE_3', 'Third'), ('GRADE_4', 'Fourth'), ('GRADE_5', 'Fifth'), ('GRADE_6', 'Sixth'), ('GRADE_7', 'Seventh'), ('GRADE_8', 'Eighth'), ('GRADE_9', 'Ninth'), ('GRADE_10', 'Tenth'), ('GRADE_11', 'Eleventh'), ('GRADE_12', 'Twelfth ')], max_length=8)),
                ('primary_exceptionality', models.CharField(max_length=20)),
                ('secondary_exceptionality', models.CharField(blank=True, max_length=20)),
                ('iep_due_date', models.DateField()),
                ('case_manager', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='student_manager.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Accommodation_List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateField()),
                ('accommodation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_manager.accommodation')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_manager.student')),
            ],
        ),
    ]
