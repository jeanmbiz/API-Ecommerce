from . import views
from django.urls import path


urlpatterns = [
    path("products/", views.ProductsView.as_view()),
    path("products/id/<uuid:pk>/", views.ProductsDetailView.as_view()),
    path("products/name/<str:product_name>/", views.ProductByNameView.as_view()),
    path("products/category/<str:product_category>/", views.ProductByCategoryView.as_view()),
]
