# Generated by Django 3.2.8 on 2021-11-12 06:26

from django.db import migrations, models
import django.db.models.deletion
import tips.models


class Migration(migrations.Migration):

    dependencies = [
        ('tips', '0002_alter_uploads_audio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField(auto_created=True, blank=True)),
                ('time_stamp', models.DateTimeField(auto_now=True)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=100)),
                ('hash', models.CharField(blank=True, max_length=255)),
                ('previous_hash', models.CharField(max_length=255)),
                ('nonce', models.CharField(blank=True, default=0, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Chain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(choices=[('Ambush', 'Ambush'), ('Bombing', 'Bombing'), ('Sucide Bombing', 'Sucide Bombing'), ('Active Shooter', 'Active Shooter'), ('Explosion', 'Explosion'), ('Cyberattack', 'Cyberattack'), ('Biological Attack', 'Biological Attack'), ('Chemical Attack', 'Chemical Attack'), ('Kidnapping', 'Kidnapping'), ('Storming', 'Stroming'), ('Radiological Attack', 'Radiological Attack'), ('Other', 'Other')], default='Cyber Attack', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('Ambush', 'Ambush'), ('Bombing', 'Bombing'), ('Sucide Bombing', 'Sucide Bombing'), ('Active Shooter', 'Active Shooter'), ('Explosion', 'Explosion'), ('Cyberattack', 'Cyberattack'), ('Biological Attack', 'Biological Attack'), ('Chemical Attack', 'Chemical Attack'), ('Kidnapping', 'Kidnapping'), ('Storming', 'Stroming'), ('Radiological Attack', 'Radiological Attack'), ('Other', 'Other')], default='Cyber Attack', max_length=50)),
                ('description', models.TextField()),
                ('video', models.FileField(upload_to='videos/', validators=[tips.models.validate_video_extension])),
                ('audio', models.FileField(upload_to='audios/', validators=[tips.models.validate_audio_extension])),
                ('image', models.ImageField(upload_to=tips.models.upload_image)),
                ('location', models.CharField(max_length=100)),
                ('event_date', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'Upload',
                'verbose_name_plural': 'Uploads',
            },
        ),
        migrations.DeleteModel(
            name='Uploads',
        ),
        migrations.AddField(
            model_name='block',
            name='chain',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tips.chain'),
        ),
    ]
