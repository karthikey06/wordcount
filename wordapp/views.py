from django.http import HttpResponse
from django.shortcuts import render
import operator
def homepage(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')

def count(request):
    data=request.GET['fulltextarea']
    print(data)
    word_list=data.split()
    print(word_list)
    list_len=len(word_list)
    print(list_len)
    worddictionary={}

    for word in word_list:
        if  word in worddictionary:
            worddictionary[word] +=1
            #increase value by 1

        else:
            worddictionary[word] =1
    sort=sorted(worddictionary.items(),key=operator.itemgetter(1),reverse=True)

    return render(request,'count.html',{'fulltext':data, 'words':list_len,'worddictionary':sort})