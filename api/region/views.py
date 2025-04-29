# from rest_framework.response import Response
# from rest_framework import status, viewsets
# from product.models import Product
# from .serializers import RegionSerializer
# from rest_framework.decorators import api_view
# from category.models import Region
# from rest_framework import mixins
# from rest_framework.generics import GenericAPIView
# from ..product.serializers import ProductSerializer
#
#
# @api_view(['GET','POST'])
# def get_list_rgn(request):
#     if request.method == "GET":
#         regions = Region.objects.all()
#         result = RegionSerializer(regions, many=True)
#         print(result.data)
#         return Response({"data": result.data})
#     elif request.method == "POST":
#         serializer = RegionSerializer(data=request.data)
#         print(serializer, serializer.is_valid())
#         if serializer.is_valid():
#             result = serializer.save()
#             print(result)
#             return Response({"data": "success"}, status=status.HTTP_201_CREATED)
#
# @api_view(['GET','PUT','DELETE'])
# def detail_rgn(request, pk):
#     try:
#         region = Region.objects.get(pk=pk)
#     except Region.DoesNotExist:
#         return Response({"error": "Could not found"}, status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == "GET":
#         serializer = RegionSerializer(region)
#         return Response(serializer.data)
#
#     elif request.method == "PUT":
#         serializer = RegionSerializer(region, data=request.data)
#         print(serializer.is_valid(), serializer)
#         if serializer.is_valid():
#             serializer.save()
#             print(serializer)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response({"error": "Could not edit"}, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == "DELETE":
#         region.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# class RegionGenericAPIView(GenericAPIView):
#     queryset = Region.objects.all()
#     serializer_class = RegionSerializer
#
#     def get(self, request):
#         books = self.get_queryset()
#         serializer = self.get_serializer(books, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#
# class RegionGenericDetailAPIView(GenericAPIView):
#     queryset = Region.objects.all()
#     serializer_class = RegionSerializer
#     def get(self, request, *args, **kwargs):
#         region = self.get_object()
#         serializer = self.get_serializer(region)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def put(self, request, *args, **kwargs):
#         region = self.get_object()
#         serializer = self.get_serializer(region, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response({"Error":"request not valid"}, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, *args, **kwargs):
#         region = self.get_object()
#         region.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
# class RegionGenericAPIViewMixin(GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
#     queryset = Region.objects.all()
#     serializer_class = RegionSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
# class RegionGenericDetailAPIViewMixin(GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
#     queryset = Region.objects.all()
#     serializer_class = RegionSerializer
#     lookup_field = 'pk'
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request,*args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
#
# class ProductViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
