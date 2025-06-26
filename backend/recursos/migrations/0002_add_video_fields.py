from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        ('recursos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tip',
            name='video',
            field=models.FileField(upload_to='tips/videos/', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tip',
            name='video_url',
            field=models.CharField(max_length=500, blank=True, null=True),
        ),
    ] 