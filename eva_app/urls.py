from django.urls import path

from eva_app import views

urlpatterns = [
    path('',views.front_page,name='front_page'),
    path('login_view',views.login_view,name='login_view'),
    path('cus_reg',views.customer_reg,name='cus_reg'),
    path('pub_reg',views.publisher_reg,name='pub_reg'),
    path('blog_create',views.blog_create,name='blog_create')
]
