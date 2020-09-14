# Generated by Django 3.0.8 on 2020-09-14 20:19

import ConnectIP.storage_backends
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Patentinformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publicationNumber', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=500)),
                ('publicationDate', models.DateField()),
                ('license', models.CharField(blank=True, max_length=100)),
                ('publicationOwner', models.CharField(blank=True, max_length=100)),
                ('region', models.CharField(blank=True, max_length=100)),
                ('publicationUsage', models.CharField(blank=True, max_length=100)),
                ('publicationType', models.CharField(blank=True, max_length=100)),
                ('stageComplete', models.BooleanField()),
                ('stageSelected', models.BooleanField()),
                ('stageApproved', models.BooleanField()),
                ('category', models.CharField(blank=True, max_length=100)),
                ('type', models.CharField(blank=True, max_length=100)),
                ('treatment', models.CharField(blank=True, max_length=100)),
                ('operation', models.CharField(blank=True, max_length=100)),
                ('creator', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', storage=ConnectIP.storage_backends.PublicMediaStorage(), upload_to='')),
                ('qualification', models.CharField(max_length=100)),
                ('research', models.CharField(max_length=100)),
                ('location', django_countries.fields.CountryField(max_length=2)),
                ('creator', models.BooleanField(default=False)),
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PatentSummary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startDate', models.DateField(null=True)),
                ('ad1', models.CharField(max_length=100)),
                ('ad2', models.PositiveIntegerField(null=True)),
                ('ad3', models.CharField(choices=[('published', 'Published/Pending'), ('granted', 'Granted'), ('active', 'Active'), ('inactive', 'Inactive')], max_length=9)),
                ('ad4', models.CharField(max_length=100)),
                ('ad5', models.URLField(max_length=300)),
                ('pr1', models.CharField(max_length=100)),
                ('pr2', models.CharField(choices=[('one', '1'), ('two', '2'), ('three', '3'), ('four', '4'), ('five', '5')], default='', max_length=5)),
                ('pr3', models.CharField(max_length=100)),
                ('pr4', models.CharField(choices=[('one', '1'), ('two', '2'), ('three', '3'), ('four', '4'), ('five', '5')], default='', max_length=5)),
                ('pr5', models.CharField(max_length=100)),
                ('pr6', models.PositiveIntegerField(null=True)),
                ('pr7', models.PositiveIntegerField(null=True)),
                ('pr8', models.CharField(max_length=100)),
                ('pr9', models.CharField(max_length=100)),
                ('tech1', models.CharField(choices=[('therapeutic', 'Therapeutic'), ('disease diagnosis tool', 'Disease diagnosis tool'), ('disease prognosis tool', 'Disease prognosis tool'), ('intervention prediction tool', 'Intervention prediction tool'), ('decision support', 'Decision support'), ('healthcare service optimization tool or platform', 'Healthcare service optimization tool or platform'), ('software', 'Software'), ('research tool', 'Research tool'), ('method of use', 'Method of use'), ('composition of matter', 'Composition of matter'), ('article of manufacture', 'Article of manufacture'), ('machine', 'Machine'), ('other', 'Other')], max_length=48)),
                ('tech2', models.CharField(max_length=100)),
                ('tech3', models.CharField(max_length=100)),
                ('tech4', models.CharField(max_length=100)),
                ('dev1', models.CharField(choices=[('Basic science research', '1 - Basic science research'), ('Technology conceptualized', '2 - Technology conceptualized'), ('In vitro proof of concept', '3 - In vitro proof of concept'), ('In vivo proof of concept', '4 - In vivo proof of concept'), ('Pre-clinical research', '5 - Pre-clinical research'), ('Clinical research (Phase I or equivalent)', '6 - Clinical research (Phase I or equivalent)'), ('Clinical research (Phase II or equivalent)', '7 - Clinical research (Phase II or equivalent)'), ('Clinical research (Phase III or equivalent)', '8 - Clinical research (Phase III or equivalent)'), ('Commercially available (optimization stage)', '9 - Commercially available (optimization stage)'), ('other', 'Other')], max_length=50)),
                ('dev2', models.CharField(max_length=100)),
                ('dev3', models.CharField(max_length=100)),
                ('comp1', models.CharField(choices=[('yes', 'Yes'), ('no', 'No'), ('unknown', 'Unknown')], max_length=8)),
                ('comp2', models.CharField(choices=[('yes', 'Yes'), ('no', 'No'), ('unknown', 'Unknown')], max_length=8)),
                ('comp3', models.CharField(choices=[('yes', 'Yes'), ('no', 'No'), ('unknown', 'Unknown')], max_length=8)),
                ('comp4', models.CharField(max_length=100)),
                ('comp5', models.CharField(choices=[('yes', 'Yes'), ('no', 'No'), ('unknown', 'Unknown')], max_length=8)),
                ('comp6', models.CharField(choices=[('yes', 'Yes'), ('incremental', 'Incremental Improvement'), ('unknown', 'N/A'), ('other', 'Other')], max_length=12)),
                ('comp7', models.CharField(choices=[('yes', 'Yes'), ('no', 'No'), ('unknown', 'Unknown')], max_length=8)),
                ('val1', models.CharField(choices=[('mechanism of action is clearly defined', 'Mechanism of action is clearly defined'), ('mechanism of action is speculative', 'Mechanism of action is speculative'), ('too complex', 'The underlying basic science is too complex and unlikely to be elucidated completely'), ("the empirical data doesn't make sense theoretically", "The empirical data doesn't make sense theoretically"), ("the underlying basic science doesn't matter", "The underlying basic science doesn't matter"), ('there is expert consensus on this being a good idea', 'There is expert consensus on this being a good idea'), ('other', 'Other')], max_length=200)),
                ('val2', models.CharField(choices=[('it', 'Inventor is the only source of any insights on the technology'), ('rt', 'Results supporting this technology has been reproduced independently by another researcher/organization'), ('st', 'Studies ongoing to assess reproducibility'), ('spt', 'Results not supportive of the technology have been produced independently by another researcher/organization'), ('unt', 'Unclear if anyone is working on this specific technology for the application protected by the patent'), ('other', 'Other')], max_length=200)),
                ('val3', models.CharField(max_length=100)),
                ('endtime', models.DateField(null=True)),
                ('exp', models.CharField(choices=[('one', '1'), ('two', '2'), ('three', '3'), ('four', '4'), ('five', '5')], default='', max_length=5)),
                ('feedback', models.TextField(max_length=500)),
                ('account', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CreatorSummary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad1', models.CharField(max_length=200)),
                ('ad2', models.CharField(max_length=200)),
                ('ad3', models.CharField(max_length=200)),
                ('ad4', models.CharField(max_length=200)),
                ('spd1', models.CharField(max_length=200)),
                ('spd2', models.CharField(max_length=200)),
                ('spd3', models.CharField(max_length=200)),
                ('spd4', models.CharField(max_length=200)),
                ('comp1', models.CharField(max_length=200)),
                ('comp2', models.CharField(max_length=200)),
                ('comp3', models.CharField(max_length=200)),
                ('comp4', models.CharField(max_length=200)),
                ('comp5', models.CharField(max_length=200)),
                ('tech1', models.CharField(max_length=200)),
                ('tech2', models.CharField(max_length=200)),
                ('tech3', models.CharField(max_length=200)),
                ('tech4', models.CharField(max_length=200)),
                ('tech5', models.CharField(max_length=200)),
                ('tech6', models.CharField(max_length=200)),
                ('tech7', models.CharField(max_length=200)),
                ('preImpact1', models.CharField(max_length=200)),
                ('preImpact2', models.CharField(max_length=200)),
                ('preImpact3', models.CharField(max_length=200)),
                ('market1', models.CharField(max_length=200)),
                ('market2', models.CharField(max_length=200)),
                ('market3', models.CharField(max_length=200)),
                ('market4', models.CharField(max_length=200)),
                ('market5', models.CharField(max_length=200)),
                ('account', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
