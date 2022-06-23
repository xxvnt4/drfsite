from django.forms import model_to_dict
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Women
# Этот класс стоит во главе иерархии всех классов представления DRF.
# Самый базовый функционал.

# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer

class WomenAPIView(APIView):
    def get(self, request):
        # Метод, который будет отвечать за обработку GET-запросов.
        lst = Women.objects.all().values()
        return Response({'posts': list(lst)})

    def post(self, request):
        post_new = Women.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id']
        )

        return Response({'post': model_to_dict(post_new)})
