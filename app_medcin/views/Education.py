from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from app_medcin.serializers import EducationSerializer
from app_medcin.models import Education

# Education
@csrf_exempt
def education_list(request):
    """
    List all code educations, or create a new education.
    """
    if request.method == 'GET':
        educations = Education.objects.all()
        serializer = EducationSerializer(educations, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EducationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def education_detail(request, pk):
    """
    Retrieve, update or delete a code education.
    """
    try:
        education = Education.objects.get(pk=pk)
    except Education.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = EducationSerializer(education)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = EducationSerializer(education, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        education.delete()
        return HttpResponse(status=204)
