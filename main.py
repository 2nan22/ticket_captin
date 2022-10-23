import requests
import random
import json
import schedule
import time
import datetime
import time
from tqdm import tqdm
from pytz import timezone

import TL_common.common_utils as common_utils
import TL_scraping.common_variable as scraping_variable
import TL_Slack.common_variable as slack_variable
import TL_recommend.common_utils as recommend_utils
import TL_recommend.common_variable as recommend_variable

slack_api_token = slack_variable.SLACK_API_TOKEN
slack_channel = slack_variable.SLACK_CHANNEL
path_json = scraping_variable.path_json



def main():

    common_utils.add_job("00:39")
    common_utils.run_job()


if __name__ == '__main__':
    main()