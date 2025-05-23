from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Message
import json
from datetime import datetime

@csrf_exempt
def save_message(request):
    if request.method == 'POST':
        try:
            body = json.loads(request.body)

            date_str = body.get('date')    
            time_str = body.get('time')    
            content = body.get('message')

            if not date_str or not time_str or not content:
                return JsonResponse({'error': 'date, time, and message are required.'}, status=400)

            try:
                date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()
                time_obj = datetime.strptime(time_str, "%H:%M:%S").time()
            except ValueError:
                return JsonResponse({'error': 'Invalid date or time format. Use YYYY-MM-DD and HH:MM:SS.'}, status=400)

            message = Message.objects.create(date=date_obj, time=time_obj, content=content)

            return JsonResponse({'success': True, 'id': message.id}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON.'}, status=400)

    return JsonResponse({'error': 'Only POST method allowed.'}, status=405)
