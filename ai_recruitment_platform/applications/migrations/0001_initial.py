# Generated by Django 5.2.4 on 2025-07-08 20:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('candidates', '0001_initial'),
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applied_at', models.DateTimeField(auto_now_add=True, help_text='Timestamp when the application was submitted.')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Timestamp of the last update to the application.')),
                ('status', models.CharField(choices=[('applied', 'Applied'), ('screening', 'Screening'), ('interviewing', 'Interviewing'), ('assessment', 'Assessment'), ('offer', 'Offer Extended'), ('rejected', 'Rejected'), ('hired', 'Hired'), ('withdrawn', 'Withdrawn')], default='applied', help_text='Current status of the application in the hiring process.', max_length=20)),
                ('resume_score', models.FloatField(blank=True, help_text='AI-generated score indicating resume match quality.', null=True)),
                ('interview_score', models.FloatField(blank=True, help_text='AI-generated score from interviews.', null=True)),
                ('feedback_notes', models.TextField(blank=True, help_text='Recruiter or AI feedback on the application.', null=True)),
                ('candidate', models.ForeignKey(help_text='The candidate applying for the job.', on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='candidates.candidate')),
                ('job', models.ForeignKey(help_text='The job being applied for.', on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='jobs.job')),
            ],
            options={
                'verbose_name': 'Job Application',
                'verbose_name_plural': 'Job Applications',
                'ordering': ['-applied_at'],
                'unique_together': {('candidate', 'job')},
            },
        ),
    ]
