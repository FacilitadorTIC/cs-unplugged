# Generated by Django 2.2.12 on 2020-06-02 02:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('at_home', '0008_auto_20200601_2342'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChallengeSubmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('language', models.CharField(max_length=25)),
                ('answer', models.CharField(default='', max_length=200)),
                ('correct', models.BooleanField()),
                ('challenge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='challenge_submissions', to='at_home.Challenge')),
            ],
        ),
        migrations.DeleteModel(
            name='ChallengeAttempt',
        ),
    ]
