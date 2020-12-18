from django.urls import path
from . views import *


urlpatterns = [
    path('', HomePage.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('upload/details/', UploadDetails.as_view(), name='upload_details'),
]
