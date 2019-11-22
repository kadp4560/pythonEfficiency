from common import config
import requests
import bs4
class HomePage:

	def __init__(self, new_sites_uid, url,  ):
		self._config = config()['new_sites'][new_sites_uid]
		self._queries = self._config['queries']
		self._html = None 
		self._visit(url)


	def _select(self, query_string):
		return self._html.select(query_string)
	
	@property
	def article_links(self):
		link_list =[]
		for link in self._select(self._queries['homepage_articles_links']):
			if link and link.has_attr('href'):
				link_list.append(link)

		return set(link['href'] for link in link_list)


	def _visit(self,url):

		response = requests.get('url')

		response.raise_for_status()

		self._html = bs4.BeautifulSoup(response.text,'html.parser')
