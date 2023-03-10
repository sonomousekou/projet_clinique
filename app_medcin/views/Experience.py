from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from app_medcin.serializers import ExperienceSerializer
from app_medcin.models import Experience


# experience
@csrf_exempt
def experience_list(request):
    """
    List all code experiences, or create a new experience.
    """
    if request.method == 'GET':
        experiences = Experience.objects.all()
        serializer = ExperienceSerializer(experiences, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ExperienceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def experience_detail(request, pk):
    """
    Retrieve, update or delete a code experience.
    """
    try:
        experience = Experience.objects.get(pk=pk)
    except Experience.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ExperienceSerializer(experience)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ExperienceSerializer(experience, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        experience.delete()
        return HttpResponse(status=204)
    