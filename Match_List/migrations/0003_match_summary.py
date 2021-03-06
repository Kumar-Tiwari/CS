# Generated by Django 3.1.2 on 2020-10-09 06:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Match_List', '0002_match_details_winner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match_Summary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('player1_points', models.IntegerField()),
                ('player2_points', models.IntegerField()),
                ('maps', models.CharField(choices=[('DustII', 'DUST II'), ('Inferno', 'Inferno'), ('Mirage', 'Mirage'), ('Nuke', 'Nuke'), ('Overpass', 'Overpass'), ('Vertigo', 'Vertigo')], default='DustII', max_length=15)),
                ('gun_banned_player1', models.CharField(choices=[('AK', 'Ak'), ('AMP', 'AMP'), ('AUG', 'AUG'), ('GAY_GUN', 'SCAR'), ('Others', 'Others')], max_length=15)),
                ('gun_banned_player2', models.CharField(choices=[('AK', 'Ak'), ('AMP', 'AMP'), ('AUG', 'AUG'), ('GAY_GUN', 'SCAR'), ('Others', 'Others')], max_length=15)),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='match', to='Match_List.match_details')),
            ],
        ),
    ]
