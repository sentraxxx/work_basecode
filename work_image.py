import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
import requests
from bs4 import BeautifulSoup
import warnings

## アクセスURL
URL = 'https://photos.app.goo.gl/mzgck3Kbw2eaXBwEA'
FILE_NAME = 'img.jpg'

## SSL warning無効化
warnings.simplefilter(
    'ignore', requests.urllib3.exceptions.InsecureRequestWarning)            

res_imgweb = requests.get(URL, verify=False)
bf_top = BeautifulSoup(res_imgweb.text, 'html.parser')

## イメージsrc url取得
imgsrc = ''
imglist = bf_top.select('img')
for i in imglist:
    print(i)
    imgsrc = i['src']
    print(imgsrc)

## ファイル取得
res_img = requests.get(imgsrc,verify=False, stream=True)
print(res_img.headers['Content-Type'])
if res_img.status_code == 200:
    with open(FILE_NAME, 'wb') as f:
        f.write(res_img.content)

    ## イメージ出力
    img = mpimg.imread(f)
    imgplot = plt.imshow(img)
