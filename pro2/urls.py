"""pro2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from kernel import index, search

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index.index),
    url(r'^log_in_temp', index.log_in_temp),
    url(r'^log_in_by_github', index.log_in_by_github),
    url(r'^log_out', index.log_out),
    url(r'^search_authors', search.search_authors),
    url(r'^search_coauthors', search.search_coauthors),
    url(r'^expert_finding', search.expert_finding),
    url(r'^coauthors', search.coauthors),

]
