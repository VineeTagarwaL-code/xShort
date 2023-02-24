from django.shortcuts import render
from .forms import take_userinput
from .models import input_taker
import requests
def url_creator(url_name , link_name ):
     error=''
     
     API_KEY =  '21f5aa572eff4bae4dc5b59d652c73d1666a4'
     BASE_URL = 'https://cutt.ly/api/api.php'
     payload = {
           'key':API_KEY,
           'short' : url_name,
           'name' : link_name
           
             }
     
     try:
            request = requests.get(BASE_URL , params=payload)
     
            data = request.json()
              
            short_link  = data['url']['shortLink']
              
            return short_link
              
     except:
             
                 error="enter a different name for your url"
                 return error   
             
# Create your views here.
def main_view(request):
  short_link=''
  if (request.method == 'POST'):
        form = take_userinput(request.POST)
        if(form.is_valid()):
              url_link = form.cleaned_data['user_link']
              url_namelink = form.cleaned_data['user_linkname']
              objectholder = input_taker.objects.create(user_link = url_link , user_linkname =  url_namelink)
              objectid = objectholder.id
              objectvalues = input_taker.objects.get(id=objectid)
              get_link = objectvalues._meta.fields[1].name
              get_name  = objectvalues._meta.fields[2].name
              fetched_link = getattr(objectvalues , get_link)
              fetched_name = getattr(objectvalues , get_name)
              short_link = url_creator(fetched_link,fetched_name)
              print(short_link)
  form=take_userinput()
  context = {
        "f" :form,
        "link" : short_link
  }
  return render(request , 'main.html' , context)
 

  