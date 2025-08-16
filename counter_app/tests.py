# counter_app/tests.py

from django.test import TestCase


class CounterViewTests(TestCase):
    """
    カウンター動作テスト
    """

    def test_counter_increments(self) -> None:
        # 初回アクセス → カウント0
        response = self.client.get('/')
        self.assertContains(response, '現在のカウント: 0')

        # POSTでカウントアップ → 1
        response = self.client.post('/')
        self.assertContains(response, '現在のカウント: 1')

        # さらにPOST → 2
        response = self.client.post('/')
        self.assertContains(response, '現在のカウント: 2')
