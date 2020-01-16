import matplotlib.pyplot as plt
from PIL import Image
import requests
from bs4 import BeautifulSoup
import warnings
import re

##########################################################
# Google photo link アクセスURL (javascriptを含むページ)
GOOGLE_PHOTO_LINK = 'https://photos.app.goo.gl/FcCsB7iE1Fmjh93Z7'

#  保存先ファイル名
SAVE_FILE_NAME = './files/img.jpg'


def getImgSrcFromGooglePhoto(url):
    """google photoのLinkページから画像のsrc urlを取得する
    
    Arguments:
        url {[string]]} -- [google photoのLink]
    
    Returns:
        [string] -- [画像srcのurl]
    """    
    # SSL warning無効化
    warnings.simplefilter(
        'ignore', requests.urllib3.exceptions.InsecureRequestWarning)

    # google photoリンクページアクセス
    res_imgweb = requests.get(url, verify=False)
    bf_top = BeautifulSoup(res_imgweb.text, 'html.parser')

    # イメージsrc url取得
    imgsrc = ''
    imglist = bf_top.select('script')
    print(f'imglist len= ', len(imglist))
    for id, img in enumerate(imglist):
        match = re.search(r'https:\/\/[^"]*', img.string, re.S)
        # print('<script> id= ', id, ': ', img.string[0:30])
        # print('<script> id= ', id, ': ', match.group() if match else "no match")
        if match:
            imgsrc = match.group(0)

    return imgsrc


def showimg(src, file_name):
    # ファイル取得&保存
    res_img = requests.get(src, verify=False, stream=True)
    print(res_img.headers['Content-Type'])
    if res_img.status_code == 200:
        with open(file_name, 'wb') as f:
            f.write(res_img.content)

    # イメージ出力(表示)
    img = plt.imread(file_name)
    plt.imshow(img)
    plt.show()


# main
imgsrc = getImgSrcFromGooglePhoto(GOOGLE_PHOTO_LINK)
showimg(imgsrc, SAVE_FILE_NAME)
