import requests
import os

SUPADATA_API_KEY = "sd_c68f559a7959492516ef0b0ae3aeb785"

videos = [
    {"author": "aleyda-solis", "title": "SEO in the Age of ChatGPT: What No One's Talking About", "url": "https://youtu.be/c8D07e6qmvQ?si=g-GtLKCQuyHC1bf5"},
    {"author": "kevin-indig", "title": "SEO in the Age of AI - Google Overviews & Future of Search", "url": "https://www.youtube.com/watch?v=qujABKOAThA"},
    {"author": "neil-patel", "title": "AI-SEO Is Changing Everything in 2026", "url": "https://www.youtube.com/watch?v=tMBdA2gkXgk"},
    {"author": "koray-tugberk", "title": "The Future of SEO: 2025 SEO Tactics", "url": "https://www.youtube.com/watch?v=xQseqVGrsPc"},
    {"author": "ross-hudgens", "title": "AI Visibility, Data Journalism, and the Future of SEO", "url": "https://www.youtube.com/watch?v=8-PS7gR2G0I"},
    {"author": "michal-suski", "title": "How to Take Your Content Strategy to the Next Level", "url": "https://www.youtube.com/watch?v=mPSVJFyW_-I"},
    {"author": "brendan-hufford", "title": "SEO Mistakes to Avoid", "url": "https://www.youtube.com/watch?v=MrxJTEfL_Og"},
    {"author": "chima-mmeje", "title": "Top SEO Tips For 2026 - Whiteboard Friday", "url": "https://www.youtube.com/watch?v=iTttoPGAJoY"},
    {"author": "eli-schwartz", "title": "Rethinking SEO in the age of AI", "url": "https://www.youtube.com/watch?v=Z71yGshPTwk"},
    {"author": "ryan-law", "title": "Crafting Data-Driven Content in the Age of AI", "url": "https://www.youtube.com/watch?v=vsCmaHL5C7k"},
]

os.makedirs("research/youtube-transcripts", exist_ok=True)

for video in videos:
    print(f"Fetching transcript for {video['author']}...")
    
    response = requests.get(
        "https://api.supadata.ai/v1/youtube/transcript",
        params={"url": video["url"], "text": True},
        headers={"x-api-key": SUPADATA_API_KEY}
    )
    
    filename = f"research/youtube-transcripts/{video['author']}.md"
    
    if response.status_code == 200:
        data = response.json()
        content = data.get("content", "")
        if isinstance(content, list):
            transcript_text = " ".join([item.get("text", "") for item in content if isinstance(item, dict)])
        else:
            transcript_text = str(content) if content else "No transcript available"
        
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"# YouTube Transcript: {video['author']}\n\n")
            f.write(f"**Video Title:** {video['title']}\n")
            f.write(f"**Source URL:** {video['url']}\n")
            f.write(f"**Collected:** 15-April-2026\n\n")
            f.write("---\n\n")
            f.write(str(transcript_text))
        print(f"✅ Saved: {filename}")
    else:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"# YouTube Transcript: {video['author']}\n\n")
            f.write(f"**Video Title:** {video['title']}\n")
            f.write(f"**Source URL:** {video['url']}\n")
            f.write(f"**Collected:** 15-April-2026\n")
            f.write(f"**Status:** Transcript unavailable (Error {response.status_code})\n")
            f.write(f"**Note:** Auto-captions disabled or video restricted.\n")
        print(f"❌ Failed for {video['author']}: {response.status_code}")

print("\n✅ All done! Check research/youtube-transcripts/")
