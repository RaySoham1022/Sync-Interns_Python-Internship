from django.shortcuts import render

import pyshorteners


def index(request, **kwargs):
    if request.method == 'POST':
        try:
            link = request.POST.get('longurl')
            shortener = pyshorteners.Shortener()
            finalurl = shortener.tinyurl.short(link)
            shorturlvalue = finalurl
            data = {'shorturlvalue':shorturlvalue}
            return render(request, "index.html", data)
        except:
            shorturlvalue = ""
            data = {'shorturlvalue':shorturlvalue}
            return render(request, "index.html", data)
    else:
        shorturlvalue = ""
        data = {'shorturlvalue':shorturlvalue}
        return render(request, "index.html", data)

