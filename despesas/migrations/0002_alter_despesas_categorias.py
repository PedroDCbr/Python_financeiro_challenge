# Generated by Django 4.1 on 2022-08-29 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('despesas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='despesas',
            name='categorias',
            field=models.CharField(choices=[('Outros', 'Outros'), ('Moradia', 'Moradia'), ('Transporte', 'Transporte'), ('Alimentação', 'Alimentacao'), ('Cartões', 'Cartoes'), ('Educação', 'Educacao'), ('Saúde', 'Saude'), ('Imprevistos', 'Imprevistos'), ('Lazer', 'Lazer')], default='Outros', max_length=11),
        ),
    ]