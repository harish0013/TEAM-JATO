import scrapy
import json


class MobileSpider(scrapy.Spider):
    name = 'mobile'
    allowed_domains = ['suchen.mobile.de']
    start_urls = ['https://suchen.mobile.de/']

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
    }

    cookies = {
        '_bb_lat_long': 'MTIuOTM2OTgwM3w4MC4xNzQwMjAy'
    }

    def start_requests(self):
        # Start by requesting the initial URL to get to the search results page
        yield scrapy.Request(self.start_urls[0], headers=self.headers, cookies=self.cookies, callback=self.parse)

    def parse(self, response):
        # Navigate to the search results page directly for simplicity
        # pages_info = response.xpath("div[data-testid='srp-pagination'] > ul > li").getall()
        pages = 50
        for page in range(0,int(pages)+1):
            search_url = f'https://suchen.mobile.de/fahrzeuge/search.html?isSearchRequest=true&lst=p&od=down&pageNumber={page}&ref=srpNextPage&refId=ce2e4d33-a6e6-0d97-4e3c-d1d12e6dc196&s=Car&sb=doc&vc=Car'
            yield scrapy.Request(search_url, headers=self.headers, cookies=self.cookies, callback=self.parse_search_results)

    def parse_search_results(self, response):
        cookies = {
            'optimizelyEndUserId': 'oeu1722428871713r0.24635694339567604',
            'vi': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InYxIn0.eyJjaWQiOiIzOWUwNWRjZS01ZGE1LTQ1OWQtYjFhYi02ZDMyZDY1MjEyNzQiLCJpYXQiOjE3MjI0Mjg4NzF9.3dSRiEojdBDWZmyo6vtgvX2WurwyhKChUJDLIsqy2QA',
            'mdeConsentDataGoogle': '1',
            'mdeConsentData': 'CQCkcIAQCkcIAEyAHADEA_FgAP_gAELAAAYgJepV5CzdbWFBcX53aPsgOY0X1tBTIsQhAhSAAyAFgBOQ8JQA02EyNASgBiACEAAAoxZBAAEEHABEAQCAQAAEAADMIgQEgAAIIABEgAEQAAJYAAoKAAAgEAAIgAIFEgAAmBiAIdLkXUCAgIAACgAQAAABAIAAAgMAAAAIAAMAAAAAQgAAAAAAAAIAAAAAARAAAAAAAAAAAAAAIF5wBAAQAA0ACYAvMAYJAvAAQAAsACoAHAAPAAyAB4AEQAKoAbwA9AB-AEIAIaARABEgCOAEsAJoAYAAwwB3AD2gH2AfoBFACNAEiAJKAXMAvQBigDaAG4ASIAnYBQ4CjwFIgLYAYaAyQBk4DMwGrgNZAcEA8cB7Q6BoAAsACoAHAAZAA8ACIAFWALgAugBiADeAHoAPwAhoBEAESAJYATQAowBgADDAGiAO4Ae0A-wD9AIoARYAjoBIgCSgFzgLyAvQBigDaAG4AOoAhABF4CRAE7AKHAUeAtgBhoDJAGTgMqAZYAzMBq4DiwHjgPaAgCQgJAALACqAFwAMQAbwA9ACOAGAAO4AigBKQC5gGKANoAdQBaIDJwHjkoDYACAAFgAcAB4AEQAKoAXAAxACGgEQARIAjgBRgDAAH4AXMAxQB1AEIAIvASIAo8BbADJAGTgMsAe0BAEpAoAAWABUADgAMgAeABEACkAFUAMQAfgBDQCIAIkAUYAwABowD7AP0AiwBHQCRAElALmAXkAxQBtADcAHUAReAkQBOwChwFsAMNAZIAycBlgDWQHBAPHAe0BDktAGAGAAO4AvQChwGZgPHA.YAAAAAAAD4AAAKcAAAAA',
            '_ga': 'GA1.1.2106014981.1722428888',
            '_gcl_au': '1.1.1302666604.1722428889',
            'FPID': 'FPID2.2.iixRz3ThUFc7BTZg0gpY4YFDhy1FhqzXDI9aSEpTBx0%3D.1722428888',
            '_tt_enable_cookie': '1',
            '_ttp': 'XIf_Kf1kbzDe3SFsJbhSIC_j31s',
            '_hjSessionUser_3567183': 'eyJpZCI6IjBhMjUwNTFiLWJkZTgtNWI5OC1hYzQ3LTE1NDU5YTUyZTg5MyIsImNyZWF0ZWQiOjE3MjI0Mjg4ODg5NTgsImV4aXN0aW5nIjp0cnVlfQ==',
            '_fbp': 'fb.1.1723196113210.431422292237617949',
            '_pubcid': '20983fd1-726f-4ef1-8bb3-01a0599e4dd0',
            '_pubcid_cst': '8yyiLEEsMA%3D%3D',
            'axd': '4369192905572835944',
            '__gsas': 'ID=b7bf26a155f6c3e1:T=1723196234:RT=1723196234:S=ALNI_MYAo2Q13crwPbRVwsOv9zWgZ3glAg',
            '__rtbh.lid': '%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22wIB6qwheHP5pXWRR2nba%22%7D',
            'hsstp': '1',
            '__rtbh.uid': '%7B%22eventType%22%3A%22uid%22%7D',
            'mobile.LOCALE': 'de',
            'tis': 'EP117%3A3989',
            '_hjHasCachedUserAttributes': 'true',
            'FPLC': 'R031AsqrDSjoQW6%2BBjokpDiAorgff7SUZ%2FftP2g1OMHnctuRCPGEjAdFW5VTP0itXHPyx%2FeZ9E%2FDozTtHWehOyT6f2J8ykvMJOAv6Sv1RoLX%2FwDKqkVcaeoszccXUw%3D%3D',
            '_lr_sampling_rate': '100',
            '_hjSession_3567183': 'eyJpZCI6ImUxODgyZTlkLWY4Y2MtNGI4Yy1iZjNjLTNmZTVhOTk1YzQ4MiIsImMiOjE3MjMyOTM1NzYxNTgsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MX0=',
            'bm_mi': '9CF56EE83FF8B45E959DD059AC0F6F9E~YAAQIDwSAvhMUyiRAQAASJHBPBjap0XM33SsqdFgaC/Pj+xKz6U+P1KB+79Moy/L3rF9dzADh9x3sb+ZeYu94ZLOlw2KdGr68kYhQ9at+GFNVg8SDlpq5v8jvQKPn4fFBJ9anSsK5N+Xs8WFdXpWaF8dWy2FnN5t/9OyKZSxXk58c0yAT6kaY7O22QubQc14hNyA/cJ+HUQe9nxryFWpw6xL6mARIBmdmpe4mUWW+yWRSv5dFYiJZ3W3JvtDP7jniyvT8ZFTLagrl4524Gg4HyB4oBk4KAS/xDd5NOz6PpJ1sX4jqTPxItoJYfWPphJlmVwKH23frCmtc3nrnTCs3Tx08A==~1',
            'ak_bmsc': '29899BE5C8AC9BCF86D0936995068F82~000000000000000000000000000000~YAAQIDwSAqkdVCiRAQAAU9DRPBi42T/pNUFc2JgtJICvN9cRqQXb2OMcp9bIbq4GaKC+1Ch/4w9gQTZXWWuPpj4H+XZjvalzXDrZcSbPZ9ccVeOrq8IPjkITrsz4LWFWFIWXqonbiJByP97ZvyTqHyZZ5tY+w6PhlWSrzB1OsMAXrZwFjOpij9yUgkLEYr8kDgCxtCLEcKV7Y5oGz0nfBQixB8Ju8KA/P4QjyBVlsmDPyQR1yj/ZaNecB0Ga9B/OM/yPP/IaY04sSLYylhvADv/fQTff+nX3qxtEGwsBKY1CMPAeE1fp06nVraZjJ+t1UTLIquRwZvgEjeLcRHJkBrU13A5PuuU//IXanPbAERRnP0J1kawRcb5FGF/ERBahsLKmYhJURkxkED+KfrWNHunPGmtMhplnn7VE0l8S1gPgtqEv4P0lI8k97ARMyvRs9QAyYqnq1/FGJIfG4YaaURkPYlMaTuunQxsVB2dI7jNnTIXfQphdnmRwG2ILuri7y0TZR2sMhd5xUr5d8RRk+/1ADgJm2/sdigKbG7M7IBQSAIcm84F/WNV4lvqlKjYXq0h+ApZ8s/AIWmN25vo7u9kUjT0sdnYXQxoXU4yEFSqZRX+qMJAqGy+UHh5pT8wcL9SFjG2IFecF5KCcLodCPQeBGNwtG5g=',
            'bm_sz': 'B2123C1CDC6AF165BAD98F0764B6A9D5~YAAQIDwSAqsdVCiRAQAAU9DRPBgaE3ljhG5K+3eSBMMHVMH5hRhykBV53JmM+VlsA6kqmPaHEiTeEnM9kcg5QieUE0VkbIchUCvK8GCqmftE3e1F41vZsJ/gKPGM5G1IffTd/TPXZ7cn56A5Tl8NBnt8TU6ch81d/MhrNYia+X6pRSot8dVeBhTC5Mhaxh83xTU7BOHyODtS2OhqfpeIPbVnVlsHIHZVJ74TK3UQ2jZXe2VZam7f0w4IYckONDCOm4V4/HOlYye0BWCchWt3TNdF+/g9gxoLcuZMm9KI63ZuMe6oi8aadDbvaemhQpWTRfixrrDF5Rhxdfc6zdrPGgjQQQ+uvZ53PicOxndBEGBhM0rDIAkDYJ0wfEYttl3ICNRHNQwS7FPH+m5IUaR92daae/FBQXNe92/ZY0+wNItyw4JR4XJ7BcSbqL/1E/az7R2Ehvw1R9cy5j6UjW0J0Pn8AMd5R1Sh+4qdaIl3byqvCcOSmz3h6FfV1deEWKlLNMDRO93AWMtNS4bcXNHkmKNjO9VLn4LhA0jVTXk+ZVUUstDxlKA=~4338740~3224889',
            'ces': '{%22lv%22:[1723302271525%2C1723299725868%2C1723297272593%2C1723295383588%2C1723293571426%2C1723288003762%2C1723285615501%2C1723283426535%2C1723280783811%2C1723277487650%2C1723198159255%2C1723196232667]}',
            '__gads': 'ID=0442cca318e7d640:T=1722428886:RT=1723302273:S=ALNI_MaaS2KEZjpF4REgfbwA6wV5PJajzg',
            '__gpi': 'UID=00000eaf5a116303:T=1722428886:RT=1723302273:S=ALNI_MbJ6p09t10eFJWl-zlZrwr_IBLw3w',
            '__eoi': 'ID=56b1b9069d604832:T=1722428886:RT=1723302273:S=AA-Afjbxw0H4GEGXbsfqtpftYv1i',
            'cess': '{%22s%22:41%2C%22nsf%22:1%2C%22v%22:36}',
            '_ga_2H40T2VTNP': 'GS1.1.1723293573.9.1.1723302508.0.0.1839722994',
            'cto_bundle': 'D-hWr19BcjR0R2EzNkFORWd1SjB1Y1lUbW5QRyUyQlNVM3BEVjVVcndhVjFDaTJFbXJsZU5sTWhqbXNua0FoMzF3WjdtaG5HRGR4ck5lemgyWk1EdndOdTRGTFBoT0JjZ3RRa1pwbkpjczljNlFSd2Z4ZDlIJTJGdmFEaHFubFRuUGx3a2tRb2l5SzIlMkZJd0xremRrU0YlMkY2UWxsQ3RLVXpyODhJdDFHTkJnaFZiOEh5clF3dVNQSkJrbm5XOEFYT0R5MW9XRiUyQnVxeDlmYzNmZyUyRkNiMWo1amNxWWtGJTJCb3clM0QlM0Q',
            '_uetsid': 'af2271d0563211ef9906ffb7cb19b63c|ubyrfj|2|fo7|0|1682',
            'dicbo_id': '%7B%22dicbo_fetch%22%3A1723302515043%7D',
            '_abck': '33AF85381E6E77D59AECD881A1C31EED~-1~YAAQIDwSAtdSVCiRAQAAq5XVPAzfXZRVYHqIyXEQjZmu6jx42FP5N0IVAK3WssWII6YgeT/mNIbtscqEfBz/8o9nL0vvjoyoTREihSsk3lpKJFfExo0Pg+d5oYDkPaIp7+rh/lvnFdpEd/elOSIP6lW47gSTkqMu4r9KE6mjUAgdQITEokGH4qVhVLJYzC+PY8S8eLT6oXDOPbA0wuYcF0qIlUO7b4m5w/+RxkfxE781XY+UjmdL4j/LfJ9VnWvqFkoDaDAqwglijzwTzz0H44fQW4B/73uaX3IrNV7m8VasTqAQPFGhQf4qFDgy8ai7TGLKHc4zBWZU+d9jRQg7+gPZ1TriJkOTfSEMx7ItdtyDHIQboKfudRAuBdLsKzJBat/diY6pNGNVVNDRCifgJvZH3YDO8CJxPc03FeiNVW4Ta19nAs4W2hFiXNri1AIPfATKjkKU5Ziu0uKXrtB6RGIylg==~0~-1~-1',
            'bm_sv': '40E7BBEFF25802A7779D90024017BBA0~YAAQIDwSAthSVCiRAQAAq5XVPBiN6UFjoXSR3nNKjEMUMWwCyPEb0+izoYGnJq41gJlI1obATylLj11seApypxxQA9ZPvaC2NCOrDtF0SBwD1cLQXWEdadoRH/xESbh77KAFeEqp2Y4OXFXp+KCC2BCOcFVQK+VX/Nv4Unil6bw5YfsRN1JYiPbsQB0Ft+MnlaZpMw+oH5mK2xF/2MWOQ42nFDjvuy+DPUCKILqL+tw0AFXG8/aBfmIMpJCIkwfm~1',
            'sec_cpt': '24738D10D1DC3198A601140BA43D4631~1~YAAQIDwSAtlSVCiRAQAAq5XVPAu+ZzFmNymKQx85dnQtw5OAKsGRot+i3Wz7WBMEvs5i0BJxUMJcB9SGjjwnneBgTHBAPaQ+uKA5xkm0Ifmuq3rf/NlNAj3+uSx8W4N7NHZ/+4BJok5ntqn/XKIZawY1MX1nUVCdrrHjBkOjKhcJA8jO9oXOdej7lSzD94xIGaBis4bE0SOoArRgpJKJBPWkGWCkOWu2lhrwbmMgyg5N9sYIw5JV3kz9u/KH+lmvr2Cvw9Wi/sDsN5pa2j3RnDKk2jkcJHfcwdkcWPb7QOMvVhe3ktRTvvCzkcNOqdq9q54gRPoAwqLIpj1mhlb4PpFqZKOj0IJVy53VWkZVJIvRlHaj9IGUc3lPQ3KTuTjvz6FQx4n0PECcIaWUpvbFyBxo0zNCljzZRi1AdVD0gp3n56OfMg1nNjJ6JyJCo9ZaexE9LunDtjqybG2QnvVjKJxJX8ArasudyWeYjqtTdJH186SmNECV6p9kaRWVw676jjn/5+oon0vtklhT946XyKQWQvdWR52cMJ2uJaJYhyx+O2BajK80UA/gviWkAzceOOGjoCErEfV6tOtkBTRuABQEilEm8drX2QjTJciSRZn+VSk9hfvBwNGjM8zSAwuGRGzZ7GOFf6ptXCtD8KBLuDyAri0Iicn17Y/58pIywrOBNkX0eYN5l5n4L75Sk+o90+cZp08aiDkKqWbzrRFIEeElAPSWa1j9ORJMXxQ50TGUF6C86KIFAI43ekit5s4tdjTh0RNgc8jK2mMNdIqJsLPX8CpEMog1uhxsTdsqUDJ5dwIfP9vaPwcRtJxoVQim+jrgw84T5MXvYwb2buedkE6TlkvwAEZMg5i/7J8WqrBx5nvkwKu6oI0y7Hid4RPk0WjJMG9B0n8qOiMKh4PenaC4rkAMMD69FY0YVWbDO8i1D40EXWXOpI9JrY+RFvQ//pv4YLPBPqA6MGSiLZb6kwKjn6XzqWwOPaAOto88fU4i4bc3kJEf9QJ8wRceIXzK1PipwPCTGVDqeFgWF+5zsqcrFjqN8tFwvoEZlAmVfqVMOlE2KoFdOFHge7o7Y0wUV4btoc6P22I5hctqfq+83b1UfoDOW1j54CIzDl9auAdhDSg0GeWxYLN05Gkpdlzxr7zW5O1r6zWwQUc=',
            '_uetvid': '585254a04f3811ef97d963d720a86abe|1rpldn4|1723302517556|62|1|bat.bing.com/p/insights/c/s',
        }

        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9,ta;q=0.8,ml;q=0.7',
            'cache-control': 'no-cache',
            # 'cookie': 'optimizelyEndUserId=oeu1722428871713r0.24635694339567604; vi=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InYxIn0.eyJjaWQiOiIzOWUwNWRjZS01ZGE1LTQ1OWQtYjFhYi02ZDMyZDY1MjEyNzQiLCJpYXQiOjE3MjI0Mjg4NzF9.3dSRiEojdBDWZmyo6vtgvX2WurwyhKChUJDLIsqy2QA; mdeConsentDataGoogle=1; mdeConsentData=CQCkcIAQCkcIAEyAHADEA_FgAP_gAELAAAYgJepV5CzdbWFBcX53aPsgOY0X1tBTIsQhAhSAAyAFgBOQ8JQA02EyNASgBiACEAAAoxZBAAEEHABEAQCAQAAEAADMIgQEgAAIIABEgAEQAAJYAAoKAAAgEAAIgAIFEgAAmBiAIdLkXUCAgIAACgAQAAABAIAAAgMAAAAIAAMAAAAAQgAAAAAAAAIAAAAAARAAAAAAAAAAAAAAIF5wBAAQAA0ACYAvMAYJAvAAQAAsACoAHAAPAAyAB4AEQAKoAbwA9AB-AEIAIaARABEgCOAEsAJoAYAAwwB3AD2gH2AfoBFACNAEiAJKAXMAvQBigDaAG4ASIAnYBQ4CjwFIgLYAYaAyQBk4DMwGrgNZAcEA8cB7Q6BoAAsACoAHAAZAA8ACIAFWALgAugBiADeAHoAPwAhoBEAESAJYATQAowBgADDAGiAO4Ae0A-wD9AIoARYAjoBIgCSgFzgLyAvQBigDaAG4AOoAhABF4CRAE7AKHAUeAtgBhoDJAGTgMqAZYAzMBq4DiwHjgPaAgCQgJAALACqAFwAMQAbwA9ACOAGAAO4AigBKQC5gGKANoAdQBaIDJwHjkoDYACAAFgAcAB4AEQAKoAXAAxACGgEQARIAjgBRgDAAH4AXMAxQB1AEIAIvASIAo8BbADJAGTgMsAe0BAEpAoAAWABUADgAMgAeABEACkAFUAMQAfgBDQCIAIkAUYAwABowD7AP0AiwBHQCRAElALmAXkAxQBtADcAHUAReAkQBOwChwFsAMNAZIAycBlgDWQHBAPHAe0BDktAGAGAAO4AvQChwGZgPHA.YAAAAAAAD4AAAKcAAAAA; _ga=GA1.1.2106014981.1722428888; _gcl_au=1.1.1302666604.1722428889; FPID=FPID2.2.iixRz3ThUFc7BTZg0gpY4YFDhy1FhqzXDI9aSEpTBx0%3D.1722428888; _tt_enable_cookie=1; _ttp=XIf_Kf1kbzDe3SFsJbhSIC_j31s; _hjSessionUser_3567183=eyJpZCI6IjBhMjUwNTFiLWJkZTgtNWI5OC1hYzQ3LTE1NDU5YTUyZTg5MyIsImNyZWF0ZWQiOjE3MjI0Mjg4ODg5NTgsImV4aXN0aW5nIjp0cnVlfQ==; _fbp=fb.1.1723196113210.431422292237617949; _pubcid=20983fd1-726f-4ef1-8bb3-01a0599e4dd0; _pubcid_cst=8yyiLEEsMA%3D%3D; axd=4369192905572835944; __gsas=ID=b7bf26a155f6c3e1:T=1723196234:RT=1723196234:S=ALNI_MYAo2Q13crwPbRVwsOv9zWgZ3glAg; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22wIB6qwheHP5pXWRR2nba%22%7D; hsstp=1; __rtbh.uid=%7B%22eventType%22%3A%22uid%22%7D; mobile.LOCALE=de; tis=EP117%3A3989; _hjHasCachedUserAttributes=true; FPLC=R031AsqrDSjoQW6%2BBjokpDiAorgff7SUZ%2FftP2g1OMHnctuRCPGEjAdFW5VTP0itXHPyx%2FeZ9E%2FDozTtHWehOyT6f2J8ykvMJOAv6Sv1RoLX%2FwDKqkVcaeoszccXUw%3D%3D; _lr_sampling_rate=100; _hjSession_3567183=eyJpZCI6ImUxODgyZTlkLWY4Y2MtNGI4Yy1iZjNjLTNmZTVhOTk1YzQ4MiIsImMiOjE3MjMyOTM1NzYxNTgsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MX0=; bm_mi=9CF56EE83FF8B45E959DD059AC0F6F9E~YAAQIDwSAvhMUyiRAQAASJHBPBjap0XM33SsqdFgaC/Pj+xKz6U+P1KB+79Moy/L3rF9dzADh9x3sb+ZeYu94ZLOlw2KdGr68kYhQ9at+GFNVg8SDlpq5v8jvQKPn4fFBJ9anSsK5N+Xs8WFdXpWaF8dWy2FnN5t/9OyKZSxXk58c0yAT6kaY7O22QubQc14hNyA/cJ+HUQe9nxryFWpw6xL6mARIBmdmpe4mUWW+yWRSv5dFYiJZ3W3JvtDP7jniyvT8ZFTLagrl4524Gg4HyB4oBk4KAS/xDd5NOz6PpJ1sX4jqTPxItoJYfWPphJlmVwKH23frCmtc3nrnTCs3Tx08A==~1; ak_bmsc=29899BE5C8AC9BCF86D0936995068F82~000000000000000000000000000000~YAAQIDwSAqkdVCiRAQAAU9DRPBi42T/pNUFc2JgtJICvN9cRqQXb2OMcp9bIbq4GaKC+1Ch/4w9gQTZXWWuPpj4H+XZjvalzXDrZcSbPZ9ccVeOrq8IPjkITrsz4LWFWFIWXqonbiJByP97ZvyTqHyZZ5tY+w6PhlWSrzB1OsMAXrZwFjOpij9yUgkLEYr8kDgCxtCLEcKV7Y5oGz0nfBQixB8Ju8KA/P4QjyBVlsmDPyQR1yj/ZaNecB0Ga9B/OM/yPP/IaY04sSLYylhvADv/fQTff+nX3qxtEGwsBKY1CMPAeE1fp06nVraZjJ+t1UTLIquRwZvgEjeLcRHJkBrU13A5PuuU//IXanPbAERRnP0J1kawRcb5FGF/ERBahsLKmYhJURkxkED+KfrWNHunPGmtMhplnn7VE0l8S1gPgtqEv4P0lI8k97ARMyvRs9QAyYqnq1/FGJIfG4YaaURkPYlMaTuunQxsVB2dI7jNnTIXfQphdnmRwG2ILuri7y0TZR2sMhd5xUr5d8RRk+/1ADgJm2/sdigKbG7M7IBQSAIcm84F/WNV4lvqlKjYXq0h+ApZ8s/AIWmN25vo7u9kUjT0sdnYXQxoXU4yEFSqZRX+qMJAqGy+UHh5pT8wcL9SFjG2IFecF5KCcLodCPQeBGNwtG5g=; bm_sz=B2123C1CDC6AF165BAD98F0764B6A9D5~YAAQIDwSAqsdVCiRAQAAU9DRPBgaE3ljhG5K+3eSBMMHVMH5hRhykBV53JmM+VlsA6kqmPaHEiTeEnM9kcg5QieUE0VkbIchUCvK8GCqmftE3e1F41vZsJ/gKPGM5G1IffTd/TPXZ7cn56A5Tl8NBnt8TU6ch81d/MhrNYia+X6pRSot8dVeBhTC5Mhaxh83xTU7BOHyODtS2OhqfpeIPbVnVlsHIHZVJ74TK3UQ2jZXe2VZam7f0w4IYckONDCOm4V4/HOlYye0BWCchWt3TNdF+/g9gxoLcuZMm9KI63ZuMe6oi8aadDbvaemhQpWTRfixrrDF5Rhxdfc6zdrPGgjQQQ+uvZ53PicOxndBEGBhM0rDIAkDYJ0wfEYttl3ICNRHNQwS7FPH+m5IUaR92daae/FBQXNe92/ZY0+wNItyw4JR4XJ7BcSbqL/1E/az7R2Ehvw1R9cy5j6UjW0J0Pn8AMd5R1Sh+4qdaIl3byqvCcOSmz3h6FfV1deEWKlLNMDRO93AWMtNS4bcXNHkmKNjO9VLn4LhA0jVTXk+ZVUUstDxlKA=~4338740~3224889; ces={%22lv%22:[1723302271525%2C1723299725868%2C1723297272593%2C1723295383588%2C1723293571426%2C1723288003762%2C1723285615501%2C1723283426535%2C1723280783811%2C1723277487650%2C1723198159255%2C1723196232667]}; __gads=ID=0442cca318e7d640:T=1722428886:RT=1723302273:S=ALNI_MaaS2KEZjpF4REgfbwA6wV5PJajzg; __gpi=UID=00000eaf5a116303:T=1722428886:RT=1723302273:S=ALNI_MbJ6p09t10eFJWl-zlZrwr_IBLw3w; __eoi=ID=56b1b9069d604832:T=1722428886:RT=1723302273:S=AA-Afjbxw0H4GEGXbsfqtpftYv1i; cess={%22s%22:41%2C%22nsf%22:1%2C%22v%22:36}; _ga_2H40T2VTNP=GS1.1.1723293573.9.1.1723302508.0.0.1839722994; cto_bundle=D-hWr19BcjR0R2EzNkFORWd1SjB1Y1lUbW5QRyUyQlNVM3BEVjVVcndhVjFDaTJFbXJsZU5sTWhqbXNua0FoMzF3WjdtaG5HRGR4ck5lemgyWk1EdndOdTRGTFBoT0JjZ3RRa1pwbkpjczljNlFSd2Z4ZDlIJTJGdmFEaHFubFRuUGx3a2tRb2l5SzIlMkZJd0xremRrU0YlMkY2UWxsQ3RLVXpyODhJdDFHTkJnaFZiOEh5clF3dVNQSkJrbm5XOEFYT0R5MW9XRiUyQnVxeDlmYzNmZyUyRkNiMWo1amNxWWtGJTJCb3clM0QlM0Q; _uetsid=af2271d0563211ef9906ffb7cb19b63c|ubyrfj|2|fo7|0|1682; dicbo_id=%7B%22dicbo_fetch%22%3A1723302515043%7D; _abck=33AF85381E6E77D59AECD881A1C31EED~-1~YAAQIDwSAtdSVCiRAQAAq5XVPAzfXZRVYHqIyXEQjZmu6jx42FP5N0IVAK3WssWII6YgeT/mNIbtscqEfBz/8o9nL0vvjoyoTREihSsk3lpKJFfExo0Pg+d5oYDkPaIp7+rh/lvnFdpEd/elOSIP6lW47gSTkqMu4r9KE6mjUAgdQITEokGH4qVhVLJYzC+PY8S8eLT6oXDOPbA0wuYcF0qIlUO7b4m5w/+RxkfxE781XY+UjmdL4j/LfJ9VnWvqFkoDaDAqwglijzwTzz0H44fQW4B/73uaX3IrNV7m8VasTqAQPFGhQf4qFDgy8ai7TGLKHc4zBWZU+d9jRQg7+gPZ1TriJkOTfSEMx7ItdtyDHIQboKfudRAuBdLsKzJBat/diY6pNGNVVNDRCifgJvZH3YDO8CJxPc03FeiNVW4Ta19nAs4W2hFiXNri1AIPfATKjkKU5Ziu0uKXrtB6RGIylg==~0~-1~-1; bm_sv=40E7BBEFF25802A7779D90024017BBA0~YAAQIDwSAthSVCiRAQAAq5XVPBiN6UFjoXSR3nNKjEMUMWwCyPEb0+izoYGnJq41gJlI1obATylLj11seApypxxQA9ZPvaC2NCOrDtF0SBwD1cLQXWEdadoRH/xESbh77KAFeEqp2Y4OXFXp+KCC2BCOcFVQK+VX/Nv4Unil6bw5YfsRN1JYiPbsQB0Ft+MnlaZpMw+oH5mK2xF/2MWOQ42nFDjvuy+DPUCKILqL+tw0AFXG8/aBfmIMpJCIkwfm~1; sec_cpt=24738D10D1DC3198A601140BA43D4631~1~YAAQIDwSAtlSVCiRAQAAq5XVPAu+ZzFmNymKQx85dnQtw5OAKsGRot+i3Wz7WBMEvs5i0BJxUMJcB9SGjjwnneBgTHBAPaQ+uKA5xkm0Ifmuq3rf/NlNAj3+uSx8W4N7NHZ/+4BJok5ntqn/XKIZawY1MX1nUVCdrrHjBkOjKhcJA8jO9oXOdej7lSzD94xIGaBis4bE0SOoArRgpJKJBPWkGWCkOWu2lhrwbmMgyg5N9sYIw5JV3kz9u/KH+lmvr2Cvw9Wi/sDsN5pa2j3RnDKk2jkcJHfcwdkcWPb7QOMvVhe3ktRTvvCzkcNOqdq9q54gRPoAwqLIpj1mhlb4PpFqZKOj0IJVy53VWkZVJIvRlHaj9IGUc3lPQ3KTuTjvz6FQx4n0PECcIaWUpvbFyBxo0zNCljzZRi1AdVD0gp3n56OfMg1nNjJ6JyJCo9ZaexE9LunDtjqybG2QnvVjKJxJX8ArasudyWeYjqtTdJH186SmNECV6p9kaRWVw676jjn/5+oon0vtklhT946XyKQWQvdWR52cMJ2uJaJYhyx+O2BajK80UA/gviWkAzceOOGjoCErEfV6tOtkBTRuABQEilEm8drX2QjTJciSRZn+VSk9hfvBwNGjM8zSAwuGRGzZ7GOFf6ptXCtD8KBLuDyAri0Iicn17Y/58pIywrOBNkX0eYN5l5n4L75Sk+o90+cZp08aiDkKqWbzrRFIEeElAPSWa1j9ORJMXxQ50TGUF6C86KIFAI43ekit5s4tdjTh0RNgc8jK2mMNdIqJsLPX8CpEMog1uhxsTdsqUDJ5dwIfP9vaPwcRtJxoVQim+jrgw84T5MXvYwb2buedkE6TlkvwAEZMg5i/7J8WqrBx5nvkwKu6oI0y7Hid4RPk0WjJMG9B0n8qOiMKh4PenaC4rkAMMD69FY0YVWbDO8i1D40EXWXOpI9JrY+RFvQ//pv4YLPBPqA6MGSiLZb6kwKjn6XzqWwOPaAOto88fU4i4bc3kJEf9QJ8wRceIXzK1PipwPCTGVDqeFgWF+5zsqcrFjqN8tFwvoEZlAmVfqVMOlE2KoFdOFHge7o7Y0wUV4btoc6P22I5hctqfq+83b1UfoDOW1j54CIzDl9auAdhDSg0GeWxYLN05Gkpdlzxr7zW5O1r6zWwQUc=; _uetvid=585254a04f3811ef97d963d720a86abe|1rpldn4|1723302517556|62|1|bat.bing.com/p/insights/c/s',
            'pragma': 'no-cache',
            'priority': 'u=0, i',
            'referer': 'https://suchen.mobile.de/fahrzeuge/details.html?id=390721906&action=topOfPage&isSearchRequest=true&lst=p&od=down&ref=srp&refId=223dcabe-8102-a174-741c-a8fcbea99cc8&s=Car&sb=doc&searchId=223dcabe-8102-a174-741c-a8fcbea99cc8&vc=Car',
            'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
        }

        # Properly format the string into a JSON object
        data = response.css('body.body script::text').get()
        data = data.replace("window.__INITIAL_STATE__ = ", '"key1":')
        data = data.replace("window.__PUBLIC_CONFIG__ = ", ',"key2":')
        data = "{" + data + "}"
        # Now try to load the JSON
        data = json.loads(data)
        page_props = data['key1']['search']['srp']['data']['searchResults']['items']

        i = 0
        for item in page_props:
            if item['type'] == 'topAd' or item['type'] == 'ad':

                yield {'make': item['make'],
                       'model' : item['model'],
                       'derivative' : item['title'],
                       'derivative_english' : item['title'],
                       'number_of_doors': item['attr']['door'],
                       'body_type': item['category'],
                       'power_train': item['attr']['ft'],
                       'Version_Name' : item['make'] + item['model'] + item['title'] + item['attr']['door'] + item['category'] + item['attr']['ft'],
                       'Version_Name_translated_english' : item['make'] + item['model'] + item['title'] + item['attr']['door'] + item['category'] + item['attr']['ft'],
                       'Currency' : item['price']['grossCurrency'],
                       'Price': item['price']['gross'],
                       'Delivery Costs - Retail' : 'Keine Angabe',
                       'Country': item['contactInfo']['country'],
                       'Research Date': '11.08.2024',
                       'Customer Type': item['leasingRate']['type'],
                       'Monthly Payment Type' : 'BALLOON',
                       'Product Name' : item['contactInfo']['name'],
                       'Monthly Payment Provider Name': 'Santander Carcredit',
                       'Monthly Payment Provider Type': 'Check24 GmbH',
                       'interest rate apr': '5,99%',
                       'Interest Rate Nominal' : '5,83%',
                       'Contract Duration (Months)': item['leasingRate']['termOfContract'],
                       'Yearly Mileage (Km)': f"{item['leasingRate']['annualMileage']:,}",
                       'Yearly Mileage (Miles)': f"{item['leasingRate']['annualMileage'] * 0.621371:,}",
                       'Total Contract Mileage (Km)': f"{item['leasingRate']['annualMileage'] * (item['leasingRate']['termOfContract'] / 12):,.2f}",
                       'Total Contract Mileage (Miles)': f"{item['leasingRate']['annualMileage'] * (item['leasingRate']['termOfContract'] / 12) * 0.621371:,.2f}",
                       'Deposit_retail': item['leasingRate']['downPayment'],
                       'Deposit (% Of Price)': f"{(float(item['leasingRate']['downPayment']) / float(item['price']['gross'].replace('€', '').replace('.', '').replace(',', '.').strip())) * 100:,.2f}",
                       '# Of Monthly Instalments': item['leasingRate']['termOfContract'],
                       'Regular monthly instalment amount - retail' : item['leasingRate']['grossRate'],
                       'Additional Fees - Retail': item['leasingRate']['downPayment'],
                       'Data Source' : 'Market',
                       'Web Source Url' : 'https://suchen.mobile.de/' + item['relativeUrl'],
                       'other source': 'Market',
                       'Vehicle Price Reference' : item['price']['netAmount'],
                       'Insurance': 'Check24 GmbH',
                       'Insurance Description' : "CHECK24's car insurance comparison is the only one in Germany to have achieved more than 15 test victories, most recently in the study 'Car insurance comparison portals' (€uro am Sonntag, issue 01/22).",
                       'Reimbursement mileage - retail': response.css('dd.nI7AA span::text').get(default='Not Available').strip(),


                }
                i += 1
            elif item['type'] == 'page1Ads':
                for sub_data in item['items']:
                    yield{'make':sub_data['make'],
                          'model':sub_data['model'],
                          'derivative':sub_data['title'],
                          'derivative_english':sub_data['title'] ,
                          'number_of_doors': sub_data['attr']['door'],
                          'body_type':sub_data['category'],
                          'power_train': sub_data['attr']['ft'],
                          'Version_Name': sub_data['make'] + sub_data['model'] + sub_data['title'] + sub_data['attr']['door'] + sub_data['category'] + sub_data['attr']['ft'],
                          'Version_Name_translated_english' : sub_data['make'] + sub_data['model'] + sub_data['title'] + sub_data['attr']['door'] + sub_data['category'] + sub_data['attr']['ft'],
                          'Currency': sub_data['price']['grossCurrency'],
                          'Price': sub_data['price']['gross'],
                          'Delivery Costs - Retail': 'Keine Angabe',
                          'Country': sub_data['contactInfo']['country'],
                          'Research Date': '11.08.2024',
                          'Customer Type': sub_data['leasingRate']['type'],
                          'Monthly Payment Type' : 'BALLOON',
                          'Product Name': sub_data['contactInfo']['name'],
                          'Monthly Payment Provider Name' : 'Santander Carcredit',
                          'Monthly Payment Provider Type' : 'Check24 GmbH',
                          'interest rate apr': '5,99%',
                          'Interest Rate Nominal': '5,83%',
                          'Contract Duration (Months)' : sub_data['leasingRate']['termOfContract'],
                          'Yearly Mileage (Km)': f"{sub_data['leasingRate']['annualMileage']:,}",
                          'Yearly Mileage (Miles)': f"{sub_data['leasingRate']['annualMileage'] * 0.621371:,}",
                          'Total Contract Mileage (Km)': f"{sub_data['leasingRate']['annualMileage'] * (sub_data['leasingRate']['termOfContract'] / 12):,.2f}",
                          'Total Contract Mileage (Miles)': f"{sub_data['leasingRate']['annualMileage'] * (sub_data['leasingRate']['termOfContract'] / 12) * 0.621371:,.2f}",
                          'Deposit_retail' : sub_data['leasingRate']['downPayment'],
                          'Deposit (% Of Price)': f"{(float(sub_data['leasingRate']['downPayment']) / float(sub_data['price']['gross'].replace('€', '').replace('.', '').replace(',', '.').strip())) * 100:,.2f}",
                          '# Of Monthly Instalments' : sub_data['leasingRate']['termOfContract'],
                          'Regular monthly instalment amount - retail': sub_data['leasingRate']['grossRate'],
                          'Additional Fees - Retail' : sub_data['leasingRate']['downPayment'],
                          'Data Source': 'Market',
                          'Web Source Url': 'https://suchen.mobile.de/' + sub_data['relativeUrl'],
                          'other source' : 'Market',
                          'Vehicle Price Reference': sub_data['price']['netAmount'],
                          'Insurance' : 'Check24 GmbH',
                          'Insurance Description': "CHECK24's car insurance comparison is the only one in Germany to have achieved more than 15 test victories, most recently in the study 'Car insurance comparison portals' (€uro am Sonntag, issue 01/22).",
                          'Reimbursement mileage - retail': response.css('dd.nI7AA span::text').get(default='Not Available').strip()
                          }
            else:
                i += 1
                continue
