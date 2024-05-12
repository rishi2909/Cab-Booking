from django.urls import path
from . import views
urlpatterns=[
    path('test',views.test),
#path for home page
    path('home',views.home),

#path for signup page
     path('signup',views.signup), 

#path for signupform table
     path('signupform',views.signupform),

#path for login page
     path('login',views.login),   

#path for logcode
     path('logcode',views.logcode),       

#path for available page
     path('available',views.available),

#path for availablecab table
     path('cab',views.cab), 

#path for show Cab
     path('showcab',views.showcab),

     path('booking',views.booking),     

     path('book',views.book),        
]