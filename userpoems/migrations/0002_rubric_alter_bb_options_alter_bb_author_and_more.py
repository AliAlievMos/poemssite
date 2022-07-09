# Generated by Django 4.0.6 on 2022-07-09 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userpoems', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rubric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=20, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Тема',
                'verbose_name_plural': 'Темы',
                'ordering': ['name'],
            },
        ),
        migrations.AlterModelOptions(
            name='bb',
            options={'ordering': ['-published'], 'verbose_name': 'Объявления', 'verbose_name_plural': 'Объявления'},
        ),
        migrations.AlterField(
            model_name='bb',
            name='author',
            field=models.CharField(max_length=20, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='bb',
            name='poem',
            field=models.TextField(blank=True, null=True, verbose_name='Моностих'),
        ),
        migrations.AlterField(
            model_name='bb',
            name='published',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано'),
        ),
        migrations.AddField(
            model_name='bb',
            name='rubric',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='userpoems.rubric', verbose_name='Тема'),
        ),
    ]