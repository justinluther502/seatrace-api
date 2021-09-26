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
        ('EMPCH', 'Empacher'),
        ('MILL', 'Millenium'),
        ('RESOL', 'Resolute'),
    )
    SIZES = (
        ('S', 'Single'),
        ('D', 'Double'),
        ('P', 'Pair'),
        ('CF', 'Coxed Four'),
        ('SF', 'Straight Four'),
        ('Q', 'Quad'),
        ('E', 'Eight')
    )
    make = models.CharField(choices=HULL_MAKES, max_length=30)
    size = models.CharField(choices=SIZES, max_length=20)
    year = models.DateTimeField()

    class Meta:
        ordering = ['year']

    def __str__(self):
        return self.make + "_" + str(self.year.year)


class Boat(models.Model):
    date = models.DateTimeField()
    hull = models.ForeignKey(Hull, on_delete=models.CASCADE)
    crewmember = models.ManyToManyField(Rower)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return self.hull.__str__() + " raced at " + str(self.date)
