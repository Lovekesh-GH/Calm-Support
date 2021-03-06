# Generated by Django 3.2.8 on 2021-11-10 05:53

from django.db import migrations, models
import tips.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Uploads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('Ambush', 'Ambush'), ('Bombing', 'Bombing'), ('Sucide Bombing', 'Sucide Bombing'), ('Active Shooter', 'Active Shooter'), ('Explosion', 'Explosion'), ('Cyberattack', 'Cyberattack'), ('Biological Attack', 'Biological Attack'), ('Chemical Attack', 'Chemical Attack'), ('Kidnapping', 'Kidnapping'), ('Storming', 'Stroming'), ('Radiological Attack', 'Radiological Attack'), ('Other', 'Other')], default='Cyber Attack', max_length=50)),
                ('description', models.TextField()),
                ('video', models.FileField(upload_to='videos/', validators=[tips.models.validate_video_extension])),
                ('audio', models.FileField(upload_to='audio/', validators=[tips.models.validate_audio_extension])),
                ('image', models.ImageField(upload_to='images/')),
                ('location', models.CharField(max_length=100)),
                ('event_date', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'Upload',
                'verbose_name_plural': 'Uploads',
            },
        ),
    ]
