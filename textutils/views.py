# I have created this file - siddharth
from django.http import HttpResponse
from django.shortcuts import render

#code for video textutils no6
# def index(request):
#      return HttpResponse('''<h1>Siddharth</h1> <a href="https://www.youtube.com/watch?v=5BDgKJFZMl8&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9">Django codewith harry</a>
#      <h1>Siddharth</h1> <a href="https://www.w3schools.com/python/default.asp"> W3school python </a>''')
#
# def about(request):
#     return HttpResponse(" About Hello Siddharth this is my first Django website")




# def index(request):
#     with open("C:\\Users\\SIDDHARTH\\PycharmProjects\\textutils\\textutils\\textutils\\1.txt") as f:
#         a = f.read()
#         return HttpResponse(a)                  #exercise purpose

#code for video 7

def index(request):
    #params = {'name':'siddharth','place':'mars'}
    return render(request,'index.html')
    #return HttpResponse("Home")

# def ex1(request):
#     sites = ['''<h1>For Entertainment </h1><a href = "https://www.youtube.com" >youtube video</a>''',
#              '''<h1>For Interaction </h1><a href = "https://www.facebook.com" >Facebook</a>''',
#              '''<h1>For Insight   </h1><a href = "https://www.ted.com/talks" >Ted Talk</a>''',
#              '''<h1>For Internship   </h1><a href="https://internshala.com" >Intenship</a>''',
#              ]
#     return HttpResponse((sites))
def analyze(request):
    #Get the text
    djtext = request.POST.get('text','default')

    # check checkbox value
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    # print(removepunc)
    # print(djtext)
    # analyzed = djtext

    #check if checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': "Removing Punctuations", 'analyzed_text': analyzed}
        djtext = analyzed
    #Analyze the text
        # return render(request,'analyze.html',params)
    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)



    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if (charcount == 'on'):
        analysed = ""
        i = 0
        for char in djtext:
            i = i + 1

        analysed = i
        params = {'purpose': 'New Line Remove', 'analyzed_text': analysed}
        # djtext = analyzed
        # return render(request, 'analyze.html', params)

    if (removepunc != "on" and newlineremover != "on" and extraspaceremover != "on" and fullcaps != "on" and charcount != 'on'):
        return HttpResponse("please select any operation and try again")
    # else:
    #     return HttpResponse('Error')
    return render(request, 'analyze.html', params)

# def capfirst(request):
#     return HttpResponse("capitalize first")
#
# def newlineremove(request):
#     return HttpResponse("Newlineremove")
#
# def spaceremove(request):
#     return HttpResponse("space remover")
#
# def charcount(request):
#     return HttpResponse('''charcount <a href="/">go back to home page</a>''')

