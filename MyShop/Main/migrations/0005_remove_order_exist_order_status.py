# Generated by Django 4.2.2 on 2024-08-28 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0004_alter_order_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='exist',
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('processing', 'В обработке'), ('completed', 'Выполнен'), ('cancelled', 'Отменён')], default='processing', max_length=10, verbose_name='Статус заказа'),
        ),
    ]