from rest_framework import serializers

from leitura.serializers import LeituraSerializer
from .models import Dispositivo


class DispositivoSerializer(serializers.ModelSerializer):
    # ADICIONAR CAMPO leituras, POIS TERÁ VÁRIAS LEITURAS POR DISPOSITIVO
    leitura_set = LeituraSerializer(many=True, required=False)
    class Meta:
        model = Dispositivo
        # fields = ['id','mac', 'email', 'leitura_set']
        fields = '__all__'