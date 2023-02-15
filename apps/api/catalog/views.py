from rest_framework import generics,permissions,viewsets
from apps.catalog.models import Category,Product
from apps.api.catalog.serializers import CategorySerializer,ProductReadSerializer,ProductWriteSerializer

class ProductListView(generics.ListAPIView):
    serializer_class = ProductReadSerializer


    def get_queryset(self):
        queryset = Product.objects.all(is_checked=True)
        category = self.request.query_params('category')
        if category:
            queryset = queryset.filter(categories=category)
        name = self.request.query_params(is_checked=True)
        if name:
            queryset = queryset.filter(categories=name)
        return queryset
class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            return [permission() for permission in [permissions.IsAdminUser]]
        return [permission() for permission in [permissions.AllowAny]]
class ProductDetailView(generics.RetrieveAPIView):
    serializer_class = ProductReadSerializer
    queryset = Product.objects.all()

class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductWriteSerializer
    queryset = Product.objects.all()
    permission_classes = [permissions.IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ProductUpdateView(generics.UpdateAPIView):
    serializer_class = ProductWriteSerializer
    queryset = Product.objects.all()
    permission_classes = [permissions.IsAdminUser]

class ProductDeleteView(generics.DestroyAPIView):
    serializer_class = ProductWriteSerializer
    queryset = Product.objects.all()
    permission_classes = [permissions.IsAdminUser]
