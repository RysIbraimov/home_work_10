from django.urls import path

from . import views

urlpatterns = [
    path('category/',views.CategoryApiView.as_view(), name='category'),
    path('category/<int:id>',views.CategoryDetailView.as_view(), name='category_detail'),

    path('firm/',views.FirmApiView.as_view(), name='firm'),
    path('firm/<int:id>',views.FirmDetailView.as_view(), name='firm_detail'),

    path('item/',views.ItemApiView.as_view(), name='item'),
    path('item/<int:id>',views.ItemDetailView.as_view(), name='item_detail'),
]