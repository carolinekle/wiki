from django.shortcuts import render
import markdown
from . import util
import random

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
    return render(request, "encyclopedia/new.html")

def new_submit(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        old_entry = util.get_entry(title)
    if content and title is not None:
        util.save_entry(title, content)
        md_content = convert(title)
        return render(request, "encyclopedia/entry.html",{
            "title":title,
            "content":md_content
        })
    if old_entry is not None:
        return render(request, "encyclopedia/error.html")
    else:
        return render(request, "encyclopedia/error.html")
    
def edit(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit.html", {
            "title": title,
            "content":content
        })
    
def save_edit(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        util.save_entry(title, content)
        html_content = convert(title)
        return render(request, "encyclopedia/entry.html",{
            "title":title,
            "content":html_content
        })

def random_page(request):
    entries = util.list_entries()
    title = random.choice((entries))
    html_content = convert(title)
    return render(request, "encyclopedia/entry.html",{
    "title": title,
    "content": html_content
})