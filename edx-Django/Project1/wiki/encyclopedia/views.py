from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
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
	for item in entries:
		if re.match(search_req, item, flags=re.IGNORECASE) and len(search_req) == len(item):
			return HttpResponseRedirect(f"wiki/{item}")

	list = []
	for item in entries:
		if item.lower().find(search_req.lower()) == -1:
			pass
		else:
			list.append(item)

	return render(request, "encyclopedia/search.html", {
		"output" : list
	})

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
	return render(request, "encyclopedia/create.html")

def randompage(request):
	entries = util.list_entries()
	title = random.choice(entries)
	return HttpResponseRedirect(f"wiki/{title}")

