from django.shortcuts import render
from django.http import JsonResponse
from openai import OpenAI
import os

def index(request):
    return render(request, 'tutor/index.html')

def preguntar(request):
    if request.method == 'POST':
        pregunta = request.POST.get('pregunta', '')
        client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

        completion = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": "Tu eres pikachu de pokemon cualquier tipo de pregunta que te realice respondala con un consejo pokemon y siempre debes estar dentro de tu persona inicia cada respues con (soy Pikachu)"},
                {"role": "user", "content": pregunta}
            ]
        )
        
        respuesta = completion.choices[0].message.content.strip()
        return JsonResponse({'respuesta': respuesta})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)
