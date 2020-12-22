# line_notify_util
utils for line notify<br>
<br>
<img src="https://raw.githubusercontent.com/matyalatte/line_notify_util/main/image.png" width="320px"><br>
LINE Notify でメッセージを送るためのスクリプトです。<br>
スクリプトの実行状況等を通知するために作成しました。<br>
テキストの送信のみに対応(pythonは画像の送信にも対応)したシンプルなスクリプトとなっています。<br>
<br>
※SlackのIncoming webhookでも同様の通知が行えます。Slack用のスクリプトは<a href="https://github.com/matyalatte/slack_webhook_util">こちら</a><br>

## ファイル一覧
- line_notify.py: python用のスクリプト。LineNotify("トークン").notify("文字列")でメッセージを送れる。
- line_notify.gs: GAS用のスクリプト。line_notify("文字列")でメッセージを送れる。ACCESS_TOKENにアクセストークンを記入して使う。
- line_notify.bat: curlでLINE Notifyのメッセージを送る
- test.png: 画像送信テスト用のテスト画像

## LINE Notifyの使い方について
アクセストークン発行等のLINE Notifyの使い方については以下のサイトを参考にしてください。<br>
<a href="https://qiita.com/iitenkida7/items/576a8226ba6584864d95">
[超簡単]LINE notify を使ってみる - Qiita
</a>
