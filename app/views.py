from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from . models import *
import pandas as pd

# Create your views here.
def index(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['file']
        UploadedFile.objects.create(file=uploaded_file)
        return redirect('/')
    file = UploadedFile.objects.all()
    print(file)
    context = {
        'data':file
    }
    return render(request,"index.html", context)

def view_data(request):
    file = UploadedFile.objects.all()
    print(file)
    context = {
        'data':file
    }
    return render(request, "admin.html",context)

def view_file(request, file_id):
    uploaded_file = get_object_or_404(UploadedFile, id=file_id)
    file_path = uploaded_file.file.path
    if file_path.endswith('.csv'):
        df = pd.read_csv(file_path)
    elif file_path.endswith('.xlsx'):
        df = pd.read_excel(file_path)
    else:
        return HttpResponse('Invalid file format')
    return render(request, 'view_data.html', {'file_name': uploaded_file.file.name, 'table_data': df.to_html()})


def download_file(request, file_id):
    uploaded_file = get_object_or_404(UploadedFile, id=file_id)
    response = HttpResponse(
        uploaded_file.file, content_type='application/octet-stream')
    response['Content-Disposition'] = f'attachment; filename="{uploaded_file.file.name}"'
    return response

