import requests
import re


def getHTMLText(url):
    try:
        headers = {
    'authority': 'www.taobao.com',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.74',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://s.taobao.com/',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cookie': 'cna=VUO0FyoFMGICAbf2kjNKYlQL; hng=CN%7Czh-CN%7CCNY%7C156; thw=cn; _samesite_flag_=true; cookie2=13e3a96783aa42d8c1b705f10ae614cd; t=0a4bc2c4d33b50136c0116fe7e80341d; _tb_token_=3eee93b9b0737; xlly_s=1; sgcookie=E100zYQ6kE%2FgGWnVY%2Bwo2wZgrKs6uRUaZ8IcaEroSm%2BoPLXdcHhQ6cJx94uSFpFggBkuMcKL5mRqJjW0WJCrZ3v6pg%3D%3D; unb=2200665619958; uc3=lg2=UtASsssmOIJ0bQ%3D%3D&id2=UUphyu%2BCxkAmbReO4g%3D%3D&nk2=F5RHoJO0TdayLJo%3D&vt3=F8dCuASj8RXkRqHk8FM%3D; csg=53241bcc; lgc=tb211257991; cookie17=UUphyu%2BCxkAmbReO4g%3D%3D; dnk=tb211257991; skt=560e6559a7829c98; existShop=MTYxMzgyMDk3MA%3D%3D; uc4=nk4=0%40FY4MsnXwRW%2FK6Z2kVIwo5t9ynngXJQ%3D%3D&id4=0%40U2grEanDXKtLD600WLyY69sBavudbcR6; tracknick=tb211257991; _cc_=VT5L2FSpdA%3D%3D; _l_g_=Ug%3D%3D; sg=188; _nk_=tb211257991; cookie1=BdYH3v2wkTgoNniWri%2FmmIt8mxojlU%2BZE%2FRaVZgVENg%3D; enc=rWbw8cMMgVUdoaGeb9LsDmTio1y6s0zn3YBpJtZnYiy4aPXdejv1zGHiu95rnltWM0c06rFqi5dN7FxyUnaxbgBlbafZLMrwpPWtzUTy%2FJE%3D; mt=ci=0_1; uc1=cookie16=WqG3DMC9UpAPBHGz5QBErFxlCA%3D%3D&existShop=false&cookie14=Uoe1gW8aGmCTrg%3D%3D&cookie15=U%2BGCWk%2F75gdr5Q%3D%3D&cookie21=W5iHLLyFe3xm&pas=0; _m_h5_tk=ef68fc78280a1c0c5bbbc719ee7be165_1613829423853; _m_h5_tk_enc=68258a591a3d69e944b3094415be6252; tfstk=cLiOBNYa-BAMqmeKUVLhGbwEFSoAa2WTiONADLX02XHWsgIAcs4-q0HTKFw4HCvd.; l=eBTOQWvPOMKEFA9oBO5CFurza77OoIRb8KVzaNbMiInca6Ol1F6WRNCIkQUwRdtxgtfYeeKrzoRtYR36z0438xs1dPGngnspBxv9-; isg=BLCw41qvpIOSOkeBwkm93khGgX4C-ZRD_YlPSqoBr4veZVEPUwyi0kcXuG0FXEwb',
    'if-none-match': 'W/"1d77d-j6W/RgMTFSfTt6103NnKtZb/Eaw"',
}
        params = (
    ('spm', 'a230r.1.0.0.bd2968b8cuMCXV'),
)

        r = requests.get(url, timeout=30,
                         headers=headers, params=params)
        r.raise_for_status
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ''
    


def parsePage(ilt, html):
    try:
        plt = re.findall(r'\"view_prise\"\:\"[\d\.]*\"', html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price, title])
    except:
        print('')


def printGoodsList(ilt):
    tplt = '{:4}\t{:8}\t{:16}'
    print(tplt.format('序号','价格','商品名称'))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))
        


def main():
    goods = '书包'
    depth = 2
    start_url = 'https://s.taobao.com/search?q=' + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44*i)
            html = getHTMLText(url)
            parsePage(infoList, html)
        except:
            continue
    printGoodsList(infoList)


main()
