from django.urls import path, include

from gallery import views

urlpatterns = [
    path('latests-images/', views.LatestImageList.as_view()),
    path('images/<slug:category_slug>/<slug:image_slug>/', views.ImageDetail.as_view()),
    path('add-image/', views.upload_photo)
]