from django.shortcuts import render

def home(request):
    return render(request,'home.html',{})

def login(request):
    return render(request,'login.html',{})
def aqi(request):
    import json
    import requests
    if request.method == 'POST':
        query = request.POST['query']
        api_url='https://api.api-ninjas.com/v1/airquality?city='
        api_request= requests.get(api_url + query, headers = {'X-Api-Key':'Jbl5w1oQwNcNNKOnzZ2p/Q==AxfZUC8NCfTqgni2'})
        try:
            api = json.loads(api_request.content)
            print(api_request.content)
        except Exception as e:
            api = "oops! There was an error"
            print(e)
        return render(request, 'aqi.html',{'api':api})
    else:
        return render(request, 'aqi.html',{'query':'Enter a valid query'})
def nutri(request):
    import json
    import requests
    if request.method == 'POST':
        query = request.POST['query']
        api_url='https://api.api-ninjas.com/v1/nutrition?query='
        api_request= requests.get(api_url + query, headers = {'X-Api-Key':'Jbl5w1oQwNcNNKOnzZ2p/Q==AxfZUC8NCfTqgni2'})
        try:
            api = json.loads(api_request.content)
            print(api_request.content)
        except Exception as e:
            api = "oops! There was an error"
            print(e)
        return render(request, 'nutri.html',{'api':api})
    else:
        return render(request, 'nutri.html',{'query':'Enter a valid query'})
