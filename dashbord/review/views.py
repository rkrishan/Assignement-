from django.shortcuts import render
import pandas as pd
# Create your views here.



def index(request):
    # df = pd.read_csv("data/car_sales.csv")
    return render(request, 'index.html')