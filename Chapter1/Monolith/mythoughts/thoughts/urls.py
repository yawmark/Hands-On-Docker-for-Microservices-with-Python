from django.urls import path
from . import login, thoughts

urlpatterns = [
    path('', thoughts.list_thoughts, name='index'),
    path('login/', login.login, name='login'),
    path('logout/', login.logout, name='logout'),
    path('thoughts/', thoughts.list_thoughts, name='list-thoughts'),
    path('thoughts/new', thoughts.new_thought, name='new-thought'),
]
