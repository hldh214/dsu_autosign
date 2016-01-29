import requests
import random
import re
import time


class FishC(object):
    def __init__(self, cookie):
        self.cookie = cookie

    def sign(self):
        hash_url = 'http://bbs.fishc.com/plugin.php?id=dsu_paulsign:sign'
        sign_url = 'http://bbs.fishc.com/plugin.php?id=dsu_paulsign:sign&operation=qiandao&infloat=1&inajax=1'
        re_hash = re.compile(r'formhash=(.+)">\u9000\u51fa</a>')
        re_resp = re.compile(r'<div class="c">\s+(.+)?</div>')
        re_usn = re.compile(r'\u8bbf\u95ee\u6211\u7684\u7a7a\u95f4">(.+)</a></strong>')
        headers = {'Cookie': self.cookie}
        qdxq = ['kx', 'ng', 'ym', 'wl', 'nu', 'ch', 'fd', 'yl', 'shuai']  # 签到心情列表
        req = requests.get(hash_url, headers=headers)
        usn = re_usn.findall(req.text)[0]
        formhash = re_hash.findall(req.text)[0]
        data = {
            'formhash': formhash,
            'qdxq': random.choice(qdxq),  # 随机一个签到心情
            'qdmode': 2,  # 1: 自己填写, 2: 快速选择
            'todaysay': '',  # 自己填写想说的话(限制最少3个,最多50个中文字数)
            'fastreply': random.randint(0, 7),  # 随机一个快速选择的索引值(0-7)
        }
        req = requests.post(sign_url, data, headers=headers)
        # print(re_resp.findall(req.text))
        res = re_resp.findall(req.text)[0]
        with open('dz_sign.log', 'a') as f:
            f.write(time.strftime('%Y/%m/%d %H:%M:%S') + ': ' + usn + ': ' + res + '\r\n')


if __name__ == '__main__':
    # fiddler005----fiddler214
    cookie = 'oMVX_2132_saltkey=Rw4E8cWu; oMVX_2132_lastvisit={0}; oMVX_2132_sendmail=1; oMVX_2132_seccode=1617.1265259cad52d9e63f; oMVX_2132_ulastactivity=35d1moNb%2BCAjNMccUDnhnWowsfGzY1YwAG3wKrITFGqrLVhueh8M; oMVX_2132_auth=7db8o24R2KEADcc0beon3v9VmvOd6FUNoDzSkZixcP6gu%2BDn4vz7Gpxw70hnRsyW57zA1qxy%2B8PFVzSQorYjDv3R43k; oMVX_2132_security_cookiereport=4fe3VVK9mOZAczF8uzHsFLsLJR0QroYdjeS%2BoVcmT83jVW%2Bu9tzD; oMVX_2132_nofavfid=1; oMVX_2132_onlineusernum=773; oMVX_2132_sid=lo9vL8; Hm_lvt_8867f2e9bc13a08cafa6cffdfff2e6bd=1453876304,1453876422; Hm_lpvt_8867f2e9bc13a08cafa6cffdfff2e6bd=1453876511; oMVX_2132_checkpm=1; oMVX_2132_lastact=1453876501%09home.php%09spacecp; oMVX_2132_connect_is_bind=0; oMVX_2132_lastcheckfeed=351367%7C1453876501; oMVX_2132_checkfollow=1; oMVX_2132_noticeTitle=1'.format(
            int(time.time()))
    f = FishC(cookie)
    f.sign()
