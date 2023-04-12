from django.contrib import admin

from . import models
# from valo_ask_rasskazov/models import Question, Answer, Ratings, Tag, User

admin.site.register(models.Question)
admin.site.register(models.Answer)
admin.site.register(models.Ratings)
admin.site.register(models.Tag)
admin.site.register(models.User)
