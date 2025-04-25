# from rest_framework import serializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import ProductSerializer
from product.models import Product
from rest_framework.views import APIView


@api_view(['GET', 'POST'])
def get_list_ctg(request):
    if request.method == "GET":
        product = Product.objects.all()
        result = ProductSerializer(product, many=True)
        print(result.data)
        return Response({"data": result.data})

    elif request.method == "POST":
        serializer = ProductSerializer(data=request.data)
        print(serializer, serializer.is_valid())
        if serializer.is_valid():
            result = serializer.save()
            print(result)
            return Response({'data': "success"}, status=status.HTTP_201_CREATED)
@api_view(["GET", "PUT", "DELETE"])
def detail_ctg(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({"error": "Could not found"})

    if request.method == "GET":
        serializer = ProductSerializer(Product)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = ProductSerializer(product, data=request.data)
        print(serializer.is_valid(), serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "Could not edit"}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductView(APIView):
    def get(self, request):
        product = Product.objects.all()
        result = ProductSerializer(product, many=True)
        return Response({"data": result.data})

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        print(serializer.is_valid())
        if serializer.is_valid():
            result = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductViews(APIView):
    def get(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({"Error": "Could not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"Error": "Could not edit"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = Product.objects.get(pk=pk)
        product.delete()
        return Response("Product successful deleted",status=status.HTTP_204_NO_CONTENT)
