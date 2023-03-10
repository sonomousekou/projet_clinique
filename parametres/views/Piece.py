from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions

from parametres.models import Piece
from parametres.serializers import PieceSerializer

@api_view(["POST"])
def ajoutpiece(request):
    if request.method == 'POST' :
        piece = PieceSerializer(data=request.data)
        if piece.is_valid():
            piece.save()
            return Response(piece.data, status.HTTP_201_CREATED)
        else:
            return Response({'text': 'piece non créé'}, status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'text': 'cette méthode n\'est pas appliquée sur cette fonction'}, status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", 'DELETE'])
def piece(request, pk: str):
    try:
        piece: Piece = Piece.objects.get(pk=pk)
    except Exception as e:
        return Response({'text': 'Piece non trouvé'}, status=status.HTTP_404_NOT_FOUND)
    
    if  request.method == 'GET' :
        return Response(PieceSerializer(piece).data, status.HTTP_200_OK)

    elif request.method == 'PUT' :
        serializer = PieceSerializer(piece, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        else:
            return Response({'text': 'Piece non modifié'}, status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        piece.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response({'text': 'cette méthode n\'est pas appliquée sur cette fonction'}, status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def pieces(request):
    return Response(PieceSerializer(Piece.objects.all(), many=True).data, status.HTTP_200_OK)

