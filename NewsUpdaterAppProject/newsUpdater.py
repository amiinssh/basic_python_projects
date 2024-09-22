from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='API_KEY')

top_headlines = newsapi.get_top_headlines(q='bitcoin',
 sources='bbc-news,the verge',
 category='business',
 language='en',
 country='us')

dt = top_headlines['articles']

for x,y in enumerate(dt):
    print(f'{x} {y["description"]}')