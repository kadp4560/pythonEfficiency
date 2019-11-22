import argparse
import logging
from common import config
import news_page_objects  as news
logging.basicConfig(level =logging.INFO)
logger = logging.getLogger(__name__)

def _news_scrapper(_news_site_uid):
        logging.info('Start::..')
        host = config()['news_site'][_news_site_uid]['url']
        logging.info('Beginning sraper for {}'.format(host))
        homepage = news.HomePage(_news_site_uid,host)

        for link in homepage.article_links:
                print(link)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    logging.info('Middle::.. {}'.format(list(config()['news_site'])))
    new_sites_choices = list(config()['news_site'].keys())
    parser.add_argument('news_site',
                            help='The news sites that u want to scrape',
                            type=str,
                            choices=new_sites_choices)


    args = parser.parse_args()
    _news_scrapper(args.news_site)

                    