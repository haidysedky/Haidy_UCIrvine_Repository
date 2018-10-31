from bs4 import BeautifulSoup as bs
import pandas as pd
from splinter import Browser
from time import sleep


def init_browser():
	executable_path = {'executable_path': 'chromedriver.exe'}
	return Browser('chrome', **executable_path, headless=False)
	

def scrape():
    
    # ## NASA Mars News
    browser = init_browser()
    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(url)
    html = browser.html
    soup = bs(html, "html.parser")
    title = soup.find('div', class_="content_title")
    news_title  = title.text.strip()
    news_p = soup.find('div', class_='article_teaser_body').get_text()
    browser.quit()

    # ## JPL Mars Space Images - Featured Image
    browser = init_browser()
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)
    browser.click_link_by_partial_text("FULL IMAGE")
    sleep(3)
    browser.click_link_by_partial_text("more info")
    #html = browser.html
    #soup = bs(html, 'html.parser')
    #md_image_link = 'https://www.jpl.nasa.gov' + soup.find("div", class_="buttons").a['href']
    #browser.click_link_by_href(md_image_link)
    html = browser.html
    soup = bs(html, 'html.parser')
    featured_image_url = soup.find('figure', class_="lede").a ['href']
    featured_image_url = 'https://www.jpl.nasa.gov' + featured_image_url
    browser.quit()

    # ## Mars Weather
    browser = init_browser()
    url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url)
    html = browser.html
    soup= bs(html, 'html.parser')
    mars_weather = soup.find('div', class_="js-tweet-text-container").p.get_text()
    browser.quit()

    # ## Mars Facts
    url = "https://space-facts.com/mars/"
    tables = pd.read_html(url)
    df = tables[0]
    df.columns =  ['Type','Value']
    df.set_index(['Type'], inplace=True)
    html_table = df.to_html()
    html_table = html_table.replace('\n', '')

    # ## Mars Hemispheres
    browser = init_browser()
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)
    html = browser.html
    hemisphere_image_urls=[]
    soup = bs(html, 'html.parser')
    titles = soup.find_all('div', class_="description")
    for title in titles:
        #print(title.h3.text)
        title = title.h3.get_text()
        browser.click_link_by_partial_text(title)
        html = browser.html
        soup = bs(html, 'html.parser')
        img_url = 'https://astrogeology.usgs.gov' + soup.find('img', class_="wide-image")['src']
        #print(img_url)
        browser.click_link_by_partial_text("Back")
        hemisphere_image_urls.append({"title":title, "img_url":img_url})
    browser.quit()

    mars_dictionary = {"news_title":news_title,
                       "news_p": news_p,
                       "featured_image_url": featured_image_url,
                       "html_table": df.to_dict(),
                       "hemisphere_image_urls":hemisphere_image_urls
                       }
    return (mars_dictionary)
    