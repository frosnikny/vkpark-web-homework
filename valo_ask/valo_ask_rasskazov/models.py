from django.db import models
from django.contrib.auth import models as user_models


class QuestionManager(models.Manager):
    def update_all(self):
        for i in super().get_queryset().all():
            i.update_average_rating()

    def with_rating_order(self):
        self.update_all()
        return super().get_queryset().order_by('-summary_rating')

    def with_tag(self, tag):
        # questions = self.filter()
        return self.get_queryset().filter(tag__name=tag)

    def with_new(self):
        return super().get_queryset().order_by('-id')

    def get_queryset(self):
        return super().get_queryset()


class UserManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()


class RatingsManager(models.Manager):
    def test(self, q):
        return super().get_queryset().filter(question=q)

    def get_queryset(self):
        return super().get_queryset()


class Ratings(models.Model):
    user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    is_question = models.BooleanField(default=True)
    question = models.ForeignKey('Question', on_delete=models.CASCADE, null=True)
    answer = models.ForeignKey('Answer', on_delete=models.CASCADE, null=True)
    is_good = models.BooleanField(default=True)

    objects = RatingsManager()


class Question(models.Model):
    title = models.CharField(max_length=127, unique=True)
    text = models.CharField(max_length=255, default='question text')
    creator = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    tag = models.ManyToManyField('Tag')
    summary_rating = models.IntegerField(null=True, blank=True)

    objects = QuestionManager()

    def update_average_rating(self):
        sum_rating = len(
            Ratings.objects.test(self).filter(is_good=True).all()) - len(
            Ratings.objects.test(self).filter(is_good=False).all())
        # print()
        self.summary_rating = sum_rating
        self.save()

    def __str__(self):
        return f'Question "{self.title}"'


class Answer(models.Model):
    text = models.CharField(max_length=255, default='answer text')
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    creator = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)


class Tag(models.Model):
    name = models.CharField(max_length=31, unique=True)
    color = models.CharField(max_length=31)

    def __str__(self):
        return f'Tag "{self.name}"'


class User(models.Model):
    profile = models.OneToOneField(user_models.User, on_delete=models.PROTECT)
    nickname = models.CharField(max_length=31, unique=True)
    avatar = models.ImageField(null=True)

    objects = UserManager()

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
