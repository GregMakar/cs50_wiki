from django.shortcuts import render
import markdown2
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def page(request, page_name):
    if util.get_entry(page_name):
        return render(request, "encyclopedia/page.html", {
            "page_name": page_name,
            "render": markdown2.markdown(util.get_entry(page_name))
        })
    else:
        return render(request, "encyclopedia/error.html", {
            "error": f"Error 404 page name: {page_name} was not found! "
        })