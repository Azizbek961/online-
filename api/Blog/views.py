# from rest_framework import serializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import BlogSerializer
from blog.models import Blog


@api_view(['GET', 'POST'])
def get_list_ctg(request):
    if request.method == "GET":
        blog = Blog.objects.all()
        result = BlogSerializer(blog, many=True)
        print(result.data)
        return Response({"data": result.data})

    elif request.method == "POST":
        serializer = BlogSerializer(data=request.data)
        print(serializer, serializer.is_valid())
        if serializer.is_valid():
            result = serializer.save()
            print(result)
            return Response({'data': "success"}, status=status.HTTP_201_CREATED)
@api_view(["GET", "PUT", "DELETE"])
def detail_ctg(request, pk):
    try:
        category = Blog.objects.get(pk=pk)
    except Blog.DoesNotExist:
        return Response({"error": "Could not found"})

    if request.method == "GET":
        serializer = BlogSerializer(category)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = BlogSerializer(category, data=request.data)
        print(serializer.is_valid(), serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "Could not edit"}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
