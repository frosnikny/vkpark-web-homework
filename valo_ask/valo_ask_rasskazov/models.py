from django.db import models
from django.contrib.auth import models as user_models


class Question(models.Model):
    title = models.CharField(max_length=127, unique=True)
    text = models.CharField(max_length=255, default='question text')
    creator = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    tag = models.ManyToManyField('Tag')

    def __str__(self):
        return f'Question "{self.title}"'


class Answer(models.Model):
    text = models.CharField(max_length=255, default='answer text')
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    creator = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)


class Ratings(models.Model):
    user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    is_question = models.BooleanField(default=True)
    question = models.ForeignKey('Question', on_delete=models.CASCADE, null=True)
    answer = models.ForeignKey('Answer', on_delete=models.CASCADE, null=True)
    is_good = models.BooleanField(default=True)


class Tag(models.Model):
    name = models.CharField(max_length=31, unique=True)
    color = models.CharField(max_length=31)

    def __str__(self):
        return f'Tag "{self.name}"'


class User(models.Model):
    profile = models.OneToOneField(user_models.User, on_delete=models.PROTECT)
    nickname = models.CharField(max_length=31, unique=True)
    avatar = models.ImageField(null=True)

    def __str__(self):
        return f'User "{self.profile.email}"'


ANSWERS = [
    {
        'text': f'Text {i}',
    } for i in range(2)
]

TAGS_2 = ['cypher', 'game']

TAGS_5 = [f'tag {i}' for i in range(5)]

TOP = [2, 3, 5, 6, 7, 8]

QUESTIONS = [
    {
        'id': i,
        'title': f'Question {i}',
        'text': f'Text {i}',
        'answers': ANSWERS[:],
        'tags': TAGS_2[:],
    } for i in range(12)
]
