# counter_app/views.py

from django.shortcuts import render
from django.http import HttpRequest


def counter_view(request: HttpRequest) -> HttpRequest:
    """
    セッションからカウント値を取得し、ボタン押下時に1ずつ増加させるビュー。

    - GETリクエスト: 現在のカウントを表示
    - POSTリクエスト: カウントを1増やして再表示
    """
    
    count: int = request.session.get('count', 0)

    if request.method == 'POST':
        count += 1
        request.session['count'] = count

    return render(request, 'counter_app/counter.html', {'count':count})