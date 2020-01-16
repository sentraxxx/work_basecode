import requests
from bs4 import BeautifulSoup
import warnings

## SSL warning無効化
warnings.simplefilter(
    'ignore', requests.urllib3.exceptions.InsecureRequestWarning)

URL = 'https://google.com'
res = requests.get(URL, verify = False)
soup = BeautifulSoup(res.text, 'html.parser')

print('***********************\n')

# 構成を知っていれば直接子要素にアクセス soup."タグ" 
print('soup.head.meta= ', soup.head.meta)
print('***********************\n')


# タグ指定全検索 soup.find_all('div')
print('soup.find_all(div)の要素数= ', len(soup.find_all('div')), '\n  2番目= ', soup.find_all('div')[1])
print('***********************\n')

# 1件検索 soup.find('li') 

# 属性検索 soup.find('li', href="html://www.google.com/") 

# class検索 soup.find('a', class_="first") 
# classは予約語なので　"_"付加

# 属性取得 first_link_element['href']
 
# テキストへのアクセスは要素 first_link_element.string 

# 親要素 first_link_element.parent 

# タグ名を全部検索
for tag in soup.find_all(True):
    print(tag.name)

# select : 指定したタグを含むリスト
title = soup.select('title')
print('--- select <title> ---')
print('title = ', title)
print('title type= ', type(title))
print('title[0] type= ', type(title[0]))
print('title.txt = ', title[0].text)
print('***********************\n')

# select : 指定タグを含むリストへのアクセス
links = soup.select('a')
print('--- select <a> ---')
print('<a>リスト要素数 = ', len(links))
print('<a>[0]番目= ', links[0])
print('<a>[0]番目の href= ', links[0]['href'])
print('***********************\n')

