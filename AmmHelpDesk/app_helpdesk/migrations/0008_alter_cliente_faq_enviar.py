# Generated by Django 4.2.1 on 2023-06-28 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_helpdesk', '0007_cliente_faq_enviar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='faq_enviar',
            field=models.CharField(blank=True, db_column='Faq_Enviado', max_length=19, null=True),
        ),
    ]
