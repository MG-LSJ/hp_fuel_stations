# A python script to scrape xml data from the web and save the files asynchronusly

import asyncio
import aiohttp

# update CSRFToken_req and customCookies from the browser
# (inspect element -> network -> headers)
# after filling captcha
baseurl = "https://hproroute.hpcl.co.in/ROAlongRoute/RoInRadius_data_dt_plus.jsp?CSRFToken_req=dgIOpDZkABoLtlJw5G7tT5gDiAMwJakJEWWO5fR9&product_type=MS&facility=any&selected_facilities_names=MS_HSD&Q=2&D="
customCookies = "JSESSIONID=1D684E900C42CFBE39A02EE104A8D1AD; ARRAffinity=86e595c4aa68ec591401e542e321ea10a4cc53823a04e2964d767c4e56df5063"
host = "hproroute.hpcl.co.in"
refrer = "https://hproroute.hpcl.co.in/ROAlongRoute/index.jsp"


headers = {
    "Host": host,
    "Referer": refrer,
    "User-Agent": "Mozilla/5.0",
    "Cookie": customCookies,
}


async def fetch(s: aiohttp.ClientSession, url):
    async with s.get(url=url, headers=headers) as response:
        return await response.read()


async def fetch_all(s: aiohttp.ClientSession):
    tasks = []
    for i in range(1, 806):
        url = baseurl + str(i).zfill(4)
        tasks.append(asyncio.create_task(fetch(s, url)))
    return await asyncio.gather(*tasks)


async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch_all(session)
        for i in range(1, 806):
            filename = "data/" + str(i).zfill(4) + ".xml"
            file = open(filename, "wb")
            file.write(html[i - 1])
            file.close()


asyncio.run(main())
