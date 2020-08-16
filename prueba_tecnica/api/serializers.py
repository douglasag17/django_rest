from api.models import Producto
from rest_framework import serializers


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = (
            "categoria",
            "descripcion",
            "identificacion",
            "fecha_inicio",
            "nombre_producto",
            "valor",
        )
        # fields = '__all__'
