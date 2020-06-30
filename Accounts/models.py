from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    account = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    qualification = models.CharField(max_length=100)
    research = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
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

    # account = models.M=ForeignKey(User, on_delete=models.CASCADE)
    startDate = models.DateTimeField()
    # Administrative information
    # Technology Title = string of word
    ad1 = models.CharField(max_length=100)
    # year patent = Year date
    ad2 = models.PositiveIntegerField()
    # patent status = small list of options, string word
    ad3 = models.CharField(max_length=9, choices=patentStatus)
    # institution = drop-down list of options
    ad4 = models.CharField(max_length=100)
    # patent link = url link
    ad5 = models.URLField(max_length=300)
    # Product market fit speculation
    # problem = String of words
    pr1 = models.CharField(max_length=100)
    # problem difficulty = number lvl
    pr2 = models.CharField(max_length=5, choices=rating)
    # solution = string of words
    pr3 = models.CharField(max_length=100)
    # solution difficulty = number lvl
    pr4 = models.CharField(max_length=5, choices=rating)
    # assists = string of words
    pr5 = models.CharField(max_length=100)
    # peopleAssistsPresent = number
    pr6 = models.PositiveIntegerField()
    # peopleAssistsNextYear = number
    pr7 = models.PositiveIntegerField()
    # indirectWinners = string of words
    pr8 = models.CharField(max_length=100)
    # valueAdded = string of words
    pr9 = models.CharField(max_length=100)
    # characterizing the technology
    # techChar = small list of options, string word
    tech1 = models.CharField(max_length=48, choices=techChar)
    # techFeature = string words
    tech2 = models.CharField(max_length=100)
    # workScientific = string words
    tech3 = models.CharField(max_length=100)
    # workNonScientific = string words
    tech4 = models.CharField(max_length=100)
    # stage of development
    # technologyReadiness = small list of options, string word
    dev1 = models.CharField(max_length=50, choices=techReady)
    # readinessJustify = string of words
    dev2 = models.CharField(max_length=100)
    # forwardNext = string of words
    dev3 = models.CharField(max_length=100)
    # Competitive landscape
    # commercialAvailable = small list of options, string word
    comp1 = models.CharField(max_length=8, choices=choiceOptions)
    # patentSolve = small list of options, string word
    comp2 = models.CharField(max_length=8, choices=choiceOptions)
    # patentOverlap = small list of options, string word
    comp3 = models.CharField(max_length=8, choices=choiceOptions)
    # patentAffect = string of words
    comp4 = models.CharField(max_length=100)
    # currentSol = small list of options, string word
    comp5 = models.CharField(max_length=8, choices=choiceOptions)
    # levelImprovement = small list of options, string word
    comp6 = models.CharField(max_length=12, choices=lvlImp)
    # costSaving = small list of options, string word
    comp7 = models.CharField(max_length=8, choices=choiceOptions)
    # Validation
    # scientific = small list of options, string word
    val1 = models.CharField(max_length=200, choices=scientific)
    # reproducibility = small list of options, string word
    val2 = models.CharField(max_length=200, choices=reproducibility)
    # references = string of words
    val3 = models.CharField(max_length=100)
    # Post Survey
    # endTime = date time
    endtime = models.DateTimeField()
    # experience = number lvl
    exp = models.CharField(max_length=5, choices=rating)
    # feedback = string of words
    feedback = models.TextField(max_length=300)

