from django.urls import path
from products.views import delete, productsindex,index,show,delete,createproduct,UpdateProductView

urlpatterns = [
      path("all", productsindex, name="products.all"),
      path("", index, name="products.index"),
      path("<int:id>", show, name= "products.show"),
      path("delete/<id>",delete,name='products.delete'),
      path("create", createproduct, name='products.create'),
      path("edit/<int:pk>",UpdateProductView.as_view(),name="products.edit")
]