import urllib.request
import urllib.parse
import http.cookiejar
import re
import random
import time


class FishC(object):
    def __init__(self, cookie):
        self.cookie = cookie
        self.opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))

    def sign(self):
        re_hash = re.compile(r'formhash=(.+)">\u9000\u51fa</a>')
        re_resp = re.compile(r'<div class="c">\s+(.+)?</div>')
        re_usn = re.compile(r'\u8bbf\u95ee\u6211\u7684\u7a7a\u95f4">(.+)</a></strong>')
        hash_url = 'http://bbs.fishc.com/plugin.php?id=dsu_paulsign:sign'
        sign_url = 'http://bbs.fishc.com/plugin.php?id=dsu_paulsign:sign&operation=qiandao&infloat=1&inajax=1'
        qdxq = ['kx', 'ng', 'ym', 'wl', 'nu', 'ch', 'fd', 'yl', 'shuai']  # 签到心情列表
        self.opener.addheaders = [('Cookie', self.cookie)]
        res = self.opener.open(hash_url).read().decode('gbk')
        usn = re_usn.findall(res)[0]
        formhash = re_hash.findall(res)[0]
        data = {
            'formhash': formhash,
            'qdxq': random.choice(qdxq),  # 随机一个签到心情
            'qdmode': 2,  # 1: 自己填写, 2: 快速选择
            'todaysay': '',  # 自己填写想说的话(限制最少3个,最多50个中文字数)
            'fastreply': random.randint(0, 7),  # 随机一个快速选择的索引值(0-7)
        }

        data = urllib.parse.urlencode(data).encode()
        res = self.opener.open(sign_url, data).read().decode('gbk')
        res = re_resp.findall(res)[0]
        # print(res)
        with open('dz_sign.log', 'a') as f:
            f.write(time.strftime('%Y/%m/%d %H:%M:%S') + ': ' + usn + ': ' + res + '\r\n')


if __name__ == '__main__':
    # hldh214
    cook000 = 'oMVX_2132_saltkey=LM6Mj1Ah; oMVX_2132_lastvisit={0}; oMVX_2132_sendmail=1; Hm_lvt_8867f2e9bc13a08cafa6cffdfff2e6bd=1453887108; Hm_lpvt_8867f2e9bc13a08cafa6cffdfff2e6bd=1453887110; oMVX_2132_seccode=2563.26149e631842523243; oMVX_2132_lastact=1453887111%09member.php%09logging; oMVX_2132_ulastactivity=df80KIlm2har9UnNglm%2BW51sP6Wfyp3JTntbaLMlbaTa%2FivP8fQE; oMVX_2132_sid=vc6644; oMVX_2132_auth=4024idlCqTqKMirRaxQJeaUJRz5GTBoqD77%2BfxZ%2B4cFP4RK%2FzY3wTnVQI3diaSat0fTga6VS%2BE9NvGRThum99K0lQKo; oMVX_2132_lastcheckfeed=263749%7C1453887111; oMVX_2132_checkfollow=1; oMVX_2132_lip=49.210.242.19%2C1453886717; oMVX_2132_security_cookiereport=f9c2HKPBgfm4YhF2gpjuqzD4a1WaNXQEIF%2BpE3TeuywM2kSkHnM0'.format(
            int(time.time()))
    # fiddler04----fiddler214
    cook001 = 'oMVX_2132_saltkey=BQ1dWrGn; oMVX_2132_lastvisit={0}; oMVX_2132_sendmail=1; oMVX_2132_seccode=499.72769a6bc3892a5311; oMVX_2132_ulastactivity=d232pV%2FJeTMlACdEOBU%2FCQi8BMEEXNS%2BnZAt1ulfNfKvvmRidm2u; oMVX_2132_auth=95f6c%2BOg2r7RFCtaANsi%2FDKG8KHdIZeQ1PEfL79b8NVnVBZiyo%2F8RaRFCDqvO8qC2o34ND%2FpV1gDVYiNNOujs%2FZy048; oMVX_2132_creditnotice=0D0D1D0D0D0D0D0D0D350912; oMVX_2132_creditbase=0D0D2D0D0D0D0D0D0; oMVX_2132_creditrule=%E6%AF%8F%E5%A4%A9%E7%99%BB%E5%BD%95; oMVX_2132_lastcheckfeed=350912%7C1453601554; oMVX_2132_checkfollow=1; oMVX_2132_lip=153.92.41.232%2C1453545165; oMVX_2132_security_cookiereport=8f36uQz0IgcBpivnmjqQnyUohHyPL%2Fd6PKIDQoFcQ1sg3NgPArLf; oMVX_2132_nofavfid=1; oMVX_2132_onlineusernum=371; oMVX_2132_sid=Q5cqJ6; Hm_lvt_8867f2e9bc13a08cafa6cffdfff2e6bd=1453601541; Hm_lpvt_8867f2e9bc13a08cafa6cffdfff2e6bd=1453601559; oMVX_2132_lastact=1453601559%09home.php%09spacecp; oMVX_2132_connect_is_bind=0; oMVX_2132_checkpm=1; oMVX_2132_noticeTitle=1'.format(
            int(time.time()))
    # fiddler005----fiddler214
    cook002 = 'oMVX_2132_saltkey=Rw4E8cWu; oMVX_2132_lastvisit={0}; oMVX_2132_sendmail=1; oMVX_2132_seccode=1617.1265259cad52d9e63f; oMVX_2132_ulastactivity=35d1moNb%2BCAjNMccUDnhnWowsfGzY1YwAG3wKrITFGqrLVhueh8M; oMVX_2132_auth=7db8o24R2KEADcc0beon3v9VmvOd6FUNoDzSkZixcP6gu%2BDn4vz7Gpxw70hnRsyW57zA1qxy%2B8PFVzSQorYjDv3R43k; oMVX_2132_security_cookiereport=4fe3VVK9mOZAczF8uzHsFLsLJR0QroYdjeS%2BoVcmT83jVW%2Bu9tzD; oMVX_2132_nofavfid=1; oMVX_2132_onlineusernum=773; oMVX_2132_sid=lo9vL8; Hm_lvt_8867f2e9bc13a08cafa6cffdfff2e6bd=1453876304,1453876422; Hm_lpvt_8867f2e9bc13a08cafa6cffdfff2e6bd=1453876511; oMVX_2132_checkpm=1; oMVX_2132_lastact=1453876501%09home.php%09spacecp; oMVX_2132_connect_is_bind=0; oMVX_2132_lastcheckfeed=351367%7C1453876501; oMVX_2132_checkfollow=1; oMVX_2132_noticeTitle=1'.format(
            int(time.time()))
    f1 = FishC(cook000)
    # f2 = FishC(cook001)
    # f3 = FishC(cook002)
    f1.sign()
    # f2.sign()
    # f3.sign()
