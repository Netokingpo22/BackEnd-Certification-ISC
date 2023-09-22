# Generated by Django 4.2.5 on 2023-09-20 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Maestro', '0002_alter_maestro_tipoestudios'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maestro',
            name='tipoEstudios',
            field=models.CharField(choices=[('L', 'Licenciatura'), ('M', 'Maestria'), ('D', 'Doctorado'), ('P', 'Post Doctorado')], max_length=128),
        ),
    ]
