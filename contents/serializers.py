from rest_framework.serializers import ModelSerializer

from contents.models import Content
class ContentSerializer(ModelSerializer):
    class Meta:
        model = Content
        fields = ['id', 'name', 'content', 'video_url' ]
        extra_kwargs = {
            'course': {'read_only' : True},
            'students': {'read_only' : True}
        }
        depth = 1 
        
        
        