# IMAX_res_notice
Yongsan IMAX reservation notification service

---
#### [cgv 홈페이지]
<img width="807" alt="스크린샷 2022-03-26 오후 4 31 10" src="https://user-images.githubusercontent.com/79912683/160229617-529d781b-5766-4426-9f84-d3b52e653ce4.png">

---
#### [기본작업]
> ~~~python
> -pip3 install bs4 requests
> -pip3 install python-telegram-bot
> -pip3 install apscheduler
> ~~~

#### [chrome 개발자도구 활용]
* 제목위치
<img width="424" alt="스크린샷 2022-03-26 오후 3 01 59" src="https://user-images.githubusercontent.com/79912683/160229750-433648f6-17f2-4a69-9076-d7817a404f8f.png">
* IMAX 예매 여부
<img width="248" alt="스크린샷 2022-03-26 오후 3 04 04" src="https://user-images.githubusercontent.com/79912683/160229759-f64e38fb-d659-48c6-9750-a876b4956750.png">

#### [telegram bot]
~~~python
import telegram
bot=telegram.Bot(token='token정보')
~~~
* 개인 아이디 확인
~~~python
for i in bot.getUpdates():
  print(i.message) # 봇으로 메시지 보내면 개인 ID 확인 가능
~~~
* python으로 개인에게 메시지 보내기
~~~python
bot.sendMessage(chat_id=개인ID,text='message')
~~~

#### [작업 정의]
~~~python
def job():
  html=requests.get(url) # url : cgv예매정보 웹 주소
  soup=BeautifulSoup(html.text,'html.parser')
  imax=soup.select_one('span.imax') # IMAX 정보
  if imax: # IMAX 예매가 오픈되어 있다면
    imax=imax.find_parent('div',class_='col-times') # 부모요소로 올라가기
    title=imax.select_one('div.info-movie>a>strong').text.strip() # 부모요소로부터 info-movie,a,strong에 제목있음
    bot.sendMessage(chat_id=개인ID,text=title+" IMAX 예매가 열렀습니다.")
~~~

#### [aws_ec2 서버에 python 올리기]
* 서버
<img width="719" alt="스크린샷 2022-03-26 오후 4 48 47" src="https://user-images.githubusercontent.com/79912683/160230153-92fcfd25-68cb-499f-a2ff-3ac10ae3da44.png">

* FileZilla로 파일 업로드
<img width="1072" alt="스크린샷 2022-03-26 오후 4 18 43" src="https://user-images.githubusercontent.com/79912683/160230184-7b682713-286f-4b2c-b569-4c73c06cc117.png">

* ubuntu
~~~python
# 접속
-ssh -i keyname.pem ubuntu@server_public_IP address
# terminal 종료 후에도 서버내에서 계속 작동
-python3 IMAX_notice_server.py &
# 작업 확인
-ps -ef
# 작업 종료
-kill 작업번호
~~~

---
#### [결과]
![IMG_2491](https://user-images.githubusercontent.com/79912683/160230402-e52c0a04-a1af-4766-9b05-314e1350379a.jpg)
