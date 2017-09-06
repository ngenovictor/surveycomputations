from django.shortcuts import render
from .calculations import AreaCalculator


def index(request):
    template = "index.html"
    title = "Home"
    context = {
        "title": title
    }
    return render(request, template, context)


def compute_area(request):
    template = "compute_area.html"
    title = "Area Result"
    point1 = (int(request.GET.get("coordinateX1")), int(request.GET.get("coordinateY1")))
    point2 = (int(request.GET.get("coordinateX2")), int(request.GET.get("coordinateY2")))
    point3 = (int(request.GET.get("coordinateX3")), int(request.GET.get("coordinateY3")))
    precision = int(request.GET.get("precision"))
    coordinates = [point1, point2, point3]
    area = AreaCalculator().area_with_coordinates(coordinates, precision)
    context = {
        "title": title,
        "area": area,
        "coordinates": coordinates
    }
    return render(request, template, context)