from django.urls import path
from .api import UpdateRNCDataFromCSV, Views

urlpatterns = [
    path('updateDate/', UpdateRNCDataFromCSV.as_view(), name='update_rnc_data'),
    path('viewsDate/', Views.as_view({'get': 'list'}), name="viewsDate")
]

