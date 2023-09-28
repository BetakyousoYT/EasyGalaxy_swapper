import os
import sys
import time
import requests
import zipfile
import subprocess
from urllib.request import urlretrieve

output = subprocess.run(["dotnet", "--list-runtimes"], capture_output=True, text=True)
runtimes = output.stdout

if "Microsoft.WindowsDesktop.App 7.0.0" in runtimes:
    print("実行環境が構築されています。")
else:
    print(".Netをダウンロードします")
    url = "https://download.visualstudio.microsoft.com/download/pr/5b2fbe00-507e-450e-8b52-43ab052aadf2/79d54c3a19ce3fce314f2367cf4e3b21/windowsdesktop-runtime-7.0.0-win-x64.exe"
    filename = url.split("/")[-1]
    urlretrieve(url, filename)
    os.startfile(filename, "runas")
    sys.exit(0)

time.sleep(1)
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

print("ライセンスを発行します")
time.sleep(0.5)
print("何か文字を入れて取得")
input()

headers = {
    "Referer": "https://lootlinks.co/"
}
res = requests.get("https://galaxyswapperv2.com/Key/Create.php", headers=headers)
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
