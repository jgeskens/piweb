from django.db import models

class Box(models.Model):
    number = models.PositiveIntegerField()
    name = models.CharField(max_length=128, blank=True, db_index=True)

    class Meta:
        verbose_name = u'box'
        verbose_name_plural = u'boxes'
        ordering = ('number',)

    def __unicode__(self):
        return u'%d. %s' % (self.number, self.name)


class Category(models.Model):
    name = models.CharField(max_length=128, db_index=True)

    class Meta:
        verbose_name = u'category'
        verbose_name_plural = u'categories'
        ordering = ('name',)

    def __unicode__(self):
        return self.name


def last_plus_one():
    from boekjes.models import Book
    try:
        return Book.objects.latest('number').number + 1
    except:
        return 1


class Book(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    author = models.CharField(max_length=128, blank=True, db_index=True)
    box = models.ForeignKey(Box, blank=True, null=True)
    hardcover = models.BooleanField(blank=True, default=True)
    category = models.ForeignKey(Category, blank=True, null=True)

    class Meta:
        ordering = ('pk',)

    def __unicode__(self):
        return u'%d. %s' % (self.pk, self.title)



