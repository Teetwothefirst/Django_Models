from django.shortcuts import render

# Create your views here.
def home_view(request):
    my_name = "Adetomiwa"
    return render(
    request,
    "home.html",
    {"my_name": my_name}
   )