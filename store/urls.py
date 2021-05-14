from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path('product_crud', views.product_crud, name='product_curd'),
    path(r'update_product/(?P<id>.+)', views.product_crud, name='update_product'),
    path(r'delete_product/(?P<id>.+)', views.delete_product, name='delete_product'),
    path('<slug:slug>/', views.product_detail, name='product_detail'),
    path('shop/<slug:category_slug>/', views.category_list, name='category_list'),
    path('', views.product_all, name='product_all'),
]