from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions

from parametres.models import Type_Piece
from parametres.serializers import Type_PieceSerializer

@api_view(["POST"])
def ajoutType_piece(request):
    if request.method == 'POST' :
        type_piece = Type_PieceSerializer(data=request.data)
        if type_piece.is_valid():
            type_piece.save()
            return Response(type_piece.data, status.HTTP_201_CREATED)
        else:
            return Response({'text': 'type_piece non créé'}, status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'text': 'cette méthode n\'est pas appliquée sur cette fonction'}, status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", 'DELETE'])
def type_piece(request, pk: str):
    try:
        type_piece: Type_Piece = Type_Piece.objects.get(pk=pk)
    except Exception as e:
        return Response({'text': 'Type_Piece non trouvé'}, status=status.HTTP_404_NOT_FOUND)
    
    if  request.method == 'GET' :
        return Response(Type_PieceSerializer(type_piece).data, status.HTTP_200_OK)

    elif request.method == 'PUT' :
        serializer = Type_PieceSerializer(type_piece, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        else:
            return Response({'text': 'Type_Piece non modifié'}, status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        type_piece.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response({'text': 'cette méthode n\'est pas appliquée sur cette fonction'}, status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def type_pieces(request):
    return Response(Type_PieceSerializer(Type_Piece.objects.all(), many=True).data, status.HTTP_200_OK)

