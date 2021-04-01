from django.shortcuts import render

# Create your views here.
def index(request):
  home_dict = {'home_page': "Home Page"}
  return render(request, 'tip_data/index.html', context=home_dict)

def api(request):
  api_dict = {'api_page': "API Data"}
  return render(request, 'tip_data/api.html', context=api_dict)