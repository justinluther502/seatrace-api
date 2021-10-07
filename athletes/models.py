from django.db import models


class Rower(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    height_ft = models.PositiveSmallIntegerField()
    height_in = models.PositiveSmallIntegerField()
    mmr = models.PositiveSmallIntegerField()
    stroke_mmr = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ['last_name']

    def __str__(self):
        return self.last_name + ", " + self.first_name


class Hull(models.Model):
    HULL_MAKES = (
        ('Empacher', 'Empacher'),
        ('Millenium', 'Millenium'),
        ('Resolute', 'Resolute'),
    )
    SIZES = (
        ('Single', 'Single'),
        ('Double', 'Double'),
        ('Pair', 'Pair'),
        ('Coxed Four', 'Coxed Four'),
        ('Straight Four', 'Straight Four'),
        ('Quad', 'Quad'),
        ('Eight', 'Eight')
    )
    make = models.CharField(choices=HULL_MAKES, max_length=30)
    size = models.CharField(choices=SIZES, max_length=20)
    year = models.SmallIntegerField()

    class Meta:
        ordering = ['year']

    def __str__(self):
        return self.make + "_" + str(self.year)


class Boat(models.Model):
    date = models.DateField()
    hull = models.ForeignKey(Hull, on_delete=models.CASCADE)
    crewmembers = models.ManyToManyField(Rower)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return self.hull.__str__() + " raced on " + str(
            self.date) + " Race ID: " + str(self.id)
