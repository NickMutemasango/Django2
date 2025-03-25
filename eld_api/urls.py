# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import TripViewSet, ELDLogViewSet
# from django.urls import path, include
# from .views import calculate_stops  # Import calculate_stops here



# router = DefaultRouter()
# router.register(r'trips', TripViewSet)
# router.register(r'eldlogs', ELDLogViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
#     path('calculate-stops/', calculate_stops, name='calculate-stops'),
#         # path('generate-eld-logs/', generate_eld_logs, name='generate-eld-logs'),
# ]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TripViewSet, ELDLogViewSet
from .views import calculate_stops
from .views import generate_eld_logs

router = DefaultRouter()
router.register(r'trips', TripViewSet)
router.register(r'eldlogs', ELDLogViewSet)

urlpatterns = [
    path('', include(router.urls)),
      path('calculate-stops/', calculate_stops, name='calculate-stops'),
          path('generate-eld-logs/', generate_eld_logs, name='generate-eld-logs'),
]



