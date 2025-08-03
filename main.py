import tweepy
import os
import google.generativeai as genai
import requests
from datetime import datetime, timezone, timedelta
from dotenv import load_dotenv

load_dotenv()

# Twitter credentials
API_KEY = os.getenv("TWITTER_CONSUMER_KEY")
API_SECRET_KEY = os.getenv("TWITTER_CONSUMER_SECRET")
ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

# Gemini API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# GitHub credentials
GITHUB_TOKEN = os.getenv("TOKEN")  # Changed to match workflow
GITHUB_USERNAME = os.getenv("GITHUB_USERNAME") or "TarunAdobe"


def get_github_activity():
    """Fetch GitHub activity directly from GitHub API"""
    if not GITHUB_TOKEN:
        print("GitHub token not found, skipping activity fetch")
        return []
    
    try:
        # Get today's date in ISO format
        today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        
        # Fetch user's events from GitHub API
        headers = {
            "Authorization": f"token {GITHUB_TOKEN}",
            "Accept": "application/vnd.github.v3+json"
        }
        
        username = GITHUB_USERNAME or "ttomar"
        url = f"https://api.github.com/users/{username}/events"
        response = requests.get(url, headers=headers)
        
        if response.status_code != 200:
            print(f"GitHub API request failed: {response.status_code}")
            print(f"Response: {response.text}")
            return []
        
        events = response.json()
        print(f"Found {len(events)} total events")
        
        # Focus on commits from today
        today_commits = []
        for event in events:
            print(f"Event type: {event.get('type')}, Date: {event.get('created_at')}")
            
            # Check if the event is from the last 32 hours
            if event.get('created_at', '') > (datetime.now(timezone.utc) - timedelta(hours=32)).strftime("%Y-%m-%d"):
                
                repo_name = event.get('repo', {}).get('name', 'Unknown repo')
                commits = event.get('payload', {}).get('commits', [])
                
                print(f"Push event in {repo_name} with {len(commits)} commits")
                
                for commit in commits:
                    commit_info = {
                        'type': 'PushEvent',
                        'repo': repo_name,
                        'message': commit.get('message', ''),
                        'author': commit.get('author', {}).get('name', ''),
                        'created_at': event.get('created_at'),
                    }
                    today_commits.append(commit_info)
                    print(f"Commit: {commit.get('message', '')}")
        
        print(f"Found {len(today_commits)} commits from today")
        return today_commits
        
    except Exception as e:
        print(f"Error fetching GitHub activity: {e}")
        return []


def generate_tweet_with_gemini(github_activity):
    """Generate a tweet using Gemini API based on GitHub activity"""
    if not GEMINI_API_KEY:
        raise ValueError("GEMINI_API_KEY not found in environment variables")
    
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel("gemini-2.5-flash-preview-05-20")
    
    if not github_activity:
        prompt = """
        I didn't have any GitHub activity today. Write a short, engaging 
        tweet (under 200 characters) about taking a break from coding, 
        reflection, or planning for tomorrow. Make it relatable to developers. 
        Add \n\n after each line. Include relevant hashtags. Just one tweet 
        nothing else. Return only the tweet.
        """
    else:
        activity_summary = []
        for activity in github_activity:
            message = activity.get('message', '')
            repo = activity.get('repo', '')
            activity_summary.append(f"{message} in {repo}")
        
        activity_text = "; ".join(activity_summary)

        print("activity_text", activity_text)
        
        prompt = f"""
        Based on my GitHub activity today: {activity_text}
        
        Write a short, engaging tweet (under 280 characters) that 
        summarizes my coding day. Make it sound natural and relatable to 
        other developers. Include relevant hashtags like #coding #github 
        #dev. Smaller the better.
        
        TONE: Be hilarious, sarcastic, or naturally conversational. Think of 
        it like texting a developer friend about your day. Use self-
        deprecating humor when appropriate. Be witty about coding struggles, 
        victories, or random developer thoughts. Avoid corporate speak at 
        all costs.
        
        Some of my best tweets are like this - 
            Need suggestions: 

            I already have an AI-curated newsletter service that sends custom 
            newsletters for any news on stocks in your portfolio every day. 

            I extend that to support any topics of your choice (not just 
            stocks). 

            Should I pivot or invest heavily in the original idea?
            OR
            Tried @stripe and @Razorpay
            for my next product's subscription handling. 

            Settled with @gumroad because of how easy it was to set up.

            + The quirky UI was an added bonus on top :)

        Don't make it sound robotic or overly promotional.
        Return only the tweet.
        Do not directly talk about the commits. Make it sound like you are 
        talking about your day.
        If there are multiple commits, it might be beneficial to somehow 
        mention the project for that commit in a subtle way.
        Add two \n \n after each line.
        Need to add two line breaks and empty spaces after every single line.
        Try to make the content helpful and engaging. Some insights are good.
        Make it funny, sarcastic, or authentically human. Think memes, not 
        marketing.
        """
    
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print(f"Error generating tweet with Gemini: {e}")
        return "Had a productive day coding! 💻 #coding #github #dev"


def post_tweet(tweet_text):
    """Post tweet to Twitter using Tweepy"""
    if not all([API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET]):
        raise ValueError("Missing Twitter API credentials")
    
    # Initialize Tweepy v2 Client
    client = tweepy.Client(
        consumer_key=API_KEY,
        consumer_secret=API_SECRET_KEY,
        access_token=ACCESS_TOKEN,
        access_token_secret=ACCESS_TOKEN_SECRET
    )
    
    try:
        response = client.create_tweet(text=tweet_text)
        print(f"Tweet posted successfully: {tweet_text}")
        print(f"Response: {response}")
        return response
    except tweepy.TweepyException as e:
        print(f"Error posting tweet: {e}")
        raise


def main():
    """Main function to orchestrate the tweet generation and posting"""
    try:
        # Get GitHub activity
        github_activity = get_github_activity()
        print(f"Found {len(github_activity)} GitHub activities for today")
        
        # Generate tweet using Gemini
        tweet_text = generate_tweet_with_gemini(github_activity)
        print(f"Generated tweet: {tweet_text}")
        
        # Post tweet
        post_tweet(tweet_text)
        
    except Exception as e:
        print(f"Error in main execution: {e}")
        # Fallback tweet if something goes wrong
        try:
            fallback_msg = ("Fallback tweet: Another day of coding in the "
                            "books! 🚀 #coding #dev")
            print(fallback_msg)
        except Exception as fallback_error:
            print(f"Even fallback tweet failed: {fallback_error}")


if __name__ == "__main__":
    main()