from django.shortcuts import render
import requests


def index(request):
    data = get_data_from_jisho('日本語')  # Remplacez '日本語' par le mot que vous voulez rechercher
    return render(request, 'index.html', {'data': data})


def get_data_from_jisho(keyword):
    response = requests.get(f'https://jisho.org/api/v1/search/words?keyword={keyword}')
    if response.status_code == 200:
        return response.json()
    else:
        return None



