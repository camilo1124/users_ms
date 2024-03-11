from .models import UserUN
from .serializers import UserunSerializer
from rest_framework import mixins, generics

# Create your views here.

class UserList(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               generics.GenericAPIView):
    
    queryset = UserUN.objects.all()
    serializer_class = UserunSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



class UserDetail(mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 generics.GenericAPIView):
    
    queryset = UserUN.objects.all()
    serializer_class = UserunSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
class UserDetailByPhone(mixins.RetrieveModelMixin,                 
                 generics.GenericAPIView):
    
    queryset = UserUN.objects.all()
    serializer_class = UserunSerializer
    lookup_field = 'phone'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    

    
    