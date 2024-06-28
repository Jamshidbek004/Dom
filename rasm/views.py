from rest_framework import viewsets
from rasm.models import (
    ImageKirish, ImagemMaket, ImagemOrqafon, ImagemMatn,
    House, Video, Contact, Contact2, NashiUslugi, HouseDesign
)
from .serializers import (
    ImageKirishSerializer, ImagemMaketSerializer, ImagemOrqafonSerializer, ImagemMatnSerializer,
    HouseSerializer, VideoSerializer, ContactSerializer, Contact2Serializer, NashiUslugiSerializer, HouseDesignSerializer
)

class ImageKirishViewSet(viewsets.ModelViewSet):
    queryset = ImageKirish.objects.all()
    serializer_class = ImageKirishSerializer

class ImagemMaketViewSet(viewsets.ModelViewSet):
    queryset = ImagemMaket.objects.all()
    serializer_class = ImagemMaketSerializer

class ImagemOrqafonViewSet(viewsets.ModelViewSet):
    queryset = ImagemOrqafon.objects.all()
    serializer_class = ImagemOrqafonSerializer

class ImagemMatnViewSet(viewsets.ModelViewSet):
    queryset = ImagemMatn.objects.all()
    serializer_class = ImagemMatnSerializer

class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class Contact2ViewSet(viewsets.ModelViewSet):
    queryset = Contact2.objects.all()
    serializer_class = Contact2Serializer

class NashiUslugiViewSet(viewsets.ModelViewSet):
    queryset = NashiUslugi.objects.all()
    serializer_class = NashiUslugiSerializer

class HouseDesignViewSet(viewsets.ModelViewSet):
    queryset = HouseDesign.objects.all()
    serializer_class = HouseDesignSerializer
