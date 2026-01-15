import requests
from newspaper import Article

response = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json')
datas = response.json()

url = f'https://hacker-news.firebaseio.com/v0/item/{datas[0]}.json'

print(requests.get(url).json())

search_words = ['AI', 'artificial intelligence', 'machine learning', 'deep learning', 'neural network', 'chatbot', 'NLP', 'computer vision', 'robotics', 'automation', 'LLM', 'GPT', 'transformer', 'data science', 'big data', 'predictive analytics', 'reinforcement learning', 'supervised learning', 'unsupervised learning', 'generative AI', 'AI ethics' 'gemini', 'bard', 'Claude', 'LLaMA', 'Mistral', 'Alpaca', 'Vicuna', 'ChatgPT']
matching_articles = []

for data in datas:
    url = f'https://hacker-news.firebaseio.com/v0/item/{data}.json'
    article = requests.get(url).json()
    if 'title' in article:
        title = article['title'].lower()
        if any(word.lower() in title for word in search_words):
            matching_articles.append(article)
            if len(matching_articles) >= 15:
                break
            
print(f"Found {len(matching_articles)} matching articles:")
for article in matching_articles:
    print(f"- {article['title']} (https://news.ycombinator.com/item?id={article['id']})")
    
                
                
api_url = 'https://hacker-news.firebaseio.com/v0/item/46629474.json' 

response = requests.get(api_url)
story_data = response.json() 

print(f"Cím: {story_data.get('title')}")
print(f"Külső Link: {story_data.get('url')}")
print("-" * 30)                
             
                
article = Article(story_data['url'])
article.download()
article.parse()
print(article.text)
print(article.authors)
print(article.publish_date)
print(article.top_image)
print(article.summary)