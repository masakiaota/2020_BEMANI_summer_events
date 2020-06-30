from selenium import webdriver  # brew cask でchromedriverのinstallが必要
from time import sleep
import datetime
import schedule
from pathlib import Path
from random import choice
hands = [0, 1, 2]  # グーチョキパー

print('start')

userdata_dir = Path('./userdata/')
if not userdata_dir.exists():
    userdata_dir.mkdir()

# クッキー情報取得
option = webdriver.ChromeOptions()
option.add_argument('--user-data-dir=' +
                    userdata_dir.as_posix())


def do_jannkenn():
    print('じゃんけんed at', datetime.datetime.now())
    # じゃんけん画面へ
    driver = webdriver.Chrome(options=option)
    driver.get("https://p.eagate.573.jp/game/bemani/bjm2020/janken/index.html")
    sleep(0.5)
    # じゃんけん済みだったらなにもせず次の回まで待機
    is_done = driver.find_element_by_id('janken')\
        .get_attribute('innerHTML')\
        .count('じゃんけん済み')
    if not is_done:
        element_janken_select = driver.find_element_by_id('janken-select')\
            .find_elements_by_tag_name('a')
        # じゃんけんする
        hand = choice(hands)  # 乱数で手を決める
        element_janken_select[hand].click()
        sleep(0.5)
    # ブラウザを終了
    driver.quit()


schedule.every().day.at('10:05').do(do_jannkenn)
schedule.every().day.at('15:05').do(do_jannkenn)
schedule.every().day.at('20:05').do(do_jannkenn)
# 初回でわざとコケる
do_jannkenn()
while True:
    schedule.run_pending()
    sleep(60 * 10)  # 10分おきに実行可能かcheck
