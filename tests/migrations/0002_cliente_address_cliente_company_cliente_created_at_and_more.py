# Generated by Django 4.2.3 on 2023-08-02 16:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='address',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='company',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='phone_number',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='empleado',
            name='address',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='empleado',
            name='department',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='empleado',
            name='hire_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='empleado',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='empleado',
            name='phone_number',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='empleado',
            name='salary',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='producto',
            name='category',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='producto',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producto',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='producto',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producto',
            name='stock',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='producto',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
