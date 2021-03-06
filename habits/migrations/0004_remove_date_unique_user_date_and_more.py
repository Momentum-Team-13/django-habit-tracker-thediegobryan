# Generated by Django 4.0.6 on 2022-07-15 11:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0003_alter_date_date'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='date',
            name='unique_user_date',
        ),
        migrations.RemoveField(
            model_name='date',
            name='tracked_habits',
        ),
        migrations.AddField(
            model_name='date',
            name='tracked_habit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dates', to='habits.habit'),
        ),
        migrations.AlterField(
            model_name='habit',
            name='creator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='habits', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddConstraint(
            model_name='date',
            constraint=models.UniqueConstraint(fields=('tracked_habit', 'date'), name='unique_user_date'),
        ),
    ]
