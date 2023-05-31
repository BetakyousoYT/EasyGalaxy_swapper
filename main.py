import os
import sys
import requests
import time
from urllib.request import urlretrieve

download_url = "https://galaxyswapperv2.com/Downloads/Galaxy%20Swapper%20v2.exe"
local_file_path = "Galaxy_Swapper_v2.exe"
print("製作者が改悪しまくったり、ダウンロードページを曖昧にしたりするので")
time.sleep(0.5)
print("β教祖がクライアントを作成しました")
time.sleep(0.5)
print("Galaxy swapperをダウンロードしています")
urlretrieve(download_url, local_file_path)
print("ダウンロード終了！")
time.sleep(0.5)
print("起動します")

os.startfile(local_file_path)

input("起動が出来たら何か文字を入力してください：")

print("ライセンスを発行します")
time.sleep(0.5)
print("何か文字を入れて取得")
input()

res = requests.get("https://galaxyswapperv2.com/Key/Create.php")
license_key = res.url.split("?key=")[1] if res.ok else None
print("ライセンスキーは：" + license_key) if license_key else print("ライセンスキーの取得時に問題が発生しました")

print("Galaxy swapperを楽しんでください！")
time.sleep(0.5)
print("https://galaxyswapperv2.com/Discord.php")
time.sleep(0.5)
print("↑ここは一応公式のDiscordです。ダウンロードページにたまにウィルスあるので")
time.sleep(0.5)
print("サポート以外は非推奨ですが、貼ります(製作者には敬意を持ちましょう。)")

while True:
    print("エンターを押すと終了します")
    exit_input = input()
    if exit_input == "":
        sys.exit(0)
