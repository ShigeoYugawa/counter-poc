# counter_app/views.py

from django.shortcuts import render
from django.http import HttpRequest


def counter_view(request: HttpRequest) -> HttpRequest:
    """
    セッションから値を取得してカウントする
    """
    
    count: int = request.session.get('count', 0)

    if request.method == 'POST':
        count += 1
        request.session['count'] = count

    return render(request, 'counter_app/counter.html', {'count':count})