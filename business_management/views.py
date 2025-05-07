from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Business
from .serializers import BusinessSerializer, BusinessCreateSerializer
from auth_management.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def business_view(request):
    user = request.user
    userSerializer = UserSerializer(instance=user)
    if request.method == "GET":
        pk = request.query_params.get("pk")
        if pk:
            try:
                business = Business.objects.get(pk=pk, owner=user)
                serializer = BusinessSerializer(business)
                return Response(serializer.data)
            except Business.DoesNotExist:
                return Response({"error": "Business not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            businesses = Business.objects.filter(owner=user)
            serializer = BusinessSerializer(businesses, many=True)
            return Response(serializer.data)

    elif request.method == "POST":
        serializer = BusinessCreateSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(owner=user)
            return Response({
                "data":serializer.data,
                "user":userSerializer.data,
                }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

