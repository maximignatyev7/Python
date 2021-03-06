# Generated by Django 3.1.2 on 2020-10-26 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='djangoClasses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=60)),
                ('course_number', models.IntegerField(default='', max_length=60)),
                ('instructor_name', models.CharField(blank=True, default='', max_length=60)),
                ('duration', models.DecimalField(decimal_places=2, default=0.0, max_digits=10000)),
            ],
        ),
    ]
