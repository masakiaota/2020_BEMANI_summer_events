An automation tool for [いちかのBEMANI超じゃんけん大会2020](https://p.eagate.573.jp/game/bemani/bjm2020/)
===

![](ichika_jannkenn.gif)

- [An automation tool for いちかのBEMANI超じゃんけん大会2020](#an-automation-tool-for-いちかのbemani超じゃんけん大会2020)
    - [動作確認環境](#動作確認環境)
    - [requirements](#requirements)
    - [How to install](#how-to-install)
      - [1. まずgoogle chromeをインストールしてください。(すでに入っている方はこの必要がありません。)](#1-まずgoogle-chromeをインストールしてくださいすでに入っている方はこの必要がありません)
      - [2. chromedriverをインストールしてください(shellから叩けるようにしてください)。](#2-chromedriverをインストールしてくださいshellから叩けるようにしてください)
        - [macの方](#macの方)
        - [ubuntuの方](#ubuntuの方)
      - [3. python3.xをインストールしてください(すでに入っている方は必要ありません)。](#3-python3xをインストールしてくださいすでに入っている方は必要ありません)
        - [macの方](#macの方-1)
        - [ubuntuの方](#ubuntuの方-1)
      - [4. 必要なPython moduleをインストールします。](#4-必要なpython-moduleをインストールします)
    - [How to use](#how-to-use)

### 動作確認環境
macOS Sierra (10.12.6)

### requirements
- Python 3.x
  - selenium
  - schedule
- google chrome
- chromedriver

### How to install
以下macとubuntuにインストールする方法を記載します。(windowsに関してはpull requestを待ってます)

#### 1. まずgoogle chromeをインストールしてください。(すでに入っている方はこの必要がありません。)

リンク → https://www.google.co.jp/intl/ja/chrome/

#### 2. chromedriverをインストールしてください(shellから叩けるようにしてください)。

##### macの方
例えば`brew cask install chromedriver`のコマンドを実行します。
homebrewがインストールされていない方は[こちらのサイト](https://brew.sh/)のInstall Homebrewを実行してください。

##### ubuntuの方
例えば`apt-get install chromedriver`のコマンドを実行します。

#### 3. python3.xをインストールしてください(すでに入っている方は必要ありません)。

##### macの方
例えば`brew install python3`のコマンドを実行します

##### ubuntuの方
例えば`apt-get install python3`のコマンドを実行します


#### 4. 必要なPython moduleをインストールします。
`pip3 install selenium schedule`


### How to use
`python3 auto_jannkenn.py` を実行してひたすら待つだけです。

初回に限って、ログイン画面でわざとエラー終了するようにしてあります。ログインしてからchromeを完全終了して、もう一度コマンドの実行をお願いします。

なお、ここで入力されたログイン情報が記録および収集されることはありません。

