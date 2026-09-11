from lxml import etree
import json
import requests


headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://roark.com/products/mens-bless-up-breathable-stretch-shirt-fossil-print",
    "sec-ch-ua": "\"Chromium\";v=\"152\", \"Not?A_Brand\";v=\"24\", \"Google Chrome\";v=\"152\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-viewport-width": "881",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36"
}
cookies = {
    "GlobalE_Analytics": "{\"merchantId\":\"30001158\",\"shopperCountryCode\":\"UA\",\"cdn\":\"https://web.global-e.com/\",\"clientId\":\"0f026371-de10-46ea-b70e-619b99cf5a7b\",\"configurations\":{},\"featureToggles\":{\"FT_3DA\":false,\"FT_3DA_UTM_SOURCE_LIST\":[],\"FT_3DA_STORAGE_LIFETIME\":4320,\"FT_BF_GOOGLE_ADS\":false,\"FT_BF_GOOGLE_ADS_LIFETIME\":30,\"isOperatedByGlobalE\":false,\"isPiiDataEnabled\":true,\"isEventSendingDelayed\":false},\"dataUpdatedAt\":1789027045074}",
    "_shopify_y": "bd87b171-deb6-4615-973b-54eedec3dc88",
    "_shopify_s": "5342c26b-72f5-4e3d-a4b3-73ea5d39a37d",
    "localization": "US",
    "cart_currency": "USD",
    "ede-s": "c410323b-a42f-49e8-b9f3-a35b0cc537ee",
    "ede-i": "60d31b43-973e-41ae-b29d-5e23368ea786",
    "ede-expid": "0fc35cdd-71cd-49af-a641-f22dc19eb887",
    "ede-expvar": "Edge Delivery Enabled",
    "__eventn_id": "b7932781-30d9-4666-ad04-edbe0f043e6d",
    "_gcl_au": "1.1.1156144573.1789025588",
    "__kla_id": "eyJjaWQiOiJNbVJrWVRnNFl6Y3RNR1prT0MwME16STBMV0l3WXpNdFpXSmtNRFZqTmpJNVlUbGgifQ==",
    "ig-location": "{\"country\":\"CN\",\"city\":\"Shanghai\",\"continent\":\"AS\",\"latitude\":\"31.22\",\"longitude\":\"121.46\",\"region\":\"Shanghai\",\"regionCode\":\"SH\"}",
    "ig-id": "ig_a5b1a8127fa43b4fd7cdb401c1a048fc49ba",
    "ig-fv": "1789025588223",
    "ig-vars": "{%2263e75d9ffcdf%22:%22a20650191873%22%2C%22redirectedFrom%22:%22%22}",
    "_ga": "GA1.1.1453494572.1789025588",
    "__spdt": "7915c7b45bd64404a957d1676f060e31",
    "shopify_client_id": "bd87b171-deb6-4615-973b-54eedec3dc88",
    "rrssts": "1789025589341",
    "_clck": "pa8iz2%5E2%5Eg9c%5E1%5E2444",
    "rrv2ses.094a": "*",
    "_fbp": "fb.1.1789025591360.582575300235302362",
    "FPID": "FPID2.2.UAaAZak64t7yIX2RBGGeafp%2BjHD37Td6atvNI%2BUbUwE%3D.1789025588",
    "FPLC": "pQKNeiyBjX%2B8SDuV6VQKiitoyd4zl9DK3UR7VQxpjsZ8z%2BY%2FVhaPi8L5iu9NOi3GFcgjgwolcC%2FBKnxHuHwYDOvPRp3Y%2Ffh9quR6PEEpNEUmkVZbnz2yv9pBQDJ7Bw%3D%3D",
    "cart": "hWNGf7cZAMh5ZhPHjnXMi11c%3Fkey%3D242639f643cda96cd375c775b6dbcaaa",
    "__mmapiwsid": "01a08a3c-7aa5-77a3-a2e0-21e1602af8fa:f1772aa3f60c6c7656cb20e02efd60f30d204431",
    "_ps_session": "ZRUy90QeXhpPRy8O71rzM",
    "_ps_site_visit": "true",
    "GlobalE_Consent": "%7B%22required%22%3Afalse%2C%22groups%22%3A%7B%221%22%3A1%2C%222%22%3A1%2C%223%22%3A1%7D%7D",
    "ede-r": "",
    "rrv2id.094a": "4589fa8b-6d56-46c3-82e4-e3029ef548e6.1789025591.1.1789026929.1789025591.186fe94f-55c5-4f45-bd6c-7c95e6ceb622",
    "ede-c": "stash-hit",
    "ede-p": "/products/mens-bless-up-breathable-stretch-shirt-fossil-print",
    "GLBE_SESS_ID": "%7B%22sid%22%3A%22706407256.508020522.30001158%22%2C%22expiry%22%3A%222026-09-10T08%3A26%3A03.583Z%22%7D",
    "_ps_session_site_visit": "%7B%22sessionId%22%3A%220d4aa2c2-9b9f-483d-878f-613759e2882b%22%2C%22startTime%22%3A1789026963616%7D",
    "forterToken": "db7db88a145b4e96bbcb2c0083c3c651_1789026963172__UDF43-m4_29ck_",
    "rrpvc": "53",
    "cf_clearance": "F9DwvhsitZlMCdd.tGUbwYOhOjyMu3KDCp8j2DtcuAA-1789027039-1.2.1.1-0qx4q7YsWxC71M8YqkIpp3EIDQpU8dN0U.NSR2ImyzHyDTmDGuoDJK7sY.At1eegDNFzoz._pKzbkSTyfyCLur2Hccjs7vJ50ZjwrOOjJUxqdgmEeF6VUtDKK9E4TDXPPYQ_p0fAYxFYpW_S3qnJvK2.gh6hcCbYgdt5KyjVEajoSHzvEw5AidKmkwR7PeNApRGM1luta5sytxDohGnbgpGWyirfmnA7bPmzKTvvbWbhBdgaimZ83iEBHyvlyhprxzfWHXY3nCx_U16.VP7JW7u7TL8iGYARy_6XbjbYeNRdKBMShG5bHYfFMj2.m1jgxOyQIqBGWjRa_sLMu2y71sJcLK0ECUyP0jnBksrTG5c",
    "__cf_bm": "gz9RGZTewWLup0OCB7ZGjJwPbTPkqVycq64ki3IObCs-1789027039.5057735-1.0.1.1-WI1aQhSurA0XrW.HylqKet3MhusasRadLfa.J0qHENT2ycOl54_WmDaHMQvdHQW8W0YEhcK21oxXMkb4ZbmmTfkDGKDbZVYi1dKc199gDamOmBH0KTJWfxnx7NsV9OG9",
    "geolizr_data": "{%22as%22:%22n/a%22%2C%22asname%22:%22n/a%22%2C%22mobile%22:false%2C%22proxy%22:false%2C%22city%22:%22%22%2C%22currency%22:{%22code%22:%22CNY%22}%2C%22country%22:{%22code%22:%22CN%22%2C%22country%22:%22China%22}%2C%22countryCode%22:%22CN%22%2C%22continent%22:%22Asia%22%2C%22continentCode%22:%22AS%22%2C%22isp%22:%22n/a%22%2C%22lat%22:34.7732%2C%22lon%22:113.722%2C%22org%22:%22n/a%22%2C%22query%22:%22240e:469:e698:f0ad:c0a7:c1e5:fdc:25b6%22%2C%22region%22:%22%22%2C%22regionName%22:%22%22%2C%22status%22:%22success%22%2C%22timezone%22:%22Asia/Shanghai%22%2C%22zip%22:%22%22%2C%22cloudflare%22:%22%22%2C%22ttl%22:0%2C%22env%22:%22PROD%22%2C%22build%22:%22maxmind%2008%20Sep%2026%2017:01%20UTC%22%2C%22currencyCode%22:%22CNY%22%2C%22countryName%22:%22China%22%2C%22service%22:%22ip.lovely-app.com%22}",
    "ig-pv": "10",
    "_shopify_analytics": ":AaCKPAHMAAEAKu5QOVU0YNtCcuRKh_q87yNtdFKIV5kkOK6EgUB-9mVK4XqB1kPgT9vsHbEmhEaBjg6RstL97BHLHqT9XDaLVabEgtEIPmRo0wqqzp8OiNjKdt0:",
    "_shopify_marketing": ":AaCKPAHMAAEAds11UCTZsI55ZBHjI5um4A96q-cGUQJDMSgcV0_98A2gBk5Ov3G22cRGlGL4_YphbZVrWPF0p6wImNwSo34whv2lS3k1HN-fkMggLoUqkHO7XlU:",
    "_uetsid": "ddf98e90ace911f181dde9bac42dc1ae",
    "_uetvid": "ddf9bdb0ace911f18168f50583fb3a73",
    "_clsk": "znef0b%5E1789027046081%5E1%5E1%5Et.clarity.ms%2Fcollect",
    "_dd_s": "aid=f321d47a-e17c-46bc-a771-b46e3d5bf705&logs=1&id=a908dce1-4d48-46a0-9cef-139877e99f12&created=1789025591784&expire=1789027982606",
    "_shopify_essential": ":AaCKPAGjAAEAGr5KXeb_Xv7EXk2iwzGbS8KsvcPNHmC5jLUIMjqifMMFyHy-DkCZtcKI2D7qSUHZ5qVqOjQKQfMEkXyJj8TTgZcxUGL5pvuUTIPRbgQCaGjIqNFXbsrGfGVWSI3a6zhL_RnElhd6lz63PR8xXf12VpUolNffciszmtvbWjKiegzWIIGZDkq9ZURucaqqDHUN-fWUCc6ugtyxLwiVByLIuw0rZ2kDrOsTkx44QS2a5cqgmpssKsaxtVylvcQSxN4U-vAiiQknQlyEivmHwpVrrWFlCvcSAqrvaLI9_MLO9rIwiSpCQhD0jRrX1myaV9GllxzGr3nLQ1jigT1xjs1CC5sfy-NHgumIcA82YpmGcIUTMvoiKjuPRr5mtWtRs1w7KFOwsQBmjiScRL9FWqHUfA60jXfJRyjFzrrzDZNdRVHZl_FaHnG-gsoCWDu5KUbZ5bZH-_Tq64EHUKlLp2dLdUHyRDWPFbZYtcdFi6-o6W35Ajuy-jBBihRQaeiSy8hWHBUQobA9Ct8fTemdjpSOSHM-ikhlCyvLBWmeK2beZIR0lI6Y4nTrX8AagS_9SpjWuPWKhzWDLK-rUneOnvMI88ihIYTbaeSexuiSS7bB2PKZi3_ThSA6rY2jI12fSpAH9s4Pq8Dm45_AW-jBGwFFbzYsrq2it4CGGF-PkZej0yugx58WZvidY6NW0hAEBYsc3mgJvppKbC8EAvBh9h6n0qAVlHtQwwtzalaBiD40-WfflJXh7odIZ-0xx1s:",
    "_ga_LV31RDQLDF": "GS2.1.s1789025591$o1$g1$t1789027094$j6$l0$h1626748544",
    "_ga_T86KF5Z744": "GS2.1.s1789025588$o1$g1$t1789027094$j6$l0$h0",
    "_ga_ZJ0X2V7S9S": "GS2.1.s1789025588$o1$g1$t1789027094$j6$l0$h0"
}
url = 'https://roark.com/products/mens-bless-up-breathable-stretch-shirt-fossil-print'
params = {
    "skipCache": "true"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)

if response.status_code == 200:
    doc = etree.HTML(response.content)

    #默认的商品为第0个
    script = doc.xpath('//script[@product-data]/text()')[0]


    def get_value(key):
        i = script.find('"' + key + '"')
        i = script.find(":", i) + 1
        return json.JSONDecoder().raw_decode(script[i:].lstrip())[0]


    name = get_value("title")
    price = get_value("price") / 100
    color = get_value("color")

    images = []
    for img in get_value("images"):
        src = img["src"]
        if src.startswith("//"):
            src = "https:" + src
        images.append(src)

    sizes = []
    for opt in get_value("options_with_values"):
        if opt["name"] == "Size":
            sizes = opt["values"]
            break

    print("name:", name)
    print("price:", f"{price:.2f} $")
    print("images:")
    for image in images:
        print(image)
    print("Color:", color)
    print("Size:", sizes)
else:
    print("请求失败:", response.status_code)

