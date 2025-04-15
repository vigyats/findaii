import os
import logging
from flask import Flask, render_template, request, jsonify, url_for
from data.tools import ai_tools, categories

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Create Flask app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET")

# Helper functions for templates
def get_category_icon(category):
    """Get the appropriate icon for a category"""
    icons = {
        'Text Generation': 'chat-square-text',
        'Image Generation': 'image',
        'Audio Generation': 'soundwave',
        'Multimodal': 'intersect',
        'Code Assistance': 'code-square',
        'Video Creation': 'film',
        'Data Analysis': 'graph-up',
        'Conversational AI': 'chat',
        'Content Writing': 'file-text',
        'Design Tools': 'palette',
        'Education Tools': 'book',
        'Business Tools': 'briefcase'
    }
    return icons.get(category, 'stars')

def get_category_description(category):
    """Get the description for a category"""
    descriptions = {
        'Text Generation': 'Create high-quality written content with AI that can write articles, stories, and more.',
        'Image Generation': 'Transform text prompts into stunning visuals with these AI image generators.',
        'Audio Generation': 'Create music, sound effects, and voice content using audio AI tools.',
        'Multimodal': 'Tools that combine multiple AI capabilities like text, image, and audio processing.',
        'Code Assistance': 'Get help with programming tasks from AI coding assistants and tools.',
        'Video Creation': 'Transform ideas into videos with AI-powered video generation and editing tools.',
        'Data Analysis': 'Make sense of complex data with AI-powered analytics and visualization tools.',
        'Conversational AI': 'Interact with AI chatbots and assistants that can answer questions and provide help.',
        'Content Writing': 'Generate articles, blog posts, and marketing copy with AI writing tools.',
        'Design Tools': 'Create stunning designs, logos, and visuals with AI design assistants.',
        'Education Tools': 'Enhance learning and teaching with educational AI tools and resources.',
        'Business Tools': 'Boost productivity and streamline workflows with AI business tools.'
    }
    return descriptions.get(category, 'Discover the latest free AI tools in this category.')

# Helper function for random icons
def get_random_icon():
    """Generate a random icon for similar tools section"""
    import random
    icons = [
        'chat-square-text', 'image', 'soundwave', 'intersect', 
        'code-square', 'film', 'graph-up', 'chat', 'lightning',
        'pencil-square', 'palette', 'book'
    ]
    return random.choice(icons)

# Register helper functions with Jinja environment
app.jinja_env.globals.update(
    get_category_icon=get_category_icon,
    get_category_description=get_category_description,
    get_random_icon=get_random_icon
)

@app.route('/')
def index():
    """Render the home page with all AI tools categorized"""
    return render_template('index.html', categories=categories, tools=ai_tools)

@app.route('/tool/<tool_id>')
def tool_detail(tool_id):
    """Render the detail page for a specific AI tool"""
    # Find the tool by ID
    tool = None
    for category in ai_tools:
        for t in category['tools']:
            if t['id'] == tool_id:
                tool = t
                break
        if tool:
            break
    
    if tool:
        return render_template('tool_detail.html', tool=tool)
    else:
        return render_template('index.html', categories=categories, tools=ai_tools, error="Tool not found")

@app.route('/search')
def search():
    """Search for AI tools by name or description"""
    query = request.args.get('query', '').lower()
    results = []
    
    if query:
        for category in ai_tools:
            for tool in category['tools']:
                if (query in tool['name'].lower() or 
                    query in tool['description'].lower() or
                    query in tool['category'].lower()):
                    results.append(tool)
    
    return render_template('index.html', 
                           categories=categories, 
                           tools=ai_tools,
                           search_results=results, 
                           query=query)

@app.route('/filter/<category>')
def filter_category(category):
    """Filter AI tools by category"""
    filtered_tools = []
    formatted_category = category.replace('-', ' ').title()
    
    for cat in ai_tools:
        if cat['category'].lower() == formatted_category.lower():
            filtered_tools = cat['tools']
            break
    
    return render_template('index.html', 
                           categories=categories, 
                           tools=ai_tools,
                           filtered_category=formatted_category,
                           filtered_tools=filtered_tools)

@app.route('/about')
def about():
    """Render the about page"""
    return render_template('about.html', categories=categories)

@app.route('/developer')
def developer():
    """Render the developer profile page"""
    return render_template('developer.html', categories=categories)

@app.context_processor
def inject_copyright():
    """Inject copyright information into all templates"""
    return {
        'copyright_year': 2025,
        'copyright_owner': 'Vigyat Singh',
        'app_version': '2.0.0'
    }

@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors"""
    return render_template('index.html', categories=categories, tools=ai_tools, error="Page not found"), 404

@app.errorhandler(500)
def server_error(e):
    """Handle 500 errors"""
    return render_template('index.html', categories=categories, tools=ai_tools, error="Server error occurred"), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
