import pandas as pd
import requests
from bs4 import BeautifulSoup

final_df=pd.DataFrame()

for j in range(1,101):
    url = 'https://www.ambitionbox.com/list-of-companies?campaign=mob_hamburger&page={}'.format(j)
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
    website = requests.get(url,headers=headers).text

    soup=BeautifulSoup(website,'lxml')

    box = soup.find_all('div', attrs={'data-testid': True})

    name = []
    rating = []
    reviews = []
    sal = []
    interview = []
    job = []

    for i in box:
        if i.get('data-testid', '').startswith('loc-company-card-'):

            name_tag = i.find('h2')
            rating_tag = i.find('span', class_="text-primary-text font-pn-700 text-sm !text-[14px] !leading-[14px]")
            reviews_tag = i.find('a', href=lambda x: x and '/reviews/' in x)
            sal_tag = i.find('a', href=lambda x: x and '/salaries/' in x)
            intv_tag=i.find('a',href=lambda x: x and '/interviews/' in x)
            job_tag=i.find('a',href=lambda x:x and '/jobs/' in x)

            name.append(name_tag.text.strip() if name_tag else None)
            rating.append(rating_tag.text.strip() if rating_tag else None)
            interview.append(intv_tag.find('span').text.strip() if intv_tag else None)
            reviews.append(reviews_tag.text.strip() if reviews_tag else None)
            sal.append(sal_tag.find('span').text.strip() if sal_tag else None)
            job.append(job_tag.find('span').text.strip() if job_tag else None)

    d={'name':name,'rating':rating,'interview':interview,'reviews':reviews,'sal':sal,'job':job}
    df = pd.DataFrame(d)
    final_df = pd.concat([final_df, df], ignore_index=True)

print(final_df)
print(final_df.shape)

final_df.to_csv('WebScarpedJobsData.csv')