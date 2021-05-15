from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class EventbritePoster():

  def __init__(self, username: str, pwd: str):
    self.driver = webdriver.Firefox()
    self.username = username
    self.pwd = pwd

  def create_links(self, filepath: str, event_link_url: str, ref_create_links: str):
    # get refs from csv
    links = []
    with open(filepath) as csvfile:
      for row in csvfile:
        links.append(row)

    # login
    self.driver.get('https://www.eventbrite.de/signin/?referrer=%2F')
    self.driver.find_element_by_id('email').send_keys(self.username + Keys.RETURN)
    sleep(1)
    self.driver.find_element_by_id('password').send_keys(self.pwd + Keys.RETURN)
    sleep(5)

    # navigate to link creation page
    self.driver.get(event_link_url)

    for link in links:
      # open creation form
      self.driver.find_element_by_id('create-new-link-button').click()

      # clear form and enter value
      self.driver.find_element_by_id("code").clear()
      self.driver.find_element_by_id("code").send_keys(link)
      self.driver.find_element_by_xpath(
        '/html/body/div[1]/div/div[2]/div/div/div/div[1]/div/main/section/div/section/div[1]/section[3]/form/div[4]/div/a[1]').click()
      sleep(2)

      # write generated Links into List
      with open('links.csv', 'w', newline='') as refs:
        refs.write(ref_create_links + link + '\n')


if __name__ == '__main__':
  poster = EventbritePoster('EMAIL', 'PASSWORD')
  # adjust filepath, link to your event and the generic part of the tracking link here
  poster.create_links('names.csv',
                      'https://www.eventbrite.com/links?eid=104768818356',
                      'https://www.eventbrite.com/e/start-and-spread-summer-2020-links-tba-powered-by-manage-and-more-tickets-104768818356?aff=')
