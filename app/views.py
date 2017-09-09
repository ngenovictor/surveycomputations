from django.shortcuts import render
from .calculations import AreaCalculator
from django.http import JsonResponse



def index(request):
    template = "index.html"
    title = "Home"
    context = {
        "title": title
    }
    return render(request, template, context)


def about(request):
    template = "about.html"
    title = "About"
    context = {
        "title": title
    }
    return render(request, template, context)


def give_feedback(request):
    message = {"message": "true"}
    return JsonResponse(message)


def compute_area(request):
    template = "compute_area.html"
    title = "Area Result"
    number_of_points = int(request.GET.get("point_number"))
    coordinates = []
    for i in range(number_of_points):
        x_string = "coordinateX" + str(i+1)
        y_string = "coordinateY" + str(i+1)

        point = (int(request.GET.get(x_string)), int(request.GET.get(y_string)))
        coordinates.append(point)

    precision = int(request.GET.get("precision"))

    area = AreaCalculator().area_with_coordinates(coordinates, precision)
    context = {
        "title": title,
        "area": area,
        "coordinates": coordinates
    }
    return render(request, template, context)