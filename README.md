# selenium test
## Description
WSL2上からのseleniumのテスト

## Features

## Requirement

## Usage
```
python3.9.5
Google Chrome 98.0.4758.80
ChromeDriver 98.0.4758.48
```

## Installation Methid
### install google-chrome
```
$ cd /tmp
$ wget https://dl.google.com/linux/linux_signing_key.pub
$ sudo apt-key add linux_signing_key.pub
$ echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' | sudo tee /etc/apt/sources.list.d/google-chrome.list
$ sudo apt-get update
$ sudo apt -f install -y
$ sudo apt-get install google-chrome-stable
$ google-chrome --version
Google Chrome 98.0.4758.80
```
### install chromedriver
```
$ cd /tmp
$ wget https://chromedriver.storage.googleapis.com/98.0.4758.48/chromedriver_linux64.zip
$ sudo apt install unzip -y
$ unzip chromedriver_linux64.zip
$ sudo mv chromedriver /usr/bin/chromedriver
$ chromedriver -v
ChromeDriver 98.0.4758.48
```

## Development

## Author
otesii