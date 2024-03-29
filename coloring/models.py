from django.db import models

# The Author model has been created for you
class Author(models.Model):
  name = models.CharField(max_length=50)

# Create the Coordinate model
class Coord(models.Model):
  x = models.IntegerField()
  y = models.IntegerField()
  
# Create the Drawing model
class Drawing(models.Model):
  title = models.CharField(max_length=150)
  author = models.ForeignKey(Author, on_delete=models.CASCADE)
  drawing_points = models.ManyToManyField(Coord)
