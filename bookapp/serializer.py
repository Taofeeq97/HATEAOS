from rest_framework.serializers import ModelSerializer
from .models import Book
from rest_framework import serializers
from rest_framework.reverse import reverse


class BookSerializer(ModelSerializer):
    detail_url = serializers.SerializerMethodField()
    update_url = serializers.SerializerMethodField()
    delete_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Book
        fields = ['id','detail_url', 'update_url','delete_url', 'title','description','created_at','updated_at']

    
    def get_detail_url(self, obj):
        request = self.context.get('request')
        absolute_url = reverse('book_detail_api_view', args=[str(obj.id)], request=request)
        return absolute_url
        
    def get_update_url(self, obj):
        request = self.context.get('request')
        update_url = reverse('book_detail_update_api_view', args=[str(obj.id)], request=request)
        return update_url
    
    def get_delete_url(self, obj):
        request = self.context.get('request')
        delete_url =  reverse('book_detail_delete_api_view', args=[str(obj.id)], request=request)
        return delete_url
        