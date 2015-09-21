from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Root(models.Model) :
    word = models.CharField(max_length = 20)
    meaning = models.CharField(max_length = 100)
    comment = models.CharField(max_length = 150, blank = True, null = True)

    def __str__(self):
        return self.word + ' = ' + self.meaning


@python_2_unicode_compatible
class Word(models.Model) :
    word = models.CharField(max_length = 20)
    meaning = models.CharField(max_length = 100)
    comment = models.CharField(max_length = 150, blank = True, null = True)

    def __str__(self):
        return self.word + ' = ' + self.meaning


@python_2_unicode_compatible
class WordRoot(models.Model):
    word_id = models.ForeignKey(Word)
    root_id = models.ForeignKey(Root)

    def __str__(self):
        return self.word_id.word + ' <-- ' + self.root_id.word


@python_2_unicode_compatible
class Noun(models.Model) :
    word_id = models.ForeignKey(Word)
    noun = models.CharField(max_length = 20)

    def __str__(self):
        return self.word_id.word + ' <==> ' + self.noun


@python_2_unicode_compatible
class Adjective(models.Model) :
    word_id = models.ForeignKey(Word)
    adjective = models.CharField(max_length = 20)

    def __str__(self):
        return self.word_id.word + ' <==> ' + self.adjective