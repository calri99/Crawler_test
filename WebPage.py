# WebPage.py
from EHHelper import EHHelper


class WebPage:
    def __init__(self, url, title, description, links):
        self.url = url
        self.title = EHHelper.EmitTagAndSpecialCh(title)
        self.description = EHHelper.EmitTagAndSpecialCh(description)
        self.links = links
        self.mcnt = 0

    @staticmethod
    def MakeWebPage(url, cpage):
        try:
            title = cpage.title.text
            atags = cpage.find_all("a")
            links = WebPage.ExtractionUrls(atags)
        except:
            return None
        else:
            return WebPage(url, title, cpage.text, links)

    @staticmethod
    def ExtractionUrls(atags):
        links = list()
        for atag in atags:
            if atag.has_attr('download') == False:
                try:
                    link = atag['href']
                except:
                    continue
                else:
                    link = WebPage.ExtractionUrl(link)
                    if str.startswith(link, 'http') or str.startswith(link, 'https'):
                        links.append(link)
        return links

    @staticmethod
    def ExtractionUrl(url):
        index = url.find('#')
        if (index != -1):
            url = url[:index]
        index = url.find("?")
        if (index != -1):
            url = url[:index]
        return url
