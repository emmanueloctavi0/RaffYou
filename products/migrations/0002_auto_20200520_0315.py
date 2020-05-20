# Generated by Django 3.0.6 on 2020-05-20 03:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')),
                ('rate', models.IntegerField(choices=[(1, 'Pésimo'), (2, 'Malo'), (3, 'Bueno'), (4, 'Muy bueno'), (5, 'Excelente')], default=1, verbose_name='Calificación')),
                ('comment', models.TextField(blank=True, max_length=300, verbose_name='Comentario')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Provider')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='provider',
            name='rate',
            field=models.ManyToManyField(blank=True, through='products.Score', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddConstraint(
            model_name='score',
            constraint=models.UniqueConstraint(fields=('user', 'provider'), name='unique_comment_by_user'),
        ),
    ]
