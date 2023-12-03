# import requests
# import pandas as pd
# from bs4 import BeautifulSoup

# html=requests.get("https://www.updateurself.com/2018/11/14/the-way-to-challenge/").text
# soup=BeautifulSoup(html,"html.parser")
# for script in soup(["script", "style"]):
#     script.decompose()
# #print(soup)

# text=soup.get_text()
# lines= [line.strip() for line in text.splitlines()]
# lines=[]
# for line in text.splitlines():
#     lines.append(line.strip())
# text="\n".join(line for line in lines if line)
# print(text)

import numpy as np

num_digitized = 4 #各状態の離散数
max_number_of_steps = 200 #1試行のstep数(コマ数)



q_table = np.random.uniform(low=-1, high=1, size=(num_digitized**num_digitized, 2))
print(q_table)