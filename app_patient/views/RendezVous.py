from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app_patient.serializers import RendezVousSerializer
from app_patient.models import RendezVous

# RendezVous
@api_view(['GET', 'POST'])
def rendezVous_list(request, format=None):
    """
    List all code rendezVouss, or create a new rendezVous.
    """
    if request.method == 'GET':
        rendezVouss = RendezVous.objects.all()
        serializer = RendezVousSerializer(rendezVouss, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RendezVousSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def rendezVous_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code rendezVous.
    """
    try:
        rendezVous = RendezVous.objects.get(pk=pk)
    except RendezVous.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RendezVousSerializer(rendezVous)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = RendezVousSerializer(rendezVous, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        rendezVous.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


