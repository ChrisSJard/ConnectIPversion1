from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from ConnectIP.storage_backends import PrivateMediaStorage



class Profile(models.Model):
    account = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', storage=PrivateMediaStorage())
    qualification = models.CharField(max_length=100)
    research = models.CharField(max_length=100)
    location = CountryField()
    creator = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.account.username} Profile'


class DBPatent(models.Model):
    publicationNumber = models.CharField(max_length=100)
    title = models.CharField(max_length=500)
    publicationDate = models.DateField()
    license = models.CharField(max_length=100, blank=True)
    publicationOwner = models.CharField(max_length=100, blank=True)
    region = models.CharField(max_length=100, blank=True)
    publicationUsage = models.CharField(max_length=100, blank=True)
    publicationType = models.CharField(max_length=100, blank=True)
    stageComplete = models.BooleanField()
    stageSelected = models.BooleanField()
    stageApproved = models.BooleanField()
    category = models.CharField(max_length=100,blank=True)
    type = models.CharField(max_length=100,blank=True)
    treatment = models.CharField(max_length=100,blank=True)
    operation = models.CharField(max_length=100,blank=True)
    creator = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.publicationNumber


class PatentSummary(models.Model):
    patentStatus = [('published', 'Published/Pending'),
                    ('granted', 'Granted'),
                    ('active', 'Active'),
                    ('inactive', 'Inactive'),
                    ]

    rating = [('one', '1'),
              ('two', '2'),
              ('three', '3'),
              ('four', '4'),
              ('five', '5'),
              ]

    techChar = [('therapeutic', 'Therapeutic'),
                ('disease diagnosis tool', 'Disease diagnosis tool'),
                ('disease prognosis tool', 'Disease prognosis tool'),
                ('intervention prediction tool', 'Intervention prediction tool'),
                ('decision support', 'Decision support'),
                (
                'healthcare service optimization tool or platform', 'Healthcare service optimization tool or platform'),
                ('software', 'Software'),
                ('research tool', 'Research tool'),
                ('method of use', 'Method of use'),
                ('composition of matter', 'Composition of matter'),
                ('article of manufacture', 'Article of manufacture'),
                ('machine', 'Machine'),
                ('other', 'Other')
                ]

    techReady = [('Basic science research', '1 - Basic science research'),
                 ('Technology conceptualized', '2 - Technology conceptualized'),
                 ('In vitro proof of concept', '3 - In vitro proof of concept'),
                 ('In vivo proof of concept', '4 - In vivo proof of concept'),
                 ('Pre-clinical research', '5 - Pre-clinical research'),
                 ('Clinical research (Phase I or equivalent)', '6 - Clinical research (Phase I or equivalent)'),
                 ('Clinical research (Phase II or equivalent)', '7 - Clinical research (Phase II or equivalent)'),
                 ('Clinical research (Phase III or equivalent)', '8 - Clinical research (Phase III or equivalent)'),
                 ('Commercially available (optimization stage)', '9 - Commercially available (optimization stage)'),
                 ('other', 'Other'),
                 ]
    lvlImp = [('yes', 'Yes'),
              ('incremental', 'Incremental Improvement'),
              ('unknown', 'N/A'),
              ('other', 'Other'),
              ]

    scientific = [
        ('mechanism of action is clearly defined', 'Mechanism of action is clearly defined'),
        ('mechanism of action is speculative', 'Mechanism of action is speculative'),
        ('too complex', 'The underlying basic science is too complex and unlikely to be elucidated completely'),
        ("the empirical data doesn't make sense theoretically", "The empirical data doesn't make sense theoretically"),
        ("the underlying basic science doesn't matter", "The underlying basic science doesn't matter"),
        ('there is expert consensus on this being a good idea', 'There is expert consensus on this being a good idea'),
        ('other', 'Other'),
    ]

    reproducibility = [
        ('it', 'Inventor is the only source of any insights on the technology'),
        ('rt',
         'Results supporting this technology has been reproduced independently by another researcher/organization'),
        ('st', 'Studies ongoing to assess reproducibility'),
        ('spt',
         'Results not supportive of the technology have been produced independently by another researcher/organization'),
        ('unt', 'Unclear if anyone is working on this specific technology for the application protected by the patent'),
        ('other', 'Other'),
    ]
    choiceOptions = [
        ('yes', 'Yes'),
        ('no', 'No'),
        ('unknown', 'Unknown'),
    ]

    account = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
    startDate = models.DateField(null=True)
    ad1 = models.CharField(max_length=100)
    ad2 = models.PositiveIntegerField(null=True)
    ad3 = models.CharField(max_length=9, choices=patentStatus)
    ad4 = models.CharField(max_length=100)
    ad5 = models.URLField(max_length=300)
    pr1 = models.CharField(max_length=100)
    pr2 = models.CharField(max_length=5, choices=rating, null=False, blank=False, default='')
    pr3 = models.CharField(max_length=100)
    pr4 = models.CharField(max_length=5, choices=rating, null=False, blank=False, default='')
    pr5 = models.CharField(max_length=100)
    pr6 = models.PositiveIntegerField(null=True)
    pr7 = models.PositiveIntegerField(null=True)
    pr8 = models.CharField(max_length=100)
    pr9 = models.CharField(max_length=100)
    tech1 = models.CharField(max_length=48, choices=techChar)
    tech2 = models.CharField(max_length=100)
    tech3 = models.CharField(max_length=100)
    tech4 = models.CharField(max_length=100)
    dev1 = models.CharField(max_length=50, choices=techReady)
    dev2 = models.CharField(max_length=100)
    dev3 = models.CharField(max_length=100)
    comp1 = models.CharField(max_length=8, choices=choiceOptions)
    comp2 = models.CharField(max_length=8, choices=choiceOptions)
    comp3 = models.CharField(max_length=8, choices=choiceOptions)
    comp4 = models.CharField(max_length=100)
    comp5 = models.CharField(max_length=8, choices=choiceOptions)
    comp6 = models.CharField(max_length=12, choices=lvlImp)
    comp7 = models.CharField(max_length=8, choices=choiceOptions)
    val1 = models.CharField(max_length=200, choices=scientific)
    val2 = models.CharField(max_length=200, choices=reproducibility)
    val3 = models.CharField(max_length=100)
    endtime = models.DateField(null=True)
    exp = models.CharField(max_length=5, choices=rating, null=False, blank=False, default='')
    feedback = models.TextField(max_length=500)

