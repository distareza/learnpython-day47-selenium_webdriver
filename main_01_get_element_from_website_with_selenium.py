"""
    Download and Unzip Chrome Drive from https://chromedriver.chromium.org/downloads
    make sure to download with the match version of chrome browser you had in chrome://settings/help

    xpath documentation : https://www.w3schools.com/xml/xpath_intro.asp
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_drive_path = "C:/apps/chromedriver_win32/chromedriver.exe"

selenium_service = Service(executable_path=chrome_drive_path)
driver = webdriver.Chrome(service=selenium_service)

amazon_url = "https://www.amazon.com/COMFEE-Pressure-Kick-Start-Multi-Functional-Programmable/dp/B091TTDRVP/ref=pd_di_sccai_cn_sccl_1_3/145-8848130-8351748?pd_rd_w=qi9lW&pf_rd_p=1ed8df3a-0df8-4988-98b9-252e4c99c568&pf_rd_r=T0SKDY4T8WENHVK61K6E&pd_rd_r=f349e095-bf41-4723-99d1-f4acd8789e31&pd_rd_wg=CyBkn&pd_rd_i=B091TTDRVP&psc=1"
driver.get(amazon_url)
"""
    assume that amazon page having following content in body
    ...
    <span class="a-price a-text-price a-size-medium" data-a-size="b" data-a-color="price">
        <span class="a-offscreen">$88.71</span>
        <span aria-hidden="true">$88.71</span>
    </span>
    ...
"""
#price = driver.find_element_by_class_name("a-price")
price = driver.find_element(by=By.CLASS_NAME, value="a-price")
print(price.text)
# it will print out %88.71


python_url = "https://www.python.org"
driver.get(python_url)
"""
    <form class="search-the-site" action="/search/" method="get">
        <fieldset title="Search Python.org">
            <span aria-hidden="true" class="icon-search"></span>
            <label class="screen-reader-text" for="id-search-field">Search This Site</label>
            <input id="id-search-field" name="q" type="search" role="textbox" class="search-field" placeholder="Search" value="" tabindex="1">
            <button type="submit" name="submit" id="submit" class="search-button" title="Submit this Search" tabindex="3">
                GO
            </button>
            <!--[if IE]><input type="text" style="display: none;" disabled="disabled" size="1" tabindex="4"><![endif]-->
        </fieldset>
    </form>
"""
#search_bar = driver.find_element_by_name("q")
search_bar = driver.find_element(by=By.NAME, value="q")
print(search_bar.tag_name)
# print input
print(search_bar.get_attribute("placeholder"))
# print Search

documentation_link = driver.find_element(by=By.CSS_SELECTOR, value=".documentation-widget a")
print(documentation_link.text)
# print docs.python.org

"""
<footer id="site-map" class="main-footer" role="contentinfo">
    <div class="main-footer-links">
        <div class="container">
            <ul class="sitemap navigation menu do-not-print" role="tree" id="container">
                <li class="tier-1 element-1"><a href="/about/">About</a></li>
                <li class="tier-1 element-2" ><a href="/downloads/">Downloads</a></li>
                <li class="tier-1 element-3"><a href="/doc/">Documentation</a></li>
                <li class="tier-1 element-4"><a href="/community/">Community</a></li>
                <li class="tier-1 element-5"><a href="/success-stories/">Success Stories</a></li>
                <li class="tier-1 element-6"><a href="/blogs/">News</a></li>                
                <li class="tier-1 element-7"><a href="/events/">Events</a></li>                
                <li class="tier-1 element-8">
                    <a href="/dev/">Contributing</a>
                    <ul class="subnav menu">
                            <li class="tier-2 element-1" role="treeitem"><a href="https://devguide.python.org/" title="">Developer's Guide</a></li>
                            <li class="tier-2 element-2" role="treeitem"><a href="https://bugs.python.org/" title="">Issue Tracker</a></li>
                            <li class="tier-2 element-3" role="treeitem"><a href="https://mail.python.org/mailman/listinfo/python-dev" title="">python-dev list</a></li>
                            <li class="tier-2 element-4" role="treeitem"><a href="/dev/core-mentorship/" title="">Core Mentorship</a></li>
                            <li class="tier-2 element-5" role="treeitem"><a href="/dev/security/" title="">Report a Security Issue</a></li>
                    </ul>
                </li>                
            </ul>
        </div>
    </div>
</footer>

reference : https://www.w3schools.com/xml/xpath_intro.asp
"""
xpath_bug_link = driver.find_element(by=By.XPATH, value='//*[@id="container"]/li[8]/ul/li[2]/a')
print(xpath_bug_link.text)
# print Issue Tracker




driver.quit()
