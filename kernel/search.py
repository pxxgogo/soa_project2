__author__ = 'pxxgogo'
from django.http import HttpResponseRedirect
from django.http import JsonResponse

from data_model import Data_model


def search_authors(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/")
    else:
        domain = request.GET['domain']
        author_info_list = Data_model.get_authors_with_domain(domain)
        # print(author_info_list)
        return JsonResponse({"authors": author_info_list}, safe=False)

def search_coauthors(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/")
    else:
        author_index = request.GET['author_index']
        author_info_list = Data_model.get_coauthors(author_index)
        # print(author_info_list)
        return JsonResponse({"authors": author_info_list}, safe=False)
