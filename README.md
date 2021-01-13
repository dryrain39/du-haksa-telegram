# du-haksa-telegram

DU Notification to telegram

학사공지를 텔레그램으로 받아 볼 수 있습니다.

## 요구사항

1. python 3.8 (3.8.5 에서 테스트됨)
2. `pip3 install beautifulsoup4 htmlmin requests python-telegram-bot`
3. telegram 전송을 위한 봇

## 세팅

1. config.json 의 first_run 을 true 로 세팅한 뒤 스크립트를 1회 동작시키십시오.
2. config.json 의 first_run 을 false 로 세팅하고 메일 계정 정보를 입력하십시오.
3. 서버에 스크립트를 계속 켜 두면 됩니다. 60초마다 자동으로 데이터를 가져옵니다.

## config.json
```json
{
  "account": {
    "chatID": "챗 아이디 작성",
    "token": "봇 API 기입"
  },
  "store_cnt": 100,
  "no_get_page": 5,
  "first_run": false
}
```
