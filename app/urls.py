from django.urls import path, include
from . import views
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
     path('', views.IndexView, name="index"),
     path("submittd/",views.insertData,name="insert"),
    #  path("in/",views.Ins,name="insert")
    #  path('show_file', views.showfile, name="show_file"),
    #  path('form',views.formview,name="form")

]