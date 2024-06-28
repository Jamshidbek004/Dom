from rest_framework import serializers
from rasm.models import (
    ImageKirish, ImagemMaket, ImagemOrqafon, ImagemMatn,
    House, Video, Contact, Contact2, NashiUslugi, HouseDesign
)

class ImageKirishSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageKirish
        fields = '__all__'

class ImagemMaketSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagemMaket
        fields = '__all__'

class ImagemOrqafonSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagemOrqafon
        fields = '__all__'

class ImagemMatnSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagemMatn
        fields = '__all__'

class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = '__all__'

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class Contact2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Contact2
        fields = '__all__'

class NashiUslugiSerializer(serializers.ModelSerializer):
    class Meta:
        model = NashiUslugi
        fields = '__all__'

class HouseDesignSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseDesign
        fields = '__all__'
