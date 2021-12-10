from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='38f2204573bc443b9f6ae5556e1d8c76')

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q='Covid,COVID-19,coronavirus',
                                          sources='bbc-news',
                                          category='health',
                                          language='en',
                                          country='england')

# /v2/everything
all_articles = newsapi.get_everything(q='Covid,COVID-19,coronavirus',
                                      sources='bbc-news',
                                      domains='bbc.co.uk',
                                      from_param='2021-02-12',
                                      to='2021-09-12',
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)

# /v2/top-headlines/sources

sources = newsapi.get_sources()
