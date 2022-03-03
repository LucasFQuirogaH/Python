"""Pro1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Pro1.views import calculaEdad, calculaEdad2, dameFecha, despedida, saludo , despedida

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('despedida/', despedida),
    path('dameFecha/', dameFecha),
    path('edades/<int:anio>' , calculaEdad), # Ahi le pasamos el parametro y lwe indicamos que es entero para que lo convierta en entero
    path('edades2/<int:edad>/<int:anio>' , calculaEdad2), # Tal cual lo coloques entre literales tal cual es escribirlo en la URL
]

# se puede agregar urls o vistas hacia otros, como jsps...
