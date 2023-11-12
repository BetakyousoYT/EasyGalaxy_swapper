import tempfile
import os
import subprocess
import threading
import requests
import webbrowser
import pygame
import subprocess
import threading
import requests
import os
import shutil
import textwrap


pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Easy Galaxy Swapper")
font = pygame.font.SysFont('meiryo', 24)
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color_button = pygame.Color('skyblue')
color_text = pygame.Color('white')

def wrap_text(message, max_width):
    words = message.split(' ')
    wrapped_lines = []
    current_line = ''

    for word in words:
        test_line = current_line + word + ' '
        w, h = font.size(test_line)

        if w <= max_width:
            current_line = test_line
        else:
            wrapped_lines.append(current_line)
            current_line = word + ' '

    wrapped_lines.append(current_line)
    return wrapped_lines


class Button:
    def __init__(self, text, x, y, w, h, action=None):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color_button
        self.text = text
        self.txt_surface = font.render(text, True, self.color)
        self.action = action

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                if self.action:
                    self.action()

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(screen, self.color, self.rect, 2)

log_area = pygame.Rect(266, 300, 534, 300)
log_messages = []

def add_log_message(message):
    wrapped_lines = wrap_text(message, 500)
    log_messages.extend(wrapped_lines)
    while len(log_messages) > 10:
        log_messages.pop(0)

def run_subprocess(command):
    return subprocess.run(command, capture_output=True, text=True)

def download_and_execute(url, file_name):
    try:
        with open(file_name, 'wb') as f:
            response = requests.get(url, stream=True)
            for chunk in response.iter_content(chunk_size=8192): 
                f.write(chunk)

        file_path = os.path.join(os.getcwd(), file_name)
        subprocess.Popen([file_path])
        add_log_message(f"{file_name} のダウンロードと実行が完了しました。")
    except Exception as e:
        add_log_message(f"エラーが発生しました: {e}")

def download_and_open_folder(url, file_name):
    try:
        net_folder = os.path.join(os.getcwd(), '.net')
        if not os.path.exists(net_folder):
            os.makedirs(net_folder)

        file_path = os.path.join(net_folder, file_name)
        with open(file_path, 'wb') as f:
            response = requests.get(url, stream=True)
            for chunk in response.iter_content(chunk_size=8192): 
                f.write(chunk)

        webbrowser.open(net_folder)
        add_log_message("ダウンロード完了")
        add_log_message("インストールを進めてください")
    except Exception as e:
        add_log_message(f"エラーが発生しました: {e}")

def check_dotnet():
    try:
        runtimes = run_subprocess(["dotnet", "--list-runtimes"]).stdout
        if "Microsoft.WindowsDesktop.App 7.0.0" in runtimes:
            add_log_message(".NET 7.0.0 がインストールされています。")
        else:
            add_log_message(".NET 7.0.0 がインストールされていません。")
    except FileNotFoundError:
        add_log_message("エラー: .NET がインストールされていません。")

def install_dotnet():
    threading.Thread(target=download_and_open_folder, args=(
        "https://download.visualstudio.microsoft.com/download/pr/5b2fbe00-507e-450e-8b52-43ab052aadf2/79d54c3a19ce3fce314f2367cf4e3b21/windowsdesktop-runtime-7.0.0-win-x64.exe",
        "dotnet_installer.exe"
    ), daemon=True).start()


def issue_license():
    global license_key
    headers = {"Referer": "https://lootlinks.co/"}
    res = requests.get("https://galaxyswapperv2.com/Key/Create.php", headers=headers)
    if res.ok:
        license_key = res.url.split("?key=")[1]
        pygame.scrap.init()
        pygame.scrap.put(pygame.SCRAP_TEXT, license_key.encode())
        add_log_message(f"ライセンスキー：{license_key}")
    else:
        add_log_message("エラー: ライセンスキーを取得できませんでした。")

license_key = None

def issue_license():
    global license_key
    headers = {"Referer": "https://lootlinks.co/"}
    res = requests.get("https://galaxyswapperv2.com/Key/Create.php", headers=headers)
    if res.ok:
        license_key = res.url.split("?key=")[1]
        pygame.scrap.init()
        pygame.scrap.put(pygame.SCRAP_TEXT, license_key.encode())
        add_log_message(f"ライセンスキー：{license_key}")
    else:
        add_log_message("エラー: ライセンスキーを取得できませんでした。")

def copy_to_clipboard():
    global license_key
    if not license_key:
        issue_license()
    if license_key:
        pygame.scrap.init()
        pygame.scrap.put(pygame.SCRAP_TEXT, license_key.encode())
        add_log_message("ライセンスキーをコピーしました。")
    else:
        add_log_message("エラー: ライセンスキーのコピーに失敗しました。")


def download_galaxy_swapper():
    threading.Thread(target=download_and_execute, args=(
        "https://galaxyswapperv2.com/Downloads/Galaxy%20Swapper%20v2.exe",
        "Galaxy_Swapper_v2.exe",
    ), daemon=True).start()


def launch_galaxy_swapper():
    galaxy_swapper_path = os.path.join(os.getcwd(), "Galaxy_Swapper_v2.exe")

    if os.path.exists(galaxy_swapper_path):
        subprocess.Popen([galaxy_swapper_path])
        add_log_message("Galaxy Swapper v2 を起動しました。")
    else:
        add_log_message("エラー: Galaxy Swapper v2 が見つかりません。")



def reset_config():
    config_path = os.path.join(os.getenv('LOCALAPPDATA'), 'Galaxy-Swapper-v2-Config')
    if os.path.exists(config_path):
        shutil.rmtree(config_path)
        add_log_message("設定がリセットされました。")
    else:
        add_log_message("設定フォルダが見つかりません。")

def show_credits():
    add_log_message("ライセンスとかでウィルス感染する人多いので")
    add_log_message("ツールを作りましたが、使いにくかったため")
    add_log_message("色々作り直しました")
    add_log_message("Galaxy swapper公式鯖は以下です")
    add_log_message("https://discord.gg/fortniteswapper")
button_dotnet = Button(".Net", 20, 50, 180, 50, lambda: set_active_toolbox('dotnet'))
button_license = Button("ライセンスキー", 20, 120, 180, 50, lambda: set_active_toolbox('license'))
button_swapper = Button("Galaxy Swapper", 20, 190, 180, 50, lambda: set_active_toolbox('swapper'))
button_credits = Button("クレジット", 20, 260, 180, 50, show_credits)

toolbox_area = pygame.Rect(266, 0, 534, 300)
active_toolbox = None
toolbox_buttons = {
    'dotnet': [
        Button("インストールの確認", 276, 10, 504, 50, check_dotnet),
        Button("インストール", 276, 70, 504, 50, install_dotnet)
    ],
    'license': [
        Button("ライセンスキーの発行", 276, 10, 504, 50, issue_license),
        Button("コピー", 276, 70, 504, 50, copy_to_clipboard)
    ],
    'swapper': [
        Button("ダウンロード", 276, 10, 504, 50, download_galaxy_swapper),
        Button("起動", 276, 70, 504, 50, launch_galaxy_swapper),
        Button("リセット", 276, 130, 504, 50, reset_config)
    ]
}

def set_active_toolbox(toolbox):
    global active_toolbox
    active_toolbox = toolbox

def copy_to_clipboard(text):
    pygame.scrap.init()
    pygame.scrap.put(pygame.SCRAP_TEXT, text.encode())

running = True
while running:
    screen.fill((30, 30, 30))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        button_dotnet.handle_event(event)
        button_license.handle_event(event)
        button_swapper.handle_event(event)
        button_credits.handle_event(event)
        if active_toolbox:
            for button in toolbox_buttons[active_toolbox]:
                button.handle_event(event)

    button_dotnet.draw(screen)
    button_license.draw(screen)
    button_swapper.draw(screen)
    button_credits.draw(screen)
    if active_toolbox:
        for button in toolbox_buttons[active_toolbox]:
            button.draw(screen)

    pygame.draw.rect(screen, (0, 255, 0), (0, 0, 266, 600), 2)
    pygame.draw.rect(screen, (0, 255, 0), (266, 0, 534, 300), 2)
    pygame.draw.rect(screen, (0, 255, 0), log_area, 2)
    pygame.draw.rect(screen, (255, 255, 0), log_area.inflate(4, 4), 2)

    for i, message in enumerate(log_messages):
        text_surface = font.render(message, True, color_text)
        screen.blit(text_surface, (log_area.x + 5, log_area.y + 5 + i * 30))

    pygame.display.flip()

pygame.quit()
