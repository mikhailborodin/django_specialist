from django.db import models
from django.urls import reverse_lazy


class Question(models.Model):
    TYPES = (
        ('apple', 'apple'),
        ('orange', 'orange'),
        ('pineapple', 'pineapple'),
        ('banan', 'banan'),
        ('melon', 'melon'),
    )
    question_text = models.CharField(max_length=200, verbose_name='Текст')
    pub_date = models.DateTimeField(verbose_name='Дата')
    type = models.CharField(max_length=50, choices=TYPES, verbose_name='Тип')
    published = models.BooleanField(default=False, verbose_name='Опубликован?')

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def get_text(self):
        return self.question_text

    def get_absolute_url(self):
        return reverse_lazy('question_detail', kwargs={'pk': self.id})

    def __str__(self):
        return '%s %s' % (self.id, self.type)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def get_text(self):
        return self.choice_text
