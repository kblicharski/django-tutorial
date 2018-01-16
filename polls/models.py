# Django models are basically normal Python classes that wrap the underlying
# database schema. Instead of defining a column as a VARCHAR, we call it a
# CharField. Django models serve as the canonical and sole source of truth about
# our data -- all fields and behavior.
#
# With this information, Django creates the database schema for our app and
# creates a Python API to access the objects. Instead of constructing queries,
# we can use the ORM syntax provided by Django.
import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    # Some fields, like CharField, have a required argument; `max_length`.
    # We generally use CharFields instead of TextFields in Django. They can be
    # more performant, since CharFields have a predefined length while
    # TextFields do not.
    question_text = models.CharField(max_length=200)
    # The first positional argument is also the `verbose_name` kwarg. If it's
    # not provided, Django will construct it from our field name, replacing
    # underscores with spaces.
    pub_date = models.DateTimeField('date published')

    # __str__ methods are important, because this is how objects will be
    # displayed in the Django shell and also on the generated admin site.
    def __str__(self):
        return self.question_text

    # We can add normal Python methods to models, too.
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    # Each Choice is related to a single Question, but a Question can have
    # many Choices. When we delete a Question, we should also delete all of its
    # associated questions -- this is denoted by the `on_delete` kwarg.
    # All ForeignKey fields must define the field to which the class is related
    # and the `on_delete` kwarg.
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    # Fields have a lot of optional kwargs, such as `default`.
    votes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.choice_text
