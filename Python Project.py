#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests


# In[2]:


from bs4 import BeautifulSoup 


# In[4]:


html_data = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=Home_Search&from=submit&asKey=OFF&txtKeywords=&cboPresFuncArea=35").text
print (html_data)


# In[5]:


soup_data = BeautifulSoup(html_data,'lxml')


# In[6]:


print(soup_data)


# In[7]:


all_jobs = soup_data.find_all('li',class_='clearfix job-bx wht-shd-bx') 


# In[8]:


base_url='https://www.timesjobs.com/candidate/job-search.html?from=submit&searchType=Home_Search&luceneResultSize=25&postWeek=60&cboPresFuncArea=35&pDate=Y&sequence=1&startPage='


# In[9]:


url_lst=[]
job_link = 'https://www.timesjobs.com/'
for item in range(1,101):
    url_lst.append(base_url+str(item)) 


# In[10]:


for url in url_lst:
    print(url)


# In[14]:


all_jobs_lst = []
a=1
web_url = 'https://www.timesjobs.com/candidate/job-search.html?from=submit&searchType=Home_Search&luceneResultSize=25&postWeek=60&cboPresFuncArea=35&pDate=Y&sequence='
end_urls = '&startPage='

for i in range(1,50):
    if(i > a+9):
        a=a+10
    url = web_url+str(i)+end_urls+str(a)
    html_data = requests.get(url).text
    soup_data = BeautifulSoup(html_data,'lxml')
    all_divs = soup_data.find_all('li',class_='clearfix job-bx wht-shd-bx')
    for item in all_divs:
        Job_Link = item.find('a',target="_blank")['href']
        Job_Title = item.find('a',target="_blank").text
        cname = item.find('h3',class_='joblist-comp-name').text
        csplit = cname.split('(')
        company_name = csplit[0].strip()
        company_skills = item.find('span',class_='srp-skills').text
        company_exp = item.find('ul',class_='top-jd-dtl clearfix').text
        csplit = cname.split('(')
        company_name = csplit[0].strip()

        companys = company_exp.split('\n')

        cexp = companys[1]
        csal = companys[2]
        if(companys[3] == 'location_on'):
            cloc = companys[4]
        else:
            cloc = companys[5]
            x = cexp.split('l')

        company_job_des = item.find('ul',class_='list-job-dtl clearfix')
        company_job = company_job_des.find('li').text

        company_job_des = company_job.split(':')
        company_job_de = company_job_des[1].strip()
        
        company_job_desc=company_job_de[0:y-12]
        first_page_prodcut = {
            'Company Name':company_name,
            'Job Title':Job_Title.strip(),
            'Job Skills':company_skills.strip(),
            'Salary':csal,
            'Location':cloc,
            'Job Description':company_job_desc,
            'Job Link':Job_Link
        }
        all_jobs_lst.append(first_page_prodcut)
    
print(all_jobs_lst)


# In[15]:


import pandas as pd  


# In[16]:


df = pd.DataFrame(all_jobs_lst)


# In[17]:


df


# In[19]:


df.to_excel('TIMES_JOB_DATA.xlsx')


# In[ ]:




