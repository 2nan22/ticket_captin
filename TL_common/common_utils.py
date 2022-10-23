import datetime
import json
import time
import requests
import schedule
from pytz import timezone
import TL_common.common_utils as common_utils
import TL_common.common_variable as common_variable
import TL_recommend.common_utils as recommend_utils
import TL_recommend.common_variable as recommend_variable
import TL_Slack.common_utils as slack_utils
import TL_Slack.common_variable as slack_variable

path_json = common_variable.path_json
slack_api_token = slack_variable.SLACK_API_TOKEN
slack_channel = slack_variable.SLACK_CHANNEL

def get_today_ymd_hms():
    """
    날짜 별 폴더 생성 시 파일명 호출 함수
    :return:
    """
    now = datetime.datetime.now(timezone('Asia/Seoul'))
    today = now.strftime('%Y/%m/%d %H:%M:%S')

    return today


def get_today_md():
    """
    날짜 별 폴더 생성 시 파일명 호출 함수
    :return:
    """
    now = datetime.datetime.now(timezone('Asia/Seoul'))
    today = now.strftime('%m%d')

    return today

def post_message(token=slack_api_token, channel=slack_channel, text=''):
    
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer " + token},
        data={"channel": channel, "text": text}
    )
    if str(response) == '<Response [200]>':
        now_time = common_utils.get_today_ymd_hms()
        print(f'{now_time} : 오늘의 메뉴 추천이 완료되었습니다')


def add_job(time):

    ko, jp, ch, we = recommend_utils.today_menu()

    schedule.every().day.at(time).do(post_message, slack_api_token, "#점심-메뉴-추천", '\n' + ko + '\n' + jp + '\n' + ch + '\n' + we)


def run_job():


    while True:
        schedule.run_pending()
        time.sleep(10)

