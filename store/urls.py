from django.urls import path
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from . import views
from pprint import pprint

router = routers.DefaultRouter()
router.register('products', views.ProductViewSet, basename='product')
router.register('collections', views.CollectionViewSet)
router.register('carts', views.CartViewSet)

products_router = routers.NestedDefaultRouter(
    router, 'products', lookup='product')
products_router.register('reviews', views.ReviewViewSet,
                         basename='product-reviews')

cart_router = routers.NestedDefaultRouter(
    router, 'carts', lookup='cart')
cart_router.register('items', views.CartItemViewSet,
                     basename='cart-items')

pprint(router.urls + products_router.urls + cart_router.urls)
# URLConf
# urlpatterns = router.urls + products_router.urls + cart_router.urls
urlpatterns = router.urls + products_router.urls + cart_router.urls
#     path('products/', views.ProductList.as_view()),
#     path('products/<int:pk>/', views.ProductDetail.as_view()),
#     path('collections/', views.CollectionList.as_view()),
#     path('collections/<int:pk>/', views.CollectionDetail.as_view(),
#          name='collection-detail'),
# ]
