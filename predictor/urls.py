from django.urls import path
from . import views
from django.shortcuts import render

urlpatterns = [
    path('predict_from_frame/', views.predict_from_frame, name='predict_from_frame'),
    path('camera_predict/', lambda request: render(request, 'predictor/camera_predict.html')),
]