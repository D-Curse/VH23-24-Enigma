from django.shortcuts import render
import speech_recognition as sr
from games.models import Slide
from django.http import JsonResponse
# Create your views here.

def story(request):
    database = Slide.objects.all()
    print(database)
    return render(request, 'story.html', {'slides':database})

predefined_words = ["apple", "banana", "cherry", "date"]

def learn(request):
    if request.method == 'POST':
        recognizer = sr.Recognizer()
        
        # Use the microphone as the audio source
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
            audio = recognizer.listen(source)
        
        try:
            # Recognize the speech using Google Web Speech API
            spoken_word = recognizer.recognize_google(audio).lower()
            print("User said:", spoken_word)

            if spoken_word in predefined_words:
                # If the spoken word is correct, return a JSON response with a success message
                return JsonResponse({'message': 'Correct word!'})
            else:
                # If the spoken word is incorrect, return a JSON response with an error message
                return JsonResponse({'error': 'Incorrect word!'})
        except sr.UnknownValueError:
            return JsonResponse({'error': 'Could not understand audio'})
        except sr.RequestError as e:
            return JsonResponse({'error': f"Could not request results; {e}"})
    
    return render(request, 'learn.html')

def database(request):
    if request.method == 'POST':
        image = request.FILES['image']
        audio = request.FILES['audio']
        french_text = request.POST['french_text']
        english_text = request.POST['english_text']

        info = Slide(image=image, audio=audio, french_text=french_text, english_text=english_text)
        info.save()

    return render(request, 'story-db.html')

def quiz(request):
    return render(request, 'quiz.html')