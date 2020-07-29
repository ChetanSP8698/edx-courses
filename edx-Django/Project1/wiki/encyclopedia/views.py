from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import markdown2
import re
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
		if re.match(search_req, item, flags=re.IGNORECASE):
			return HttpResponseRedirect(f"wiki/{item}")


