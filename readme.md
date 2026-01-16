# AI News Summarizer

Generate a daily AI news digest from Hacker News using a GPT model and archive the result to markdown.

## What it does

- Pulls the top 100 Hacker News stories and filters titles for AI-related keywords.
- Downloads article content with Newspaper3k.
- Summarizes grouped topics with OpenAI Chat Completions.
- Saves the daily digest into an archive by year/month.

## Requirements

- Python 3.10+
- An OpenAI API key

## Installation

```bash
pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the project root:

```
OPENAI_API_KEY=your_api_key_here
```

## Usage

```bash
python news.py
```

The script will:

1. Fetch Hacker News top stories.
2. Filter AI-related titles.
3. Download article text.
4. Generate a grouped markdown summary.
5. Save to the archive folder.

## Output

Daily digests are saved here:

```
archive/<YYYY>/<MM>/daily_ai_news_<YYYY_MM_DD>.md
```

## Notes

- The summarizer uses the `gpt-5` model name in the code. Update it if your account uses a different model.
- If no relevant articles are found, the script prints a message and exits.

## License

If you plan to publish this, add a LICENSE file. MIT is a common choice.