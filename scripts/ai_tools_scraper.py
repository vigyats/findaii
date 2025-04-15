"""
AI Tools Scraper

This script scrapes information about AI tools from various sources,
including tools that are popular globally and in India.
"""

import json
import os
import time
import random
import trafilatura
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from datetime import datetime

# Create directories if they don't exist
os.makedirs("scripts/data", exist_ok=True)

# List of websites to scrape
SOURCES = [
    {
        "name": "futurepedia",
        "url": "https://www.futurepedia.io/ai-tools",
        "country": "global"
    },
    {
        "name": "futuretools",
        "url": "https://www.futuretools.io/",
        "country": "global"
    },
    {
        "name": "there_is_an_ai_for_that",
        "url": "https://theresanaiforthat.com/",
        "country": "global" 
    },
    {
        "name": "aitools_fyi",
        "url": "https://aitools.fyi/",
        "country": "global"
    },
    {
        "name": "toolspilot",
        "url": "https://toolspilot.com/ai-tools/",
        "country": "global"
    },
    {
        "name": "topai_tools",
        "url": "https://www.topai.tools/",
        "country": "global"
    },
    {
        "name": "indianai",
        "url": "https://indian.ai/tools",
        "country": "india"
    },
    {
        "name": "analyticsindiamag",
        "url": "https://analyticsindiamag.com/category/ai/",
        "country": "india"
    }
]

# Set headers to mimic browser and avoid blocking
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive"
}

# Popular AI tools in India (manually curated)
INDIAN_AI_TOOLS = [
    {
        "name": "Krutrim AI",
        "url": "https://krutrim.ai/",
        "description": "India's first AI model and assistant, developed by Ola, supporting multiple Indian languages.",
        "category": "Language Model",
        "pricing": "Freemium",
        "country": "India"
    },
    {
        "name": "Bhashini",
        "url": "https://bhashini.gov.in/",
        "description": "A government-backed AI translation platform supporting 22 official Indian languages.",
        "category": "Translation",
        "pricing": "Free",
        "country": "India"
    },
    {
        "name": "Sarvam AI",
        "url": "https://www.sarvam.ai/",
        "description": "A voice-first AI that works in multiple Indian languages to solve India-specific problems.",
        "category": "Voice AI",
        "pricing": "Freemium",
        "country": "India"
    },
    {
        "name": "Rephrase.ai",
        "url": "https://www.rephrase.ai/",
        "description": "AI-powered video creation platform with digital avatars for marketing and sales content.",
        "category": "Video Generation",
        "pricing": "Paid",
        "country": "India"
    },
    {
        "name": "Vernacular.ai",
        "url": "https://vernacular.ai/",
        "description": "Voice AI solutions for customer service in multiple Indian languages.",
        "category": "Voice AI",
        "pricing": "Paid",
        "country": "India"
    },
    {
        "name": "Artivatic.ai",
        "url": "https://artivatic.ai/",
        "description": "AI solutions for insurance and healthcare industries with focus on the Indian market.",
        "category": "Healthcare",
        "pricing": "Paid",
        "country": "India"
    },
    {
        "name": "Haptik",
        "url": "https://www.haptik.ai/",
        "description": "Conversational AI platform that helps businesses engage customers through chat and voice.",
        "category": "Chatbot",
        "pricing": "Paid",
        "country": "India"
    },
    {
        "name": "SigTuple",
        "url": "https://sigtuple.com/",
        "description": "AI solutions for medical diagnosis through image analysis of blood samples, etc.",
        "category": "Healthcare",
        "pricing": "Paid",
        "country": "India"
    },
    {
        "name": "Niramai",
        "url": "https://www.niramai.com/",
        "description": "AI-based breast cancer screening solution that's non-invasive and privacy-aware.",
        "category": "Healthcare",
        "pricing": "Paid",
        "country": "India"
    },
    {
        "name": "Mad Street Den",
        "url": "https://www.madstreetden.com/",
        "description": "AI platform specializing in retail and fashion visual AI solutions with global reach.",
        "category": "Retail",
        "pricing": "Paid",
        "country": "India"
    },
    {
        "name": "Zevi.ai",
        "url": "https://www.zevi.ai/",
        "description": "AI-powered search and discovery platform for e-commerce sites with focus on Indian market.",
        "category": "E-commerce",
        "pricing": "Paid",
        "country": "India"
    },
    {
        "name": "Mihup",
        "url": "https://mihup.com/",
        "description": "Conversational AI that works with Indian languages and dialects for businesses.",
        "category": "Voice AI",
        "pricing": "Paid",
        "country": "India"
    },
    {
        "name": "Fluid AI",
        "url": "https://fluid.ai/",
        "description": "AI banking platform for financial institutions to personalize customer experience.",
        "category": "Finance",
        "pricing": "Paid",
        "country": "India"
    },
    {
        "name": "E42",
        "url": "https://e42.ai/",
        "description": "AI worker platform that helps businesses automate processes across departments.",
        "category": "Automation",
        "pricing": "Paid",
        "country": "India"
    },
    {
        "name": "CropIn",
        "url": "https://www.cropin.com/",
        "description": "AI and data-driven agriculture solutions for farmers, banks, and government.",
        "category": "Agriculture",
        "pricing": "Paid",
        "country": "India"
    }
]

# Additional popular global AI tools
GLOBAL_AI_TOOLS = [
    {
        "name": "Midjourney",
        "url": "https://www.midjourney.com/",
        "description": "AI art generation tool that creates images from text descriptions.",
        "category": "Image Generation",
        "pricing": "Paid",
        "country": "USA"
    },
    {
        "name": "Suno AI",
        "url": "https://suno.ai/",
        "description": "AI music generation platform that creates songs from text prompts.",
        "category": "Music Generation",
        "pricing": "Freemium",
        "country": "USA"
    },
    {
        "name": "Replit",
        "url": "https://replit.com/",
        "description": "AI-powered coding platform with Ghostwriter for code generation and completion.",
        "category": "Coding",
        "pricing": "Freemium",
        "country": "USA"
    },
    {
        "name": "Perplexity AI",
        "url": "https://www.perplexity.ai/",
        "description": "AI-powered search engine that provides comprehensive answers to complex questions.",
        "category": "Search",
        "pricing": "Freemium",
        "country": "USA"
    },
    {
        "name": "Runway",
        "url": "https://runwayml.com/",
        "description": "Creative AI tools for video editing, generation, and creative workflow.",
        "category": "Video",
        "pricing": "Paid",
        "country": "USA"
    },
    {
        "name": "Elevenlabs",
        "url": "https://elevenlabs.io/",
        "description": "AI voice synthesis platform for realistic text-to-speech and voice cloning.",
        "category": "Voice",
        "pricing": "Freemium",
        "country": "UK"
    },
    {
        "name": "DALL-E",
        "url": "https://openai.com/dall-e-3",
        "description": "OpenAI's AI system that creates realistic images and art from text descriptions.",
        "category": "Image Generation",
        "pricing": "Paid",
        "country": "USA"
    },
    {
        "name": "ChatGPT",
        "url": "https://chat.openai.com/",
        "description": "OpenAI's conversational AI model that can engage in natural dialogs and answer questions.",
        "category": "Language Model",
        "pricing": "Freemium",
        "country": "USA"
    },
    {
        "name": "Copy.ai",
        "url": "https://www.copy.ai/",
        "description": "AI copywriting tool that helps create marketing content, emails, and social media posts.",
        "category": "Writing",
        "pricing": "Freemium",
        "country": "USA"
    },
    {
        "name": "Jasper",
        "url": "https://www.jasper.ai/",
        "description": "AI content platform for marketing teams to create blogs, social posts, and emails.",
        "category": "Writing",
        "pricing": "Paid",
        "country": "USA"
    },
    {
        "name": "Notion AI",
        "url": "https://www.notion.so/product/ai",
        "description": "AI writing assistant integrated into Notion for summarizing, brainstorming, and editing.",
        "category": "Writing",
        "pricing": "Paid",
        "country": "USA"
    },
    {
        "name": "Anthropic Claude",
        "url": "https://www.anthropic.com/claude",
        "description": "Conversational AI assistant designed to be helpful, harmless, and honest.",
        "category": "Language Model",
        "pricing": "Freemium",
        "country": "USA"
    },
    {
        "name": "Synthesia",
        "url": "https://www.synthesia.io/",
        "description": "AI video generation platform that creates videos with virtual avatars from text.",
        "category": "Video",
        "pricing": "Paid",
        "country": "UK"
    },
    {
        "name": "Lumen5",
        "url": "https://lumen5.com/",
        "description": "AI video creation platform that transforms text content into engaging videos.",
        "category": "Video",
        "pricing": "Freemium",
        "country": "Canada"
    },
    {
        "name": "DeepL",
        "url": "https://www.deepl.com/",
        "description": "AI translation service known for high-quality, natural-sounding translations.",
        "category": "Translation",
        "pricing": "Freemium",
        "country": "Germany"
    },
    {
        "name": "Descript",
        "url": "https://www.descript.com/",
        "description": "AI-powered audio and video editing platform with transcription and voice cloning.",
        "category": "Audio/Video",
        "pricing": "Freemium",
        "country": "USA"
    },
    {
        "name": "Stable Diffusion",
        "url": "https://stability.ai/",
        "description": "Open-source AI image generation model that creates images from text descriptions.",
        "category": "Image Generation",
        "pricing": "Free",
        "country": "UK"
    },
    {
        "name": "GitHub Copilot",
        "url": "https://github.com/features/copilot",
        "description": "AI coding assistant that suggests code completions based on context.",
        "category": "Coding",
        "pricing": "Paid",
        "country": "USA"
    },
    {
        "name": "Grammarly",
        "url": "https://www.grammarly.com/",
        "description": "AI writing assistant that checks grammar, spelling, and suggests style improvements.",
        "category": "Writing",
        "pricing": "Freemium",
        "country": "USA"
    },
    {
        "name": "Canva AI",
        "url": "https://www.canva.com/ai-image-generator/",
        "description": "AI tools in Canva for design, image generation, and content creation.",
        "category": "Design",
        "pricing": "Freemium",
        "country": "Australia"
    }
]

def fetch_website_content(url):
    """Fetch website content with error handling and retries"""
    max_retries = 3
    retry_delay = 2
    
    for attempt in range(max_retries):
        try:
            response = requests.get(url, headers=HEADERS, timeout=10)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {url}: {str(e)}")
            if attempt < max_retries - 1:
                sleep_time = retry_delay * (attempt + 1) + random.uniform(0, 1)
                print(f"Retrying in {sleep_time:.1f} seconds...")
                time.sleep(sleep_time)
            else:
                print(f"Failed to fetch {url} after {max_retries} attempts")
                return None

def extract_text_content(html_content):
    """Extract main text content from HTML using trafilatura"""
    if not html_content:
        return None
    
    try:
        return trafilatura.extract(html_content)
    except Exception as e:
        print(f"Error extracting content: {str(e)}")
        return None

def scrape_website(source):
    """Scrape a website and extract AI tools information"""
    print(f"Scraping {source['name']} ({source['url']})...")
    
    html_content = fetch_website_content(source['url'])
    if not html_content:
        return []
    
    text_content = extract_text_content(html_content)
    if not text_content:
        return []
    
    # Store raw content for analysis
    with open(f"scripts/data/{source['name']}_raw.txt", "w", encoding="utf-8") as f:
        f.write(text_content)
    
    print(f"Saved raw content for {source['name']}")
    return text_content

def run_scraper():
    """Run the scraping process for all sources"""
    results = {}
    
    # Scrape each website
    for source in SOURCES:
        content = scrape_website(source)
        if content:
            results[source['name']] = {
                "url": source['url'],
                "content": content[:5000],  # Truncate content for summary
                "country_focus": source['country'],
                "scrape_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
    
    # Save results
    with open("scripts/data/scraped_sites.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    
    # Combine manually curated lists
    all_tools = INDIAN_AI_TOOLS + GLOBAL_AI_TOOLS
    
    # Save the combined list
    with open("scripts/data/ai_tools.json", "w", encoding="utf-8") as f:
        json.dump(all_tools, f, indent=2)
    
    print(f"Scraping complete. Added {len(INDIAN_AI_TOOLS)} Indian AI tools and {len(GLOBAL_AI_TOOLS)} global AI tools.")
    return all_tools

if __name__ == "__main__":
    run_scraper()