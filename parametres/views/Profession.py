from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from parametres.models import Profession
from parametres.serializers import ProfessionSerializer

# Profession
@csrf_exempt
def profession_list(request):
    """
    List all code professions, or create a new profession.
    """
    if request.method == 'GET':
        professions = Profession.objects.all()
        serializer = ProfessionSerializer(professions, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProfessionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def profession_detail(request, pk):
    """
    Retrieve, update or delete a code profession.
    """
    try:
        profession = Profession.objects.get(pk=pk)
    except Profession.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProfessionSerializer(profession)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProfessionSerializer(profession, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        profession.delete()
        return HttpResponse(status=204)

