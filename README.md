# du-haksa-telegram

대구대학교 학사공지 알림 봇
[DU Notification to telegram](https://t.me/sw_dev)

대구대학교 학사공지를 [텔레그램](https://t.me/sw_dev)으로 받아 볼 수 있습니다.
이 프로젝트 코드의 일부는 아래 프로젝트에 코드를 참고하여 제작되었습니다.

참고한 프로젝트 : [du-n2m](https://github.com/dryrain39/du-n2m)

## 요구사항

1. python 3.8 (3.8.5 에서 테스트됨)
2. `pip3 install beautifulsoup4 htmlmin requests python-telegram-bot`
3. telegram 전송을 위한 봇

## 세팅

1. config.json 의 first_run 을 true 로 세팅한 뒤 스크립트를 1회 동작시키십시오.
2. config.json 의 first_run 을 false 로 세팅하고 텔레그램 계정 정보를 입력하십시오.
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
