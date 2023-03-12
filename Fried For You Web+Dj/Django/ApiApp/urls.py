from django.db import router
from  django.urls import path,include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
#router路由器(總機)

router.register(r'product',views.ProductViewSet)
#配對path與view(分機),http://127.0.0.1:8000/product

urlpatterns = [path('',include(router.urls)),
               path('api/',include(router.urls)),
               ]
#設定總機路由2組
#http://127.0.0.1:8000/
#http://127.0.0.1:8000/api/
