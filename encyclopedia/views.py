from django.shortcuts import render
from . import util
from django.http import HttpResponse, HttpResponseNotFound, Http404,  HttpResponseRedirect
import markdown2 , random
from .forms import CreatePageForm , EditPageForm


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

#Site_Search 

def site_name(request, site_name):
	title = util.get_entry(site_name)

	if title:
		title_html = markdown2.markdown(title)
		context = { 'title' : site_name, "html_display" : "{}".format(title_html) }
		return render(request, "encyclopedia/entry_page.html", context)
	else:
		return render(request, "encyclopedia/entry_page.html", {"html_display" : "Error 404 : Page Not Found"})

#Create Page

def create_page(request):

	if request.method == 'POST':
		form = CreatePageForm(request.POST)
		if form.is_valid():

			title_newpage = form.cleaned_data['title']
			markdown_newpage =  "#{}\n".format(title_newpage) + form.cleaned_data['Textarea']


			util.save_entry(title_newpage, markdown_newpage)

			return HttpResponseRedirect("/")

	form = CreatePageForm()
	return render(request, "encyclopedia/create_page.html", {'form':form })

#Edit Page

def edit_page(request, site_name):

	if request.method == 'POST':
		form = EditPageForm(request.POST)
		if form.is_valid():

			
			markdown_newpage = form.cleaned_data['Textarea']


			util.save_entry(site_name, markdown_newpage)


			return HttpResponseRedirect("/")

	form = EditPageForm(initial={'title': site_name , 'Textarea' : util.get_entry(site_name)})
	return render(request, "encyclopedia/edit_page.html" , {'form' : form})

#Search

def search(request):
	search_query = request.POST.get('q')
	entry_list = util.list_entries()
	search_result = []

	if search_query in entry_list:
		return HttpResponseRedirect("/wiki/{}/".format(search_query))

	for i in entry_list:
		print(i)
		print(search_query)
		if search_query.lower() in i.lower():
			search_result.append(i)
			continue

		elif i.lower() in search_query.lower():
			search_result.append(i)
			continue

	if len(search_result) == 0:
		return render(request, "encyclopedia/search_result_not_found.html")


	return render(request, "encyclopedia/search_result.html", {'search_result' : search_result})







# Random Page

def random_page(request):
	random_page = random.choice(util.list_entries())
	return HttpResponseRedirect("/wiki/{}/".format(random_page))
	



