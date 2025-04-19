from django.shortcuts import render, redirect, get_object_or_404
from .models import SalesData
from .forms import SalesDataForm
import joblib
import pandas as pd

model = joblib.load('xgb_model.pkl')

def index(request):
    return render(request, 'sales/index.html')

def salesdata_list(request):
    data = SalesData.objects.all()
    return render(request, 'sales/salesdata_list.html', {'data': data})

def salesdata_add(request):
    if request.method == 'POST':
        form = SalesDataForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            input_data = pd.DataFrame([{
                'Item_Weight': obj.Item_Weight,
                'Item_Visibility': obj.Item_Visibility,
                'Item_MRP': obj.Item_MRP,
                'Outlet_Establishment_Year': obj.Outlet_Establishment_Year
            }])
            prediction = model.predict(input_data)[0]
            obj.Item_Outlet_Sales = prediction
            obj.save()
            return redirect('salesdata_list')
    else:
        form = SalesDataForm()
    return render(request, 'sales/salesdata_form.html', {'form': form})

def salesdata_edit(request, pk):
    data = get_object_or_404(SalesData, pk=pk)
    if request.method == 'POST':
        form = SalesDataForm(request.POST, instance=data)
        if form.is_valid():
            obj = form.save(commit=False)
            input_data = pd.DataFrame([{
                'Item_Weight': obj.Item_Weight,
                'Item_Visibility': obj.Item_Visibility,
                'Item_MRP': obj.Item_MRP,
                'Outlet_Establishment_Year': obj.Outlet_Establishment_Year
            }])
            prediction = model.predict(input_data)[0]
            obj.Item_Outlet_Sales = prediction
            obj.save()
            return redirect('salesdata_list')
    else:
        form = SalesDataForm(instance=data)
    return render(request, 'sales/salesdata_form.html', {'form': form})

def salesdata_delete(request, pk):
    data = get_object_or_404(SalesData, pk=pk)
    if request.method == 'POST':
        data.delete()
        return redirect('salesdata_list')
    return render(request, 'sales/salesdata_confirm_delete.html', {'data': data})

from django.shortcuts import render
from .models import TrainData

def index(request):
    return render(request, 'sales/index.html')

def train_data_list(request):
    data = TrainData.objects.all()
    return render(request, 'sales/train_data_list.html', {'data': data})



#def index(request):
 #   return render(request, 'sales/index.html')

#E:\bigmart11\sales\templates\sales\index.html


from django.shortcuts import render
from .utils import get_latest_headlines  # if moved to a separate utils.py
'''
def index(request):
    headlines = get_latest_headlines()
    return render(request, 'sales\index.html', {'headlines': headlines})
'''
# sales/views.py
from django.shortcuts import render
from .scraper import scrape_latest_sales_news  # Import the function

def index(request):
    headlines = scrape_latest_sales_news()  # Call the function to get headlines
    return render(request, 'sales/index.html', {'headlines': headlines})
