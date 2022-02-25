from django.shortcuts import render
from .calculations import AreaCalculator
from django.http import JsonResponse
from django.http import *
import requests

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
    name = request.GET.get("name")
    email = request.GET.get("email")
    message = request.GET.get("message")

    if not name or not email or not message:
        response_message = {"message": "something missing"}
        return JsonResponse(response_message)
    else:
        data = {
            "name": name,
            "email": email,
            "message": message
        }
        requests.get("https://victormailapp.herokuapp.com/surveytools_feedback", data)

        response_message = {"message": "Thank You for Your feedback"}
        return JsonResponse(response_message)


def compute_area(request):
    template = "compute_area.html"
    title = "Area Result"
    area = None
    coordinates = None
    if request.method == 'POST':
        number_of_points = int(request.POST.get("point_number"))
        coordinates = []
        for i in range(number_of_points):
            x_string = "coordinateX" + str(i+1)
            y_string = "coordinateY" + str(i+1)

            point = (int(request.POST.get(x_string)), int(request.POST.get(y_string)))
            coordinates.append(point)

        precision = int(request.POST.get("precision"))

        area = AreaCalculator().area_with_coordinates(coordinates, precision)
    context = {
        "title": title,
        "area": area,
        "coordinates": coordinates
    }
    return render(request, template, context)
