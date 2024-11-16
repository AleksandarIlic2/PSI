# Generated by Django 5.0.4 on 2024-06-06 15:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Korisnik',
            fields=[
                ('idkor', models.AutoField(db_column='IdKor', primary_key=True, serialize=False)),
                ('mejl', models.CharField(db_column='Mejl', max_length=45, unique=True)),
                ('uloga', models.CharField(db_column='Uloga', max_length=45)),
                ('sifra', models.CharField(db_column='Sifra', max_length=45)),
                ('slika', models.BinaryField(blank=True, db_column='Slika', null=True)),
            ],
            options={
                'db_table': 'Korisnik',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Paket',
            fields=[
                ('idpak', models.AutoField(db_column='IdPak', primary_key=True, serialize=False)),
                ('brtermina', models.IntegerField(db_column='BrTermina')),
                ('dana', models.IntegerField(db_column='Dana')),
                ('cena', models.DecimalField(db_column='Cena', decimal_places=2, max_digits=10)),
                ('naziv', models.CharField(db_column='Naziv', max_length=40)),
            ],
            options={
                'db_table': 'Paket',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('idsala', models.AutoField(db_column='IdSala', primary_key=True, serialize=False)),
                ('naziv', models.CharField(db_column='Naziv', max_length=45, unique=True)),
            ],
            options={
                'db_table': 'Sala',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Trening',
            fields=[
                ('idtre', models.AutoField(db_column='idTre', primary_key=True, serialize=False)),
                ('tip', models.CharField(db_column='Tip', max_length=45)),
            ],
            options={
                'db_table': 'Trening',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Komentar',
            fields=[
                ('idkom', models.AutoField(db_column='IdKom', primary_key=True, serialize=False)),
                ('tekst', models.CharField(db_column='Tekst', max_length=200)),
                ('status', models.IntegerField(db_column='Status')),
                ('datum', models.DateTimeField(db_column='Datum')),
                ('idautor', models.ForeignKey(blank=True, db_column='IdAutor', null=True, on_delete=django.db.models.deletion.CASCADE, to='proj.korisnik')),
                ('idkomentarisan', models.ForeignKey(db_column='IdKomentarisan', on_delete=django.db.models.deletion.CASCADE, related_name='komentar_idkomentarisan_set', to='proj.korisnik')),
            ],
            options={
                'db_table': 'Komentar',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Drzi',
            fields=[
                ('iddrzi', models.AutoField(db_column='IdDrzi', primary_key=True, serialize=False)),
                ('idkor', models.ForeignKey(db_column='IdKor', on_delete=django.db.models.deletion.CASCADE, to='proj.korisnik')),
                ('idtre1', models.ForeignKey(db_column='IdTre1', on_delete=django.db.models.deletion.CASCADE, to='proj.trening')),
            ],
            options={
                'db_table': 'Drzi',
                'managed': True,
                'unique_together': {('idkor', 'idtre1')},
            },
        ),
        migrations.CreateModel(
            name='Pretplata',
            fields=[
                ('idpre', models.AutoField(db_column='IdPre', primary_key=True, serialize=False)),
                ('datumdo', models.DateTimeField(db_column='DatumDo')),
                ('preostalotermina', models.IntegerField(db_column='PreostaloTermina')),
                ('idpretplaceni', models.ForeignKey(db_column='IdPretplaceni', on_delete=django.db.models.deletion.CASCADE, to='proj.korisnik')),
            ],
            options={
                'db_table': 'Pretplata',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Podrzava',
            fields=[
                ('idpodrzava', models.AutoField(db_column='IdPodrzava', primary_key=True, serialize=False)),
                ('idsala', models.ForeignKey(db_column='IdSala', on_delete=django.db.models.deletion.CASCADE, to='proj.sala')),
                ('idtre2', models.ForeignKey(db_column='IdTre2', on_delete=django.db.models.deletion.CASCADE, to='proj.trening')),
            ],
            options={
                'db_table': 'Podrzava',
                'managed': True,
                'unique_together': {('idsala', 'idtre2')},
            },
        ),
        migrations.CreateModel(
            name='Termin',
            fields=[
                ('idter', models.AutoField(db_column='IdTer', primary_key=True, serialize=False)),
                ('dan', models.CharField(db_column='Dan', max_length=3)),
                ('pocetak', models.TimeField(db_column='Pocetak')),
                ('kraj', models.TimeField(db_column='Kraj')),
                ('preostalo', models.IntegerField(db_column='Preostalo')),
                ('iddrzi', models.ForeignKey(db_column='IdDrzi', on_delete=django.db.models.deletion.CASCADE, to='proj.drzi')),
                ('idpodrzava', models.ForeignKey(db_column='IdPodrzava', on_delete=django.db.models.deletion.CASCADE, to='proj.podrzava')),
            ],
            options={
                'db_table': 'Termin',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Prati',
            fields=[
                ('idprati', models.AutoField(db_column='IdPrati', primary_key=True, serialize=False)),
                ('idkor', models.ForeignKey(db_column='IdKor', on_delete=django.db.models.deletion.CASCADE, to='proj.korisnik')),
                ('idter', models.ForeignKey(db_column='IdTer', on_delete=django.db.models.deletion.CASCADE, to='proj.termin')),
            ],
            options={
                'db_table': 'Prati',
                'managed': True,
                'unique_together': {('idkor', 'idter')},
            },
        ),
        migrations.CreateModel(
            name='Pokriva',
            fields=[
                ('idpokriva', models.AutoField(db_column='IdPokriva', primary_key=True, serialize=False)),
                ('idpre', models.ForeignKey(db_column='IdPre', on_delete=django.db.models.deletion.CASCADE, to='proj.pretplata')),
                ('idtre', models.ForeignKey(db_column='IdTre', on_delete=django.db.models.deletion.CASCADE, to='proj.trening')),
            ],
            options={
                'db_table': 'Pokriva',
                'managed': True,
                'unique_together': {('idpre', 'idtre')},
            },
        ),
        migrations.CreateModel(
            name='Obuhvata',
            fields=[
                ('idobuh', models.AutoField(db_column='IdObuh', primary_key=True, serialize=False)),
                ('idpak', models.ForeignKey(db_column='IdPak', on_delete=django.db.models.deletion.CASCADE, to='proj.paket')),
                ('idtre', models.ForeignKey(db_column='IdTre', on_delete=django.db.models.deletion.CASCADE, to='proj.trening')),
            ],
            options={
                'db_table': 'Obuhvata',
                'managed': True,
                'unique_together': {('idtre', 'idpak')},
            },
        ),
    ]