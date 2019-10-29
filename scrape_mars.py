#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import dependencies
from splinter import Browser
from bs4 import BeautifulSoup 
import pandas as pd
import time


# ### NASA Mars News

# In[2]:

def scrape():

	# Visit Nasa URL through splinter and parse HTML with beautiful soup
	executable_path = {'executable_path': 'chromedriver.exe'}
	browser = Browser('chrome', **executable_path, headless=False)
	url = 'https://mars.nasa.gov/news/'
	browser.visit(url)
	html = browser.html
	soup = BeautifulSoup(html, 'html.parser')


	# In[3]:


	# Scrape the site and collect the latest News Title and Paragraph Text.
	news= soup.find("div", class_="list_text")
	mars_title=news.find("div", class_="content_title").get_text()
	mars_p=news.find("div", class_="article_teaser_body").get_text()
	print(mars_title)
	print(mars_p)


	# In[4]:


	browser.quit()


	# ### JPL Mars Space Images - Featured Image

	# In[5]:


	# Visit Nasa URL through splinter and parse HTML with beautiful soup
	executable_path = {'executable_path': 'chromedriver.exe'}
	browser = Browser('chrome', **executable_path, headless=False)
	url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
	browser.visit(url)
	html = browser.html
	soup = BeautifulSoup(html, 'html.parser')


	# In[6]:


	# Navigate the site to display the full size .jpg image
	browser.click_link_by_id('full_image')


	# In[7]:


	button = 'more info     '
	time.sleep(3)
	browser.find_by_text(button).click()


	# In[8]:


	# Parse the new html page with beautiful soup and retrieve url string for the image
	html=browser.html
	soup = BeautifulSoup(html, 'html.parser')
	url=soup.find("img",class_= "main_image")['src']
	featured_url='https://www.jpl.nasa.gov'+url
	featured_url


	# In[9]:


	browser.quit()


	# ### Mars Weather

	# In[10]:


	# Visit  URL through splinter and parse HTML with beautiful soup
	executable_path = {'executable_path': 'chromedriver.exe'}
	browser = Browser('chrome', **executable_path, headless=False)
	url = 'https://twitter.com/marswxreport?lang=en'
	browser.visit(url)   
	html = browser.html
	soup = BeautifulSoup(html, 'html.parser')


	# In[11]:


	# scrape the latest Mars weather tweet from the page.
	#data=soup.find("div",class_="js-tweet-text-container").get_text()
	mars_weather=soup.find("p",class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
	mars_weather


	# In[12]:


	# replace \n with , and display data
	mars_weather = ",".join(mars_weather.split("\n"))
	mars_weather


	# In[13]:


	browser.quit()


	# ### Mars Hemispheres

	# In[14]:


	# Visit URL through splinter and parse HTML with beautiful soup
	executable_path = {'executable_path': 'chromedriver.exe'}
	browser = Browser('chrome', **executable_path, headless=False)
	#browser = webdriver.Chrome('./chromedriver')
	url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
	browser.visit(url)   
	html = browser.html
	soup = BeautifulSoup(html, 'html.parser')


	# In[15]:


	items = soup.find_all('div', class_='description')

	# Create empty list for hemisphere urls 
	hemisphere_image_urls = []

	# Store the main_ul 
	hemispheres_main_url = 'https://astrogeology.usgs.gov'

	# Loop through the items previously stored
	for i in items: 
		# Store title
		title = i.find('h3').text
		
		# Store link that leads to full image website
		partial_img_url = i.find('a', class_='itemLink product-item')['href']
		
		# Visit the link that contains the full image website 
		browser.visit(hemispheres_main_url + partial_img_url)
		
		# HTML Object of individual hemisphere information website 
		partial_img_html = browser.html
		
		# Parse HTML with Beautiful Soup for every individual hemisphere information website 
		soup = BeautifulSoup( partial_img_html, 'html.parser')
		
		# Retrieve full image source 
		img_url = hemispheres_main_url + soup.find('img', class_='wide-image')['src']
		
		# Append the retreived information into a list of dictionaries 
		hemisphere_image_urls.append({"title" : title, "img_url" : img_url})
		

	# Display hemisphere_image_urls
	hemisphere_image_urls
	#items


	# In[16]:


	browser.quit()


	# In[17]:


	# desc=soup.find_all("div",class_="description")
	#data=[]
	# for i in range(len(desc)):
	#     name=desc[i].find("h3").get_text()
	#     browser.find_by_text(name).click()
	#     time.sleep(5)
	#     #browser.find_by_text('Original').click()
	#     #browser.find_by_text('Open').click()
	#     #src=soup.find("img",class_="wide-image")['src']
	#     #load=soup.find("div",class_="downloads", href=True)
	#     #ProdLinkElem = soup.find_all('a',target = '_blank', href = True)
	#     html = browser.html
	#     soup = BeautifulSoup(html, 'html.parser')
	#     hemispheres_main_url = 'https://astrogeology.usgs.gov'
	#     img_url = hemispheres_main_url + soup.find('img', class_='wide-image')['src']
	#     data.append({'title':name,
	#                 'url':img_url})


	# ### Mars Facts

	# In[24]:


	# Visit  URL through splinter and parse HTML with beautiful soup
	executable_path = {'executable_path': 'chromedriver.exe'}
	browser = Browser('chrome', **executable_path, headless=False)
	#browser = webdriver.Chrome('./chromedriver')
	url = 'https://space-facts.com/mars/'
	browser.visit(url)   
	#html = browser.html
	#soup = BeautifulSoup(html, 'html.parser')


	# In[25]:


	# use read_html function in Pandas to automatically scrape any tabular data from a page. 
	mars_factsDf=pd.read_html(url)
	mars_fact=mars_factsDf[0]
	#mars_facts = mars_facts.to_html()
	#mars_facts
	mars_fact.columns = ['Description','Value','Value2']
	mars_fact.set_index('Description', inplace=True)
	mars_fact=mars_fact.iloc[:,0:1]
	mars_facts=mars_fact.to_html()
	mars_facts=mars_facts.replace('\n', '')
	mars_fact.to_html('table1.html')
	mars_fact


	# In[20]:


	browser.quit()


	# In[21]:


	# # Visit Mars facts url 
	# #facts_url = 'http://space-facts.com/mars/'

	# # Use Panda's `read_html` to parse the url
	# mars_facts = pd.read_html(url)

	# # Find the mars facts DataFrame in the list of DataFrames as assign it to `mars_df`
	# mars_df = mars_facts[0]

	# # Assign the columns `['Description', 'Value']`
	# mars_df.columns = ['Description','Value']

	# # Set the index to the `Description` column without row indexing
	# mars_df.set_index('Description', inplace=True)

	# # Save html code to folder Assets
	# mars_df.to_html()

	# data = mars_df.to_dict(orient='records')  # Here's our added param..

	# # Display mars_df
	# mars_df


	# In[22]:


	# Display a python dictionary of all scraped data


	# In[27]:


	mars_data={
		"news_title":mars_title,
		"news_p":mars_p,
		"featured_url":featured_url,
		"mars_weather":mars_weather,
		"mars_facts":mars_facts,
		"hemisphere_image_urls":hemisphere_image_urls
	  
		
	}
	return mars_data


	# In[ ]:




