from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def dark_matter(request):
    return render(request, "domain/dark_matter.html")


def planet_death(request):
    return render(request, "domain/planet_death.html")


def quantum_mechanics(request):
    return render(request, "domain/quantum_mechanics.html")

