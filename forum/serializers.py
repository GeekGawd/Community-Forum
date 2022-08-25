from rest_framework import serializers
from .models import Account, Post

class PostSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Post
        fields = '__all__'
    
class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = '__all__'