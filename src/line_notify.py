import requests

class LineNotify:
    URL='https://notify-api.line.me/api/notify'

    def __init__(self, access_token):
        self.header = {'Authorization': 'Bearer ' + access_token}

    def notify(self, message, image=None):
        if message=="" or (type(message) is not str):
            raise ValueError("'message' should be a string of more than one character!")

        payload = {
            'message': message,
        }

        file = {}
        if image is not None:
            file = {'imageFile': open(image, 'rb')}

        r = requests.post(LineNotify.URL, headers=self.header, data=payload, files=file)

#テスト用
if __name__=="__main__":
    access_token="ここにアクセストークンを記入する"

    line_notify=LineNotify(access_token)

    line_notify.notify("テストだよ")
    line_notify.notify("テスト画像だよ", image="../img/test.png")

        