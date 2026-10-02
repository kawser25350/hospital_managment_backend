from rest_framework.routers import DefaultRouter
from django.urls import path,include
from . import views

router=DefaultRouter()

router.register('list',views.PatientViewset,basename='Patient')


urlpatterns = [
    path('',include(router.urls)),
    path('register/',views.RegistratoinApiView.as_view(),name='register'),
    path('active/<uid64>/<token>/',views.active_account,name='activate'),
    path('login/',views.LoginApiView.as_view(),name='login'),
    path('logout/',views.LogoutApiView.as_view(),name='logout')
]