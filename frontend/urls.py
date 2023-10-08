from django.contrib import admin
from django.urls import path,include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'frontend'

urlpatterns = [
    path('', index, name='index'),
    path('detail/<int:id>/', TrekDetail, name='detail'),
    #banner
    path('banners/', BannerImages, name='banner'),
    path('add-banner/', AddBannerImages, name='add_banner'),
    path('view-banner/<int:id>/', ViewBanners, name='view_banner'),
    path('edit-banner/<int:id>/', EditBanner, name='edit_banner'),
    path('delete-banner/<int:id>/', DeleteBanner, name='delete_banner'),
    path('activate-deactive-banner/<int:id>/', ActivatDeactivateBanner, name='activate_deactivate_banner'),
    #State
    path('state-list/',StateList, name='state_list'),
    path('state-detail/<int:id>/',StateDetail, name='state_detail'),
    path('add-state/', AddState, name='add_state'),
    path('view-state/<int:id>/', ViewState, name='view_state'),
    path('edit-state/<int:id>/', EditState, name='edit_state'),
    path('delete-state/<int:id>/', DeleteState, name='delete_state'),
    path('activate-deactivate-state/<int:id>/', ActivatDeactivateState, name='activate_deactivate_state'),

    #district
    path('district-list/',DistrictList, name='district_list'),
    path('district-detail/<int:id>/',DistrictDetail, name='district_detail'),
    path('add-district/', AddDistrict, name='add_district'),
    path('view-district/<int:id>/', ViewDistrict, name='view_district'),
    path('edit-district/<int:id>/', EditDistrict, name='edit_district'),
    path('delete-district/<int:id>/', DeleteDistrict, name='delete_district'),
    #Tresks
    path('trek-list/',TrekList, name='trek_list'),
    path('add-trek/', AddTrek, name='add_trek'),
    path('view-trek/<int:id>/', ViewTrek, name='view_trek'),
    path('edit-trek/<int:id>/', EditTrek, name='edit_trek'),
    path('delete-trek/<int:id>/', DeleteTrek, name='delete_trek'),
]