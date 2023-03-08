
# class SpecialiteList(generics.ListCreateAPIView):
#     queryset=Specialite.objects.all()
#     serializer_class=SpecialiteSerializer
#     permission_classes = [IsAdminUser]
    
# class SpecialiteListDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset=Specialite.objects.all()
#     serializer_class=SpecialiteSerializer
#     permission_classes = [IsAdminUser]


# path(r'',SpecialiteList.as_view(),name='Specialite/'),
    # path(r'api/(?P<pk>[0-9]+)/$', SpecialiteListDetail.as_view(),name='Specialitedetails/'),
    

@csrf_exempt
def patient_list(request):
    """
    List all code patients, or create a new patient.
    """
    if request.method == 'GET':
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PatientSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def patient_detail(request, pk):
    """
    Retrieve, update or delete a code patient.
    """
    try:
        patient = Patient.objects.get(pk=pk)
    except Patient.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PatientSerializer(patient)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PatientSerializer(patient, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        patient.delete()
        return HttpResponse(status=204)


    path('patients/', views.patient_list),
    path('patients/<str:pk>/', views.patient_detail),

