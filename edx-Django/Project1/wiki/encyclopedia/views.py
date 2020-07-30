from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
import markdown2
import re
import random
from . import util


def index(request):
	return render(request, "encyclopedia/index.html", {
		"entries": util.list_entries()
	})

def page(request, title):
	if util.get_entry(title):
		md = markdown2.Markdown()
		return render(request, "encyclopedia/wiki.html", {
			"entries": md.convert(util.get_entry(title))
		})
	else:
		return render(request, "encyclopedia/error.html")

def search(request):
	entries = util.list_entries()
	search_req = request.GET.get("q")

	list = []
	for item in entries:
		lcase = item.lower()
		if lcase.find(search_req.lower()) == -1:
			pass
		else:
			list.append(item)

	if len(list) > 1 :
		return render(request, "encyclopedia/search.html", {
			"output" : list
		})

	elif len(list) == 1:
		for item in entries:
			if re.match(search_req, item, flags=re.IGNORECASE) and len(search_req) == len(item):
				return HttpResponseRedirect(f"wiki/{item}")
			
		return render(request, "encyclopedia/search.html", {
			"output" : list
		})

	else:
		for item in entries:
			if re.match(search_req, item, flags=re.IGNORECASE) and len(search_req) == len(item):
				return HttpResponseRedirect(f"wiki/{item}")
			else:
				return render(request, "encyclopedia/error.html")

	
def create(request) :
	if request.method == "POST":
		title = request.POST.get("title")
		content = request.POST.get("content")
		entries = util.list_entries()
		
		for item in entries:
			if re.match(title, item, flags=re.IGNORECASE) and len(title) == len(item):
				return render(request, "encyclopedia/create_error.html")
		
		util.save_entry(title, content)
		return HttpResponseRedirect(f"wiki/{title}")
	else:
		title = ""
		content = ""
		return render(request, "encyclopedia/create.html")

def randompage(request):
	entries = util.list_entries()
	title = random.choice(entries)
	return HttpResponseRedirect(f"wiki/{title}")

def edit(request):
    if request.method == "GET":
        pre_url = request.META.get('HTTP_REFERER')
        cont = pre_url.split('/')
        cont = cont[-1]
        return render(request, "encyclopedia/edit.html", {
			"content" : util.get_entry(cont),
			"title" : cont
		})
    
    elif request.method == "POST" :
        title = request.POST.get("edited_title")
        content = request.POST.get("edited_content")
        util.save_entry(title, content)
        return HttpResponseRedirect(f"wiki/{title}")
        