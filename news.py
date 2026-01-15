import requests
from newspaper import Article
import os
from dotenv import load_dotenv
from openai import OpenAI
from datetime import datetime


load_dotenv()
openai_api = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=openai_api)

print("Requesting Hacker News top stories...")
response = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json')
datas = response.json()

search_words = ['AI', 'artificial intelligence', 'machine learning', 'deep learning', 'neural network', 'chatbot', 'NLP', 'computer vision', 'robotics', 'automation', 'LLM', 'GPT', 'transformer', 'data science', 'big data', 'predictive analytics', 'reinforcement learning', 'supervised learning', 'unsupervised learning', 'generative AI', 'AI ethics', 'gemini', 'bard', 'Claude', 'LLaMA', 'Mistral', 'Alpaca', 'Vicuna', 'ChatGPT']

matching_articles = []

print("Filtering articles for AI relevance...")
for data in datas[:100]: 
    try:
        url = f'https://hacker-news.firebaseio.com/v0/item/{data}.json'
        article_info = requests.get(url, timeout=25).json()
        
        if article_info and 'title' in article_info and 'url' in article_info:
            title = article_info['title']

            if any(word.lower() in title.lower() for word in search_words):
                print(f"Matches: {title}")
                matching_articles.append(article_info)
                

                if len(matching_articles) >= 15: 
                    break
    except Exception as e:
        print(f"Error fetching news... {e}")
        continue


article_contents = ""

print(f"\n{len(matching_articles)} downloading article...")

for article in matching_articles:
    try:

        news_article = Article(article['url'])
        news_article.download()
        news_article.parse()
        


        short_text = news_article.text[:3000]
        

        article_contents += f"""
        Title: {article['title']}
        Source URL: {article['url']}
        Content: {short_text}...
        ---
        """
    except Exception as e:
        print(f"Error downloading article ({article['title']}): {e}")


if article_contents:
    print("\nGenerating AI Summary...")
    
    
    
    response = client.chat.completions.create(
        model="gpt-5", 
        messages=[
            {
                "role": "system",
                "content": "You are an elite AI Tech Analyst briefing a CTO. Group the news by topic. Use the markdown file format. For each story, provide the Headline, a 2-sentence Summary, and a 'Why it Matters' section."
            },
            {
                "role": "user",
                "content": f"Summarize these AI news articles:\n\n{article_contents}"
            }
        ]
    )


    final_summary = response.choices[0].message.content
    today = datetime.now().strftime("%m/%d/%Y")
    print(f"\--- DAILY AI NEWS - {today}")
    print(final_summary)
    
    
    now = datetime.now()
    

    year = now.strftime('%Y')
    month = now.strftime('%m')
    day_str = now.strftime('%Y_%m_%d')
    
    directory = os.path.join("archive", year, month)
    
    os.makedirs(directory, exist_ok=True)
    
    filename = f"daily_ai_news_{day_str}.md"
    full_path = os.path.join(directory, filename)
    
    print(f"Save: {full_path} ...")
    
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(f"# DAILY AI NEWS - {now.strftime('%Y-%m-%d')}\n\n")
        f.write(final_summary)

else:
    print("No relevant articles found.")