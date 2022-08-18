from django.shortcuts import render
from django.contrib import messages
import language_check
from textblob import TextBlob
from django.shortcuts import redirect
from design.models import Testimonial
from design.models import Gallary
from django.urls import reverse

# Create your views here.
testimonials = Testimonial.objects.all()
pic = Gallary.objects.all()

def check(request):
    text = request.POST.get('text_to_edit',False)
    threshold= len(text)
    x=text.count(" ")
    if x<3:
        messages.warning(request, "Please enter a sentence with more than 3 words! ")
        return redirect('/')

    if x>10:
        t= text.split()
        s= t[0]+" "+t[1]+" "+t[2]+" "+t[3]+" "+t[4]+" "+t[5]+" "+t[6]+" "+t[7]+" "+t[8]
    else:
        s= text
        
    print (s)
    b = TextBlob(s)
    
    if b.detect_language() == 'en':
        
        
        tool = language_check.LanguageTool('en-US')
        matches = tool.check(text)
        l=len(matches)
        i=0
        for mistakes in matches:
            messages.error(request, "error at: %s" % mistakes )
            matches = tool.check(text)
            text_correct = language_check.correct(text, matches)
            

        testimonials = Testimonial.objects.all()
        pic = Gallary.objects.all()
        return render(request, 'correction.html', context={'testimonials': testimonials, 'pic':pic, 'correct_text': text_correct})     
    else:
        messages.error(request, "The language is not english")
        return redirect ('/')



