from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request,'home.html', {'name' : 'Word Count'})

def Count(request):
    name = request.GET['textarea']
    wordlist = name.split()
    worddictionary = {}
    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] +=1
        else :
            worddictionary[word] = 1
    print(len(name))
    print(worddictionary)
    return render(request , 'count.html' ,{'textarea': name,  'worddictionary' : worddictionary})

def About(request):
    return render(request , 'about.html')

