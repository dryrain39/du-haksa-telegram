import datetime
import logging
import os
import time
import telegram

from DU.Config import get_config
import json

from DU.DUParser import du_get_list, du_content_parser
from DU.telegram import send_telegram

logging.basicConfig(
    level=logging.INFO,
)
rootLogger = logging.getLogger()
logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
fileHandler = logging.FileHandler("{0}/{1}.log".format(".", datetime.datetime.now().strftime("%Y-%m-%d")),
                                  encoding="utf-8")
fileHandler.setFormatter(logFormatter)
rootLogger.addHandler(fileHandler)

consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
rootLogger.addHandler(consoleHandler)


def work(config, element, keyword):
    try:
        url = "https://www.daegu.ac.kr/article/DG159/detail/" + element[0]

        r = du_content_parser(url)
        logging.info(element[1] + " 데이터를 가져왔습니다.")

        telegram_subject = r.title
        telegram_url = f"{url}"

        if keyword not in r.title:
            return

        send_telegram(config, telegram_subject, telegram_url)
        logging.info(element[1] + " 데이터를 보냈습니다.")
    except Exception as e:
        logging.error(e)
    pass


def main(keyword):
    config = get_config()
    memory = []

    memory_max = config["store_cnt"]
    no_get_page = config["no_get_page"]

    if os.path.exists("./memory.json"):
        memory = json.load(open("memory.json", 'r', encoding="utf-8"))
        logging.info("json 로드 성공...")

    for x in range(1, no_get_page + 1):
        current_list = du_get_list(x)

        for e in current_list:
            if e not in memory:
                if not config["first_run"]:
                    work(config, e, keyword)
                    logging.info(str(x) + " 완료 3초 대기...")
                    time.sleep(3)
                memory.append(e)

        logging.info(str(x) + " 페이지 완료 10초 대기...")
        time.sleep(10)

    if len(memory) > memory_max:
        memory = memory[len(memory) - memory_max:]
        logging.info("memory.json을 정리했습니다.")

    logging.info("memory.json 덤프 중...")
    json.dump(memory, open("memory.json", "w", encoding="utf-8"), ensure_ascii=False)

    logging.info("끝났습니다.")


if __name__ == '__main__':
    while True:
        keyword = input("키워드를 입력하세요")
        main(keyword)
        time.sleep(60)
