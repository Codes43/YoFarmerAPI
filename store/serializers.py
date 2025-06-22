from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField() 
    imageUrl = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_imageUrl(self, obj):
        if obj.image:
            request = self.context.get('request')
            if request is not None:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return ''

    def get_category_name(self, obj):
        return obj.get_category_display()