from django.shortcuts import render
from django.http import HttpResponse
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
