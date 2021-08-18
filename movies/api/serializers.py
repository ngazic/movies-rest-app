from movies.models import Movie, StreamPlatform, Review
from rest_framework import serializers

class MovieSerializer(serializers.ModelSerializer):
    # platform = serializers.CharField(source='platform.name',read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'


class PlatformSerializer(serializers.ModelSerializer):
    # watchlist = MovieSerializer(many=True, read_only=True)
    class Meta:
        model = StreamPlatform
        fields = '__all__'

        
class ReviewSerializer(serializers.ModelSerializer):
    # watchlist = MovieSerializer(many=True, read_only=True)
    class Meta:
        model = Review
        # fields = '__all__'
        exclude = ('movie',)


