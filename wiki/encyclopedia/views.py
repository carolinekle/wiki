from django.shortcuts import render
from django.db.models import Q
import markdown
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def convert(title):
    content = util.get_entry(title)
    if content == None:
        return 
    else:
        html_content = markdown.markdown(content)
        return html_content

def entry_page(request, title):
    html_content = convert(title)
    if html_content == None:
        return render(request, "encyclopedia/error.html")
    else:
        return render(request, "encyclopedia/entry.html",{
        "title": title,
        "content": html_content
    })

def search(request):
    if request.method == "POST":
        entry_search = request.POST["q"]
        html_content = convert(entry_search)

        if html_content is not None:
            return render(request, "encyclopedia/entry.html", {
                "title":entry_search,
                "content": html_content
            })
        else:
            all = util.list_entries()
            rec = []
            for entry in all:
                if entry_search.lower() in entry.lower():
                    rec.append(entry)
            return render(request, "encyclopedia/search.html",{
                "rec":rec
            })
        
def new(request):
    return