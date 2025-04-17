import requests
from lxml import etree
from openai import OpenAI
url='题目链接'

myheaders={
'cookie':
'your cookie',#这里输入网页的cookie
'user-agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0'

}
#这里要输入自己的人工智能API接口
client = OpenAI(api_key="API", base_url="https://api.deepseek.com")

response=requests.get(url,headers=myheaders)
#print(response.status_code)
tree=etree.HTML(requests.get(url,headers=myheaders).text)
divs=tree.xpath('//div[@class="marBom60 questionLi singleQuesId"]')
#(divs)
for div in divs:
    di=div.xpath('.//span[@class="qtContent workTextWrap"]/p/text()')
    str1="".join(di)
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": f"{str1}"},
        ],
        stream=False
    )
    print(response.choices[0].message.content)




