# Counter PoC

## 概要
Django 5.2.5 を使用した最小限のカウンターアプリのPoCです。  
ボタンを押すとカウントが1ずつ増加し、セッションで値を保持します。  
学習目的で作成した超小型PoCです。

## 技術スタック
- Python 3.12
- Django 5.2.5
- HTML (テンプレート)
- セッション管理
- 開発環境: Windows11 + WSL(Ubuntu)

## インストール方法
1. 仮想環境を作成・有効化
```bash
python -m venv venv
source venv/bin/activate
```
2. 依存パッケージをインストール
```bash
pip install --upgrade pip
pip install django
```
3. データベースマイグレーション
```bash
python manage.py migrate
```
4. 開発サーバー起動
```bash
python manage.py runserver
```
5. ブラウザでアクセス
```
http://127.0.0.1:8000/
```

## 使い方
- 「カウントアップ」ボタンを押すとカウントが1ずつ増えます  
- ページをリロードしてもセッションでカウントが保持されます

## テスト実行
```bash
python manage.py test counter_app
# → カウントアップ動作を確認できます
```

## デモ
- 動作GIFやWebMをここに追加可能
```markdown
![Demo](https://github.com/ShigeoYugawa/counter-poc/blob/main/assets/demo.gif?raw=true)
```

## 注意
- 開発用PoCであり、本番環境用ではありません  
- CSRFトークンを使用していますが、本番向けのセキュリティ設定は含まれていません

## ライセンス
- 個人学習用 / 無償公開
