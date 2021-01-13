import logging
import re

import requests
import htmlmin
from bs4 import BeautifulSoup


class ParserResult:
    def __init__(self, success=False, title="", html="", text="", error=None):
        self.success = success
        self.html = html
        self.title = title
        self.text = text
        self.error = error


def du_content_parser(url):
    try:
        r = requests.get(url)
        logging.info(url + " 데이터를 가져옵니다...")

        bs = BeautifulSoup(r.text, 'html.parser')

        content = bs.find("td", class_="contentArea")

        output_html = htmlmin.minify(str(content))
        output_content = ""
        title = bs.find("th", class_="view_title").text
    
        return ParserResult(
            success=True,
            title=title,
            html=output_html,
            text=output_content
        )
    except Exception as e:
        logging.error(e)
        return ParserResult(success=False, error=e)


def du_get_list(page=1):
    try:
        r = requests.get(f"https://www.daegu.ac.kr/article/DG159/list?pageIndex={page}&searchCondition=TA.SUBJECT")
        bs = BeautifulSoup(r.text, 'html.parser')

        article_list = []

        for x in bs.find_all("a"):
            if "onclick" in x.attrs and "goDetail" in x["onclick"]:
                current_article_number = x["onclick"].split("(")[1].split(")")[0]
                current_article_title = x.text.strip().split("\n")[0].strip()

                logging.info(str(page) + " 페이지의 " + current_article_number + " " + current_article_title + " 를 찾았습니다.")
                article_list.append([current_article_number, current_article_title])

        return article_list
    except Exception as e:
        logging.error(e)
        return []
