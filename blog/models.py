from django.db import models
from django.core.validators import MaxValueValidator
from django.utils.text import slugify
from django_quill.fields import QuillField
from user.models import Profile
import uuid

# Create your models here.


class Essay(models.Model):
    '''This class is for create essay .'''

    # primary key | time created
    id = models.UUIDField(default=uuid.uuid4, editable=False,
                          unique=True, primary_key=True)
    created = models.DateTimeField(auto_now=True, editable=False)

    # information
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=250, unique=True)
    description = QuillField()
    upload_image = models.ImageField(default='surface.jpg')
    source_link = models.CharField(max_length=2000, blank=True, null=True)
    demo_link = models.CharField(max_length=2000, blank=True, null=True)
    total_vote = models.IntegerField(default=0)
    positive_vote = models.IntegerField(
        default=0, validators=[MaxValueValidator(100)])

    # relation
    tag = models.ManyToManyField('Tag', related_name='+')

    # slug url
    slug = models.SlugField(max_length=255, unique=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    # return the title of the class
    def __str__(self):
        return self.title

    # Meta class for change and development
    class Meta:
        ordering = ['-created']


class Comment(models.Model):
    '''This class is for commenting below the essay .'''

    # primary key | time created
    id = models.UUIDField(default=uuid.uuid4, editable=False,
                          unique=True, primary_key=True)
    created = models.DateField(auto_now=True, editable=False)

    # selection of type vote
    VOTE = [
        ('I read essay', 'I read this essay and realized many concepts .'),
        ('I have not finished this essay',
         'I have not been able to read this article to the end and understand its concepts .'),
        ('I not read essay', 'I am not interested in reading this article .')
    ]

    # relation
    essay = models.OneToOneField('Essay', on_delete=models.CASCADE)

    # user comment
    comment = models.CharField(
        choices=VOTE, default='I read essay', max_length=255)

    # return the commit of the class
    def __str__(self):
        return self.comment

    # Meta class for change and development
    class Meta:
        ordering = ['-created']


class Tag(models.Model):
    '''This class is for marking Essay .'''

    # primary key | time created
    id = models.UUIDField(default=uuid.uuid4, editable=False,
                          unique=True, primary_key=True)
    created = models.DateField(auto_now=True, editable=False)

    # title label
    label = models.CharField(max_length=255, unique=True)

    # return the label of the class
    def __str__(self):
        return self.label

    # Meta class for change and development
    class Meta:
        ordering = ['-created']
