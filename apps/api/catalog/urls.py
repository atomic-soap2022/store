from django.urls import path
from apps.api.catalog.views import ProductListView,ProductDetailView,ProductCreateView,ProductDeleteView,\
ProductUpdateView


urlpatterns = [
    path('product/', ProductListView.as_view()),
    path('product/<int:pk>/', ProductDetailView.as_view()),
    path('product/create/', ProductCreateView.as_view()),
    path('product/update/<int:pk>/', ProductUpdateView.as_view()),
    path('product/delete/create/', ProductDeleteView.as_view()),
]
