# 🤖 Tweeter Bot: Because Manual Tweeting is SO 2019

> *"Why tweet about your code when your code can tweet about itself?"* - Probably some philosopher

## What is this beautiful chaos? 🎭

Meet your new digital hype person! This bot stalks your GitHub activity like an overly enthusiastic mom at a soccer game, then uses AI to craft tweets that make your coding sessions sound way cooler than they actually were.

**Before Tweeter Bot:**
- You: *pushes 3 commits fixing typos*
- Twitter: *crickets*

**After Tweeter Bot:**
- You: *pushes 3 commits fixing typos*
- Bot: "Just shipped some elegant optimizations to enhance code readability and maintainability! 🚀 Sometimes the smallest changes make the biggest impact #coding #dev #craftsmanship"

## Features That'll Make You Question Reality 🌟

- 🕵️ **GitHub Stalker Mode**: Automatically watches your every commit (in a totally non-creepy way)
- 🧠 **AI Ghostwriter**: Uses Google's Gemini to make your `fix: typo` commits sound like you just solved world hunger
- ⏰ **Scheduled Narcissism**: Posts daily at 7 PM UTC because that's prime "look how productive I am" hours
- 🎪 **Fallback Humility**: If you didn't code today, it'll tweet something relatable about taking breaks (we see you, Netflix binger)
- 🤖 **Zero Effort Required**: Because who has time to manually brag about their code?

## Setup (Or: How to Outsource Your Social Media Presence) 🛠️

### Prerequisites
- A GitHub account (obviously)
- A Twitter account (preferably one your employer follows)
- Google Gemini API key (because we're fancy like that)
- The ability to follow instructions (surprisingly rare)

### Step 1: Get Your API Keys 🔑

**Twitter API** (The hard part):
1. Go to [Twitter Developer Portal](https://developer.twitter.com/)
2. Apply for developer access
3. Wait 3-5 business years for approval
4. Sacrifice a rubber duck to the API gods
5. Get your keys (finally!)

**Google Gemini API** (The easy part):
1. Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Click the big obvious button
3. Copy the key
4. Feel smart for 2 seconds

**GitHub Token** (The "why do I need another token?" part):
1. Go to GitHub Settings → Developer settings → Personal access tokens
2. Create a new token with `public_repo` access
3. Name it something creative like "tweet-bot-supreme"
4. Store it somewhere safe (not in another repo, genius)

### Step 2: Feed the Secrets Monster 🍽️

In your GitHub repo, go to:
`Settings → Secrets and variables → Actions → New repository secret`

Add these secrets (spell them exactly like this, the bot is picky):
- `TWITTER_CONSUMER_KEY`
- `TWITTER_CONSUMER_SECRET` 
- `TWITTER_ACCESS_TOKEN`
- `TWITTER_ACCESS_TOKEN_SECRET`
- `GEMINI_API_KEY`
- `TOKEN` (your GitHub token)

### Step 3: Sit Back and Watch the Magic ✨

The bot runs every day at 7 PM UTC. If you want to test it immediately (because patience is overrated), go to:
`Actions → Daily Tweet from GitHub Activity → Run workflow`

## How It Works (The Technical Stuff Nobody Reads) 🔧

1. **Stalking Phase**: Bot checks your GitHub activity for the day
2. **Analysis Phase**: Finds all your commits, PRs, and other productive-looking activities
3. **Creative Writing Phase**: Feeds your boring commit messages to AI
4. **Ego Boosting Phase**: AI transforms "fixed bug" into "implemented elegant solution to enhance user experience"
5. **Publishing Phase**: Posts tweet and makes you look like a coding rockstar

## Sample Outputs 📱

**Your commit:** `fix: remove console.log`

**Bot's tweet:** "Today's focus: cleaning up debug artifacts and optimizing the development workflow! 🧹✨ Sometimes the best code is the code you remove #cleancoding #optimization #developer"

**Your activity:** *No commits today*

**Bot's tweet:** "Taking a strategic pause today to let the creative juices recharge! 🔋 Tomorrow's breakthroughs need today's reflection #mindfulness #developer #planning"

## Troubleshooting (When Things Go Wrong) 🚨

**"It's not tweeting!"**
- Check if your API keys are correct (they probably aren't)
- Make sure you spelled the secret names right (case sensitive, because computers are mean)
- Verify your Twitter app has write permissions (read-only is for quitters)

**"It's tweeting weird stuff!"**
- That's the AI being creative! Embrace the chaos
- Or adjust the prompt in `main.py` if you're boring

**"It tweeted about my 3 AM debugging session!"**
- That's... actually pretty accurate
- Maybe commit less embarrassing messages?

## Contributing 🤝

Found a bug? Want to add features? Think the AI needs more personality? 

PRs welcome! Just remember:
- Keep it fun
- Keep it functional  
- Keep it from becoming sentient

## License 📜

MIT License - Use it, abuse it, improve it, just don't blame us when your bot starts subtweeting your coworkers.

## Disclaimer ⚠️

This bot may:
- Make your GitHub activity look more impressive than it is
- Cause coworkers to think you're a productivity machine
- Lead to unrealistic expectations about your coding abilities
- Become your most consistent social media presence

Use responsibly. Side effects may include increased follower count, imposter syndrome, and the occasional existential crisis about automation replacing human creativity.

---

*Built with ❤️, ☕, and an unhealthy amount of automation*

**Remember**: If your bot starts tweeting better content than you do manually, that's not a bug – it's a feature! 🎉 