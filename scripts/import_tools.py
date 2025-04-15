"""
AI Tools Importer

This script imports AI tools from our scraper into the FindAI app database.
"""

import json
import os
import sys
import random

# Add the project directory to Python path
sys.path.append('.')

# Import Flask app and database models
from app import app, db
from data.tools import ai_tools, AI_TOOL_CATEGORIES, update_tool_in_database

def get_category_for_tool(tool_category):
    """Map the scraped tool category to our predefined categories"""
    # Map of category synonyms to our predefined categories
    category_mapping = {
        # Writing
        "writing": "content_creation",
        "content": "content_creation",
        "copywriting": "content_creation",
        
        # Image Generation
        "image": "image_generation",
        "image generation": "image_generation",
        "art": "image_generation",
        
        # Video
        "video": "video_editing",
        "video generation": "video_editing",
        "video editing": "video_editing",
        
        # Audio/Voice
        "audio": "music_audio",
        "voice": "music_audio",
        "music": "music_audio",
        "music generation": "music_audio",
        
        # Language Models
        "language model": "ai_assistants",
        "language": "ai_assistants",
        "chatbot": "ai_assistants",
        "assistant": "ai_assistants",
        
        # Coding
        "coding": "developer_tools",
        "code": "developer_tools",
        "programming": "developer_tools",
        "developer": "developer_tools",
        
        # Productivity
        "productivity": "productivity",
        "automation": "productivity",
        "workflow": "productivity",
        
        # Healthcare
        "healthcare": "healthcare",
        "medical": "healthcare",
        "health": "healthcare",
        
        # Finance
        "finance": "business_finance",
        "financial": "business_finance",
        "business": "business_finance",
        
        # Education
        "education": "education",
        "learning": "education",
        "teaching": "education",
        
        # Marketing
        "marketing": "marketing",
        "seo": "marketing",
        "social media": "marketing",
        
        # Design
        "design": "design",
        "ui": "design",
        "ux": "design",
        
        # Translation
        "translation": "language_translation",
        "translate": "language_translation",
        "language translation": "language_translation",
        
        # Search
        "search": "research_tools",
        "research": "research_tools",
    }
    
    # Check if the category is directly in our list
    if tool_category.lower() in [cat.lower() for cat in AI_TOOL_CATEGORIES.keys()]:
        for cat_key in AI_TOOL_CATEGORIES.keys():
            if tool_category.lower() == cat_key.lower():
                return cat_key
    
    # Try to match with our mapping
    for key, value in category_mapping.items():
        if key in tool_category.lower():
            return value
    
    # If no match, use a default category
    default_categories = ["other", "ai_assistants", "productivity"]
    return random.choice(default_categories)

def import_tools_from_json():
    """Import AI tools from the scraped JSON file"""
    json_file = "scripts/data/ai_tools.json"
    
    if not os.path.exists(json_file):
        print(f"Error: {json_file} not found. Run the scraper first.")
        return False
    
    try:
        with open(json_file, "r", encoding="utf-8") as f:
            scraped_tools = json.load(f)
    except Exception as e:
        print(f"Error loading JSON file: {str(e)}")
        return False
    
    # Track current tool IDs to avoid duplicates
    existing_tool_names = set(tool['name'].lower() for tool in ai_tools)
    
    # Count of added and updated tools
    added_count = 0
    updated_count = 0
    
    print(f"Processing {len(scraped_tools)} scraped tools...")
    
    for tool in scraped_tools:
        # Basic validation
        if not all(key in tool for key in ['name', 'url', 'description', 'category']):
            print(f"Skipping incomplete tool: {tool.get('name', 'Unknown')}")
            continue
        
        # Check if tool already exists
        tool_name_lower = tool['name'].lower()
        if tool_name_lower in existing_tool_names:
            # Update existing tool with new information
            for i, existing_tool in enumerate(ai_tools):
                if existing_tool['name'].lower() == tool_name_lower:
                    # Keep the original ID but update other fields
                    tool_id = existing_tool['id']
                    
                    # Map the category
                    mapped_category = get_category_for_tool(tool['category'])
                    
                    # Create combined tool with updated information
                    updated_tool = {
                        'id': tool_id,
                        'name': tool['name'],
                        'category': mapped_category,
                        'url': tool['url'],
                        'description': tool['description'],
                        'pricing': tool.get('pricing', 'Unknown'),
                        'icon': existing_tool.get('icon', 'bi-stars'), # Keep original icon
                        'is_featured': existing_tool.get('is_featured', False),
                    }
                    
                    # Update tool in our list
                    ai_tools[i] = updated_tool
                    updated_count += 1
                    print(f"Updated existing tool: {tool['name']}")
                    break
        else:
            # Add new tool
            # Generate a new ID
            new_id = max([t['id'] for t in ai_tools], default=0) + 1
            
            # Map the category
            mapped_category = get_category_for_tool(tool['category'])
            
            # Choose a random icon based on the category
            category_icons = {
                'ai_assistants': ['bi-robot', 'bi-chat-dots', 'bi-chat-square-text'],
                'image_generation': ['bi-image', 'bi-palette', 'bi-camera'],
                'content_creation': ['bi-pencil-square', 'bi-file-text', 'bi-blockquote-left'],
                'music_audio': ['bi-music-note', 'bi-soundwave', 'bi-headphones'],
                'video_editing': ['bi-camera-video', 'bi-film', 'bi-play-circle'],
                'productivity': ['bi-speedometer', 'bi-gear', 'bi-lightning'],
                'developer_tools': ['bi-code-square', 'bi-braces', 'bi-terminal'],
                'business_finance': ['bi-cash-coin', 'bi-graph-up', 'bi-briefcase'],
                'education': ['bi-book', 'bi-mortarboard', 'bi-pencil'],
                'design': ['bi-brush', 'bi-palette2', 'bi-vector-pen'],
                'marketing': ['bi-megaphone', 'bi-bullseye', 'bi-graph-up-arrow'],
                'research_tools': ['bi-search', 'bi-binoculars', 'bi-journal-text'],
                'language_translation': ['bi-translate', 'bi-globe', 'bi-chat-quote'],
                'healthcare': ['bi-heart-pulse', 'bi-hospital', 'bi-activity'],
                'other': ['bi-stars', 'bi-tools', 'bi-boxes']
            }
            
            # Select an icon from the category or use a default
            icon = random.choice(category_icons.get(mapped_category, ['bi-stars', 'bi-lightning', 'bi-magic']))
            
            # Create new tool
            new_tool = {
                'id': new_id,
                'name': tool['name'],
                'category': mapped_category,
                'url': tool['url'],
                'description': tool['description'],
                'pricing': tool.get('pricing', 'Unknown'),
                'icon': icon,
                'is_featured': False,  # New tools are not featured by default
            }
            
            # Add to our list
            ai_tools.append(new_tool)
            existing_tool_names.add(tool_name_lower)
            added_count += 1
            print(f"Added new tool: {tool['name']}")
    
    # Save the updated tools file
    with app.app_context():
        # Update the database
        print("Updating database with new and modified tools...")
        for tool in ai_tools:
            update_tool_in_database(tool)
    
    print(f"Import complete. Added {added_count} new tools, updated {updated_count} existing tools.")
    return True

if __name__ == '__main__':
    import_tools_from_json()