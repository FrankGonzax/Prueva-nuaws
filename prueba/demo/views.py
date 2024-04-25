from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def get_api_data(request):
   return JsonResponse({'name': 'Francito mas nahhh...'})