from django.urls import path
from django.views.generic.detail import DetailView

from .views import *
from .models import Photo

app_name = 'photo'

urlpatterns = [
    path('', photo_list, name='photo_list'),  # 함수형 뷰 이름만 지정
    path('detail/<int:pk>/',  # 상세보기 뷰는 urls.py에서 인라인 코드로 작성
         DetailView.as_view(
             model=Photo, template_name='photo/detail.html'),
         name='photo_detail'),
    path('upload/', PhotoUploadView.as_view(), name='photo_upload'),
    path('delete/<int:pk>/', PhotoDeleteView.as_view(), name='photo_delete'),
    path('update/<int:pk>/', PhotoUpdateView.as_view(), name='photo_update'),
]
