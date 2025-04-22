from rest_framework import serializers
from blog.models import BLog

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BLog
        fields = ['id','title','description','category','author',"user"]
