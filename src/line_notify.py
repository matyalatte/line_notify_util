#line_notify.py
#2020/12/23 updated by matyalatte

from pathlib import Path
import requests

class LineNotify:
    '''
    Sends message and image via LineNotify.
    Args:
        access_token (str): Access token for LINE notify.
        verbose (bool): Whether LineNotify print its status or not.
            Optional. Defaults to True.
    '''

    URL='https://notify-api.line.me/api/notify'

    def __init__(self, access_token, verbose=True):
        self.token = access_token
        self.verbose = verbose

        self.header = {'Authorization': 'Bearer ' + self.token}

        if self.verbose:
            print("LineNotify: Setup completed")

    def notify(self, message, img_path=None, sticker_package_id=None, sticker_id=None ,notification=True):
        '''
        Sends message and image via LineNotify.
        
        Args:
            message (str): Message you want to send. 1000 characters max.
            img_path (str or pathlib.Path): Path to image you want to send.
                Supported image format is png and jpeg.
                Optional. Defaults to None.
            sticker_package_id (int): Package ID of sticker.
                Optional. Defaults to None.
                if you want to send stickers, see sitcker list (https://devdocs.line.me/files/sticker_list.pdf).
            sticker_id (int): Sticker ID.
                Optional. Defaults to None.
            notification (bool): Whether LineNotify send a push notification to users.
                Optional. Defaults to True.

        Returns:
            r (requests.models.Response): Output of requests.post()
        '''
        
        #check args
        if message=="" or not isinstance(message, str):
            raise ValueError("'message' should be a string of more than one character!")

        if img_path:
            if isinstance(img_path, str):
                img_path=Path(img_path)
            if not isinstance(img_path, Path):
                raise TypeError("img_path should be str or pathlib.Path.")

            if not Path.exists(img_path):
                raise ValueError("{} does NOT exist.".format(img_path))

            suf=img_path.suffix
            if not suf:
                raise ValueError("img_path should be image path. But the input was directory.")
            if not (suf in ['.png', '.jpg', '.jpeg']):
                raise ValueError("image format should be png or jpg.")

        if sticker_package_id:
            if not isinstance(sticker_package_id, int):
                raise TypeError("sticker_package_id should be int.")

        if sticker_id:
            if not isinstance(sticker_id, int):
                raise TypeError("sticker_id should be int.")

        if (sticker_package_id is None) ^ (sticker_id is None):
            raise ValueError("you missed sticker_package_id or sticker_id.")
        #check completed

        #send message
        payload = {
            'message': message,
            'stickerPackageId': sticker_package_id,
            'stickerId': sticker_id,
            'notificationDisabled': not notification,
        }

        file = {}
        if img_path:
            img = open(img_path, 'rb')
            file = {'imageFile': img}

        r = requests.post(LineNotify.URL, headers=self.header, data=payload, files=file)

        if img_path:
            img.close()
        #send completed

        #logging
        if self.verbose:
            sc = r.status_code
            print("LineNotify: Sending a messsage... ", end="")
            if sc==200:
                print("Success!")
            else:
                print("Failed! (status:{})".format(sc))
                if sc==400:
                    print("            Bad request.")
                elif sc==401:
                    print("            Invalid access token. Check your access token.")
                elif sc==404:
                    print("            '{}' was Not Found.".format(self.URL))
                elif sc==500:
                    print("            Failure due to server error.")

        return r

#テスト用
if __name__=="__main__":
    access_token=""

    line_notify=LineNotify(access_token)

    line_notify.notify("pythonのスクリプトを実行したよ", notification=False)
    line_notify.notify("スタンプだよ", sticker_package_id=1, sticker_id=1)
    line_notify.notify("テスト画像だよ", img_path="../img/test.png")

        