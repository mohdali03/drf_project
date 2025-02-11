from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from snippets.serializers import SinppetsSerializer
from .models import Snippet
from django.http import HttpResponse, JsonResponse
from io import BytesIO
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics  import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin

class snippetsCreateList(ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SinppetsSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class snippetsDetail(RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SinppetsSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]
    
    
    
# class RcApi(GenericAPIView, ListModelMixin, CreateModelMixin):
#     queryset = Snippet.objects.all()
#     serializer_class = SinppetsSerializer
    
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    
# class RUDApi(GenericAPIView, RetrieveModelMixin, UpdateModelMixin,DestroyModelMixin):
#     queryset = Snippet.objects.all()
#     serializer_class = SinppetsSerializer
    
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

# # Create your views here.
# def snippets(req, pk):
#     snippet = Snippet.objects.get(id = 1)
#     print("snippent ======== /n", snippet)
#     serializer = SinppetsSerializer(snippet)
#     # print("serializer =========== /n",serializer)
#     # print("serializer Data ============ /n",serializer.data)
    
#     # snippet_json = JSONRenderer().render(serializer.data)
#     # print("JSON ===== /n",snippet_json)
#     return JsonResponse(serializer.data)

# @csrf_exempt
# def create(req):
#     if req.method == "POST":
#         json_data = req.body
#         stream = BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         serializer = SinppetsSerializer(data = pythondata)
#         if serializer.is_valid():
#             serializer.save()
#             res =  {'msg': "data Created"}
#             return JsonResponse(res)
#         else:
#             return JsonResponse(serializer.errors)
