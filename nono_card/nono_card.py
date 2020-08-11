from selenium import webdriver  # brew cask でchromedriverのinstallが必要
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import datetime
import schedule
from pathlib import Path
from random import choice


class NotLoginError(Exception):
    pass


hands = [0, 1, 2]  # どのカードを引くか

print('start')

userdata_dir = Path('./userdata/')
if not userdata_dir.exists():
    userdata_dir.mkdir()

# クッキー情報取得
option = webdriver.ChromeOptions()
option.add_argument('--user-data-dir=' +
                    userdata_dir.as_posix())


def do_cardgame():
    print('played at', datetime.datetime.now())
    # cardgame画面へ
    driver = webdriver.Chrome(options=option)
    driver.get("https://p.eagate.573.jp/game/bemani/wbr2020/01/card.html")
    sleep(0.5)

    # 初回ログイン時処理
    if driver.find_element_by_tag_name('body').text.startswith('e-amusementサイトにログインしていません'):
        print('login and quit your blowser')
        print('please restart this program')
        raise NotLoginError

    # カードバトル
    try:
        cards = [driver.find_element_by_id('card0'),
                 driver.find_element_by_id('card1'),
                 driver.find_element_by_id('card2')]
        hand = choice(hands)  # 乱数で手を決める
        cards[hand].click()
        print('choiced', hand)
        sleep(0.5)
    except NoSuchElementException:
        print('already played')

    # ブラウザを終了
    driver.quit()


schedule.every().day.at('15:01').do(do_cardgame)
schedule.every().day.at('05:01').do(do_cardgame)

# 初回でわざとコケる
do_cardgame()
while True:
    schedule.run_pending()
    sleep(60 * 60)  # 1時間おきに実行可能かcheck
