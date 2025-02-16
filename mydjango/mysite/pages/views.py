# from django.shortcuts import render
# from django.http import HttpResponse
# from .models import Page

# # def index_pages(request):
# #     return HttpResponse("<h1 style='text-align :center ;'>Site de GLAASRI : Application pages</h1>")

# # def index_pages(request) :
# #     return render (request, 'pages/page.html')


# def index_pages(request, pagename=''):
#     pagename = '/' + pagename
#     pg = Page.objects.get(permalink=pagename)
#     context = {
#         'title': pg.title,
#         'content': pg.bodytext,
#         'last_updated': pg.updated_at,
#     }
#     return render(request, 'pages/page.html', context)


from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Page

def index_pages(request, pagename=''):
    pagename = '/' + pagename
    try:
        pg = Page.objects.get(permalink=pagename)
    except Page.DoesNotExist:
        raise Http404("Page does not exist")
    
    context = {
        'title': pg.title,
        'content': pg.bodytext,
        'last_updated': pg.updated_at,
        'page_list': Page.objects.all(),
    }
    return render(request, 'pages/page.html', context)