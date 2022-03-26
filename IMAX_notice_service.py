import requests
import telegram
from bs4 import BeautifulSoup
from apscheduler.schedulers.blocking import BlockingScheduler

bot=telegram.Bot(token='5266266718:AAGFHq4ytu1u_hBxFPiKKGD0a1ZHkRd0OC8')
url='http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20220402'
def job():
    html=requests.get(url)
    soup=BeautifulSoup(html.text,'html.parser')
    imax=soup.select_one('span.imax')
    if imax:
        imax=imax.find_parent('div',class_='col-times')
        title=imax.select_one('div.info-movie>a>strong').text.strip()
        bot.sendMessage(chat_id=5179415817,text=title+" IMAX 예매가 열렸습니다.")
        sched.pause()

sched=BlockingScheduler(timezone='Asia/Seoul')
sched.add_job(job,'interval',seconds=30)
sched.start()
