#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os


# In[2]:


os.getcwd()


# In[3]:


from selenium import webdriver
from bs4 import BeautifulSoup


# In[4]:


driver = webdriver.Chrome('chromedriver_90')


# In[5]:


url = 'https://www.amazon.com/'
driver.get(url)


# In[6]:


sel_search = driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')
sel_btn = driver.find_element_by_xpath('//*[@id="nav-search-submit-button"]')

print(sel_search.tag_name, sel_btn.tag_name)


# In[7]:


sel_search.clear()
sel_search.send_keys("kindle")
sel_btn.click()


# In[8]:


page = driver.page_source
soup = BeautifulSoup(page, "html.parser")
soup.title


# In[13]:


url = "https://www.amazon.com/All-new-Kindle-Oasis-now-with-adjustable-warm-light/dp/B07F7TLZF4/ref=sr_1_1?dchild=1&amp;keywords=kindle&amp;qid=1624257040&amp;sr=8-1"
driver.get(url)


# In[14]:


import time
time.sleep(3)


# 전체 평점 확인

# In[15]:


sel_rate = driver.find_element_by_xpath('//*[@id="acrCustomerReviewText"]')
sel_rate.click()


# 전체 리뷰 확인

# In[16]:


sel_all_reviews = driver.find_element_by_xpath('//*[@id="reviews-medley-footer"]/div[2]/a')
sel_all_reviews.click()


# In[17]:


page = driver.page_source
soup = BeautifulSoup(page, 'lxml')
soup.title


# In[19]:


all_r = soup.find_all("span", class_='a-size-base review-text review-text-content')
len(all_r)
all_r[0].text.strip()


# In[20]:


all_reviews = []

for one in all_r:
    tmp = one.text
    review = tmp.strip()
    all_reviews.append(review)
    
all_reviews


# In[21]:


import pandas as pd


# In[23]:


dat_r = {'review':all_reviews}
dat = pd.DataFrame(dat_r)
dat


# In[24]:


dat.to_csv("kindle_reviews.csv", index=False)


# ### 하나의 제품에 대하여 작성된 리뷰들을 여러 페이지에서 가져오기

# In[25]:


sel_all_reviews2 = driver.find_element_by_xpath('//*[@id="cm_cr-pagination_bar"]/ul/li[2]/a')
sel_all_reviews2.click()


# In[26]:


page = driver.page_source
soup = BeautifulSoup(page, 'lxml')
soup.title


# In[27]:


all_r2 = soup.find_all("span", class_='a-size-base review-text review-text-content')
all_r2[0].text


# In[33]:


all_reviews2 = []

for one in all_r2:
    tmp = one.text
    review2 = tmp.strip()
    all_reviews2.append(review2)
    
print("리뷰 개수 : ", len(all_reviews2))
print(all_reviews2, sep='\n')


# In[32]:


import os, warnings
import re
warnings.filterwarnings(action = 'ignore')


# 사용자 추가

# In[34]:


soup.find_all("span", class_='a-profile-name')[-1].text


# 평점 가져오기

# In[35]:


all_r2 = soup.find_all("div", class_='a-section celwidget')
all_r2[0].find("span", class_='a-icon-alt').text


# 날짜

# In[36]:


tmp = all_r2[0].find("span", class_="a-size-base a-color-secondary review-date").text
texts = tmp.split("on")
texts[1].strip()


# 지역 정보

# In[37]:


tmp = all_r2[0].find("span", class_="a-size-base a-color-secondary review-date").text
texts = tmp.split("on")
texts[0].strip()


# 한 페이지의 정보 가져오기

# In[48]:


all_r2 = soup.find_all("div", class_="a-section celwidget")

all_users = [] # 사용자
all_ratings = []  # 평점
all_dates = []  # 날짜
all_regions = [] # 지역
all_reviews = [] # 리뷰

for one in all_r2:
    user_one = one.find("span", class_="a-profile-name").text
    all_users.append(user_one)  # 사용자 추가
    
    rating_one = one.find("span", class_="a-icon-alt").text
    nums = re.findall("\d+", rating_one)[0]
    all_ratings.append(nums)  # 평점 추가
    
    date_one = one.find("span", class_="a-size-base a-color-secondary review-date").text
    texts = date_one.split("on")
    data = texts[1].strip()
    all_dates.append(data) # 날짜 추가
    
    region_one = one.find("span", class_="a-size-base a-color-secondary review-date").text
    texts = date_one.split("on")
    region = texts[0].strip()
    all_regions.append(region)
    
    review_one = one.find("span", class_="a-size-base review-text review-text-content")
    tmp = review_one.text
    review = tmp.strip()
    all_reviews.append(review)  # 리뷰 추가
    
print(all_users)
print(all_ratings)
print(all_dates)
print(all_regions)
print(all_reviews)


# 여러 페이지에서 리뷰 가져오기

# In[55]:


all_users = [] # 사용자
all_ratings = []  # 평점
all_dates = []  # 날짜
all_regions = [] # 지역
all_reviews = [] # 리뷰

for one in range(2,7,1):
    time.sleep(3)
    
    page = driver.page_source
    soup = BeautifulSoup(page, 'html.parser')
    all_r2 = soup.find_all("div", class_="a-section celwidget")
    
        
    for one in all_r2:
        # 사용자 추가
        user_one = one.find("span", class_="a-profile-name").text
        all_users.append(user_one)
    
        # 평점 추가
        rating_one = one.find("span", class_="a-icon-alt").text
        nums = re.findall("\d+", rating_one)[0]
        all_ratings.append(nums)
        
        # 날짜 추가
        date_one = one.find("span", class_="a-size-base a-color-secondary review-date").text
        texts = date_one.split("on")
        data = texts[1].strip()
        all_dates.append(data) 
        
        # 지역 추가
        region_one = one.find("span", class_="a-size-base a-color-secondary review-date").text
        texts = date_one.split("on")
        region = texts[0].strip()
        all_regions.append(region) 
        
        # 리뷰 추가
        review_one = one.find("span", class_="a-size-base review-text review-text-content")
        tmp = review_one.text
        review = tmp.strip()
        all_reviews.append(review)
        
    # 확인
    print("user :", all_users[-1], "rating :", all_ratings[-1])
    print("review :", all_reviews[-1], end="\n\n\n")
    
    # 다음 페이지 클릭
    sel_next = driver.find_element_by_xpath('//*[@id="cm_cr-pagination_bar"]/ul/li[2]/a')
    sel_next.click()
    
print(all_users)
print(all_ratings)
print(all_dates)
print(all_regions)
print(all_reviews)


# In[64]:




dic = { "user":all_users, "rating":all_ratings, "date":all_dates, "region":all_regions, "review":all_reviews }
dat = pd.DataFrame(dic, columns=['user','rating','date','region','review'])

dat.to_csv("20210621_kindle_reviews.csv", index=False, encoding="utf-8")
dat


# In[ ]:




