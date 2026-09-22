from rest_framework.routers import DefaultRouter
from django.urls import path,include
from . import views

router=DefaultRouter()

router.register('list',views.DoctorViewSet,basename='doctor')
router.register('specialization',views.SpecializationViewSet,basename='specialization')
router.register('available_time',views.AvailableTimeViewSet,basename='available_time')
router.register('designation',views.DesignationViewSet,basename='designation')


urlpatterns = [
    path('',include(router.urls)),
]