from django.shortcuts import render
from coloring.models import *
from django.http import HttpResponse
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
import json

def get_author_by_name(authorname): 
  author = None
  
  # check if an Author with name 'authorname' already exists
  if Author.objects.filter(name = authorname).exists():
    # if so, fetch that object from the database
    author = Author.objects.get(name=authorname)
    
  else: 
    # otherwise, create a new Author with the name authorname
    author = Author(name = authorname)
    # save the created object
    author.save()

  return author

def get_drawing_by_author_and_title(author_obj, drawing_title, points): 
  drawing = None
  # check if an Author with name 'authorname' already exists
  if Drawing.objects.filter(author = author_obj, title = drawing_title).exists():
    # if so, fetch that object from the database
    drawing = Drawing.objects.get(title=drawing_title, author=author_obj)
    
  else: 
    # otherwise, create a new Drawing with the name authorname
    drawing = Drawing(title = drawing_title, author=author_obj)
    
    # save the created object
  drawing.save() 
  for point in points:
      coord = Coord(x=point[0], y=point[1])
      if not (coord in drawing.drawing_points.all()):
        coord.save()
        drawing.drawing_points.add(coord)
        drawing.save   
  return drawing
  
@csrf_exempt
def index(request, authorname="DefaultAuthor", titlename="DefaultTitle"):

  print("The authorname is:", authorname)
  author = get_author_by_name(authorname)
  drawing = None
  if request.POST: 
    # POST request received
    
    # demonstrating printing out the POST request & data
    print("Received POST request with data:")
    data = json.loads(request.body.decode('UTF-8'))
    drawing = get_drawing_by_author_and_title(author, data.get("title"), data.get("points"))
    # find out if a Drawing with the Author and Title already exists?
    # if it doesn't exist, you may create a new Drawing object
    # if it does exist, you may update an existing Drawing object
    # make sure to save your object after creating or updating 
    # for more information, see get_author_by_name() and reference below
    # https://docs.djangoproject.com/en/4.0/ref/models/instances/#saving-objects
    
    return HttpResponse(True)

  else: 
    # GET request received

    # if a drawing by the author already exists,
    # send the drawing conent and title with the data below
    all_coords = []
    if Drawing.objects.filter(author = author, title=titlename).exists():
      drawing = Drawing.objects.filter(author = author, title=titlename)
      coord_set = drawing[len(drawing)-1].drawing_points.all()
      for coord in coord_set:
        xy = [coord.x, coord.y]
        all_coords.append(xy)
      data = {
        "author": author,
        "drawing": drawing[len(drawing)-1],
        "all_coords": all_coords
      }
    elif Drawing.objects.filter(author = author).exists():
      drawing = Drawing.objects.filter(author = author)
      coord_set = drawing[len(drawing)-1].drawing_points.all()
      for coord in coord_set:
        xy = [coord.x, coord.y]
        all_coords.append(xy)
      data = {
        "author": author,
        "drawing": drawing[len(drawing)-1],
        "all_coords": all_coords
      }
    else:
      data = {
        "author": author,
        "all_coords": all_coords
      }
    
    return render(request, 'coloring/index.html', data)