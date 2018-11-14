#!/usr/bin/env python
# encoding: utf-8
import time

import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def get_feeds():

    data = {"url":"https://aweme.snssdk.com/aweme/v1/feed/?type=0&max_cursor=0&min_cursor=0&count=6&volume=0.06666666666666667&pull_type=2&need_relieve_aweme=0&filter_warn=0&req_from&is_cold_start=0&js_sdk_version=1.2.2&app_type=normal&manifest_version_code=321&_rticket="+str(int(time.time()))+"&ac=wifi&device_id=52650937206&iid=50374690113&os_version=8.1.0&channel=gray_3306&version_code=330&device_type=ONEPLUS%20A5000&language=zh&uuid=866265035315870&resolution=1080*1920&openudid=4617150637217100&update_version_code=3216&app_name=aweme&version_name=3.3.0&os_api=27&device_brand=OnePlus&ssmix=a&device_platform=android&dpi=420&aid=1128"}

    resp = requests.post(url="https://crawldata.app/api/douyin/v2/sign", data=json.dumps(data),
                         headers={"Content-Type": "application/json"}, verify=False)
    content = resp.content.decode("utf-8")
    d = json.loads(content)
    url = d['url']
    resp = requests.get(url, headers={
        "User-Agent": "com.ss.android.ugc.aweme/321 (Linux; U; Android 8.1.0; zh_CN; ONEPLUS A5000; Build/OPM1.171019.011; Cronet/58.0.2991.0)"},
                        verify=False,
                        cookies={"install_id": "50374690113", "ttreq": "1$38b472f84b775d8d0f3228c4a1666cd82ce9ed79",
                                 "odin_tt": "d02add7886fd9d7876382dfb4fade469be1b1933345c0687ddbafdb9975a93afa52ed70569cf8e5506aafdec4071e5f6",
                                 "sid_guard": "d4896895f8bbfe82cdb49ac577317032%7C1541682822%7C5184000%7CMon%2C+07-Jan-2019+13%3A13%3A42+GMT",
                                 "uid_tt": "050eb346f3daccb101ff0b3a4aabdd7d",
                                 "sid_tt": "d4896895f8bbfe82cdb49ac577317032",
                                 "sessionid": "d4896895f8bbfe82cdb49ac577317032"})
    content = resp.content.decode("utf-8")
    d = json.loads(content)
    return d


# 获取10页
page = 0
page_max = 100
while page < page_max:
    page += 1
    feeds = get_feeds()
    print("page:" + str(page) + " feed len:" + str(len(feeds['aweme_list'])))
    for feed in feeds['aweme_list']:
        # print(feed['is_ads'], feed['share_url'], feed['desc'])
        if feed['is_ads']:
            print(feed['share_url'], feed['desc'])
