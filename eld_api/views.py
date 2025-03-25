# from django.shortcuts import render

# # Create your views here.
# from rest_framework import viewsets
# from .models import Trip, ELDLog
# from .serializers import TripSerializer, ELDLogSerializer
# from rest_framework.decorators import api_view  # Add this import

# class TripViewSet(viewsets.ModelViewSet):
#     queryset = Trip.objects.all()
#     serializer_class = TripSerializer

# class ELDLogViewSet(viewsets.ModelViewSet):
#     queryset = ELDLog.objects.all()
#     serializer_class = ELDLogSerializer

#     from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from datetime import timedelta

# @api_view(['POST'])
# def calculate_stops(request):
#     trip_id = request.data.get('trip_id')
#     trip = Trip.objects.get(id=trip_id)
#     driving_hours = trip.cycle_hours



#     # Example logic for calculating rests based on driving rules
#     if driving_hours > 8:
#         rests = [{"type": "Rest", "duration": "30 minutes"}]
#     else:
#         rests = []

#     return Response({"trip_id": trip_id, "rests": rests})
    


    
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Trip, ELDLog
from .serializers import TripSerializer, ELDLogSerializer
from datetime import timedelta

# ViewSet for Trip
class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

# ViewSet for ELDLog
class ELDLogViewSet(viewsets.ModelViewSet):
    queryset = ELDLog.objects.all()
    serializer_class = ELDLogSerializer

# Custom view for calculating stops
@api_view(['POST'])
def calculate_stops(request):
    trip_id = request.data.get('trip_id')
    
    if not trip_id:
        return Response({"error": "trip_id is required"}, status=400)
    
    try:
        trip = Trip.objects.get(id=trip_id)
    except Trip.DoesNotExist:
        return Response({"error": "Trip not found"}, status=404)
    
    driving_hours = trip.cycle_hours

    # Example logic for calculating rests based on driving rules
    if driving_hours > 8:
        rests = [{"type": "Rest", "duration": "30 minutes"}]
    else:
        rests = []

    return Response({"trip_id": trip_id, "rests": rests})

# Custom view for generating ELD logs
@api_view(['POST'])
def generate_eld_logs(request):
    trip_id = request.data.get('trip_id')
    
    if not trip_id:
        return Response({"error": "trip_id is required"}, status=400)
    
    try:
        trip = Trip.objects.get(id=trip_id)
    except Trip.DoesNotExist:
        return Response({"error": "Trip not found"}, status=404)
    
    # Example logic to generate ELD logs
    ELDLog.objects.create(
        trip=trip,
        log_type="Driving",
        start_time=trip.start_time,
        end_time=trip.end_time,
    )
    
    return Response({"message": "ELD logs generated successfully"})