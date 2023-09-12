# -*- coding: utf-8 -*-
"""
在下面设置你的米游社Cookie
"""
mysCookie = '_MHYUUID=357f717a-54d6-439e-a0c4-d83af24f8a35; DEVICEFP_SEED_ID=85092b700d4432c4; DEVICEFP_SEED_TIME=1694501109847; DEVICEFP=38d7f06a78f56; login_uid=315065630; login_ticket=hOpjqNbKFwKMQKOkFAo1ikLjBzIcGQT0ypjAEkxk'
"""
以下内容不要改！！！
"""
mysVersion = "2.34.1"
salt = "z8DRIUjNDT7IT5IZXvrUAxyupA1peND9"  # 米游社2.34.1版本安卓客户端salt值
salt2 = "t0qEgfub6cvueAPgR5m9aQWWVciEer7v" #这个给签到用
client_type = "2"  # 1:ios 2:android

"""
api
"""
cookieUrl = "https://webapi.account.mihoyo.com/Api/cookie_accountinfo_by_loginticket?login_ticket={}"
cookieUrl2 = "https://api-takumi.mihoyo.com/auth/api/getMultiTokenByLoginTicket?login_ticket={}&token_types=3&uid={}"
signUrl = "https://bbs-api.mihoyo.com/apihub/app/api/signIn"  # post
listUrl = "https://bbs-api.mihoyo.com/post/api/getForumPostList?forum_id={}&is_good=false&is_hot=false&page_size=20&sort_type=1"
detailUrl = "https://bbs-api.mihoyo.com/post/api/getPostFull?post_id={}"
shareUrl = "https://bbs-api.mihoyo.com/apihub/api/getShareConf?entity_id={}&entity_type=1"
voteUrl = "https://bbs-api.mihoyo.com/apihub/sapi/upvotePost"  # post json 

"""
分区编号
"""
gameList = [
    {
        "id": "1",
        "forumId": "1",
        "name": "崩坏3",
        "url": "https://bbs.mihoyo.com/bh3/"
    },
    {
        "id": "2",
        "forumId": "26",
        "name": "原神",
        "url": "https://bbs.mihoyo.com/ys/"
    },
    {
        "id": "3",
        "forumId": "30",
        "name": "崩坏2",
        "url": "https://bbs.mihoyo.com/bh2/"
    },
    {
        "id": "4",
        "forumId": "37",
        "name": "未定事件簿",
        "url": "https://bbs.mihoyo.com/wd/"
    },
    {
        "id": "5",
        "forumId": "34",
        "name": "大别野",
        "url": "https://bbs.mihoyo.com/dby/"
    },
    {
    "id": "6",
    "forumId": "52",
    "name": "崩坏：星穹铁道",
    "url": "https://bbs.mihoyo.com/sr/"
    },
    {
    "id": "8",
    "forumId": "57",
    "name": "绝区零",
    "url": "https://bbs.mihoyo.com/zzz/"
    }
]
