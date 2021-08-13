# I have created this file -Piyush
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse("Home")
    return render(request, 'index.html')


def analyze(request):
    # get the text
    djtext = request.POST.get('text', 'default')
    print(djtext)
    # check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    print(removepunc)
    fullcaps = request.POST.get('fullcaps', 'off')
    print(fullcaps)
    newlineremover = request.POST.get('newlineremover', 'off')
    print(newlineremover)
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    print(extraspaceremover)
    charcounter = request.POST.get('charcounter', 'off')
    print(charcounter)
    # check which checkbox is on
    if (removepunc == "on"):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        # analyze the text
        # return render(request,'analyze.html',params)
    if (fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # analyze the text
        # return render(request,'analyze.html',params)
    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
            else:
                print("no")
        params = {'purpose': 'Remove New Line', 'analyzed_text': analyzed}
        djtext = analyzed
        # analyze the text
        # return render(request,'analyze.html',params)
    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if (djtext[index] == " ") and (djtext[index + 1] == " "):
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose': 'Remove the extra space', 'analyzed_text': analyzed}



    if (removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover != "on"):
        return render(request,"error.html")

    return render(request, 'analyze.html', params)
