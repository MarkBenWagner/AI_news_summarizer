import requests
import newspaper3k

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
    
                
                