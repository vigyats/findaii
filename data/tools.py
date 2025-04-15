# Database connection will be handled in app.py

# Define categories for AI tools with icons and descriptions
AI_TOOL_CATEGORIES = {
    "ai_assistants": {
        "name": "AI Assistants",
        "icon": "bi-robot",
        "description": "Conversational AI tools for chat and assistance"
    },
    "image_generation": {
        "name": "Image Generation",
        "icon": "bi-image",
        "description": "Create images, art, and visuals with AI"
    },
    "content_creation": {
        "name": "Content Creation",
        "icon": "bi-pencil-square",
        "description": "Generate blog posts, articles, and marketing copy"
    },
    "music_audio": {
        "name": "Music & Audio",
        "icon": "bi-music-note",
        "description": "Create music, sounds, and voice content"
    },
    "video_editing": {
        "name": "Video Tools",
        "icon": "bi-camera-video",
        "description": "AI for video creation, editing, and enhancement"
    },
    "productivity": {
        "name": "Productivity",
        "icon": "bi-speedometer",
        "description": "Tools to boost efficiency and workflow"
    },
    "developer_tools": {
        "name": "Developer Tools",
        "icon": "bi-code-square",
        "description": "Code generation, debugging, and development assistance"
    },
    "business_finance": {
        "name": "Business & Finance",
        "icon": "bi-graph-up",
        "description": "Tools for business operations and financial analysis"
    },
    "education": {
        "name": "Education",
        "icon": "bi-book",
        "description": "Learning resources and educational AI"
    },
    "design": {
        "name": "Design",
        "icon": "bi-palette",
        "description": "UI/UX, graphic design, and creative tools"
    },
    "marketing": {
        "name": "Marketing",
        "icon": "bi-megaphone",
        "description": "Marketing, SEO, and social media AI tools"
    },
    "research_tools": {
        "name": "Research Tools",
        "icon": "bi-search",
        "description": "Information gathering and analysis tools"
    },
    "language_translation": {
        "name": "Language & Translation",
        "icon": "bi-translate",
        "description": "Translate and work with multiple languages"
    },
    "healthcare": {
        "name": "Healthcare",
        "icon": "bi-heart-pulse",
        "description": "Medical and healthcare AI applications"
    },
    "other": {
        "name": "Other AI Tools",
        "icon": "bi-stars",
        "description": "Specialized and emerging AI applications"
    }
}

# Create a simplified list of categories for backward compatibility
categories = list(AI_TOOL_CATEGORIES.keys())

# Function to update tool in database - implemented in app.py
def update_tool_in_database(tool):
    """This function is implemented in app.py to avoid circular imports"""
    pass

# Define AI tools organized by categories
ai_tools = [
    {
        "category": "Text Generation",
        "tools": [
            {
                "id": "text-1",
                "name": "ChatGPT",
                "description": "Conversational AI assistant that can generate text responses on various topics",
                "url": "https://chat.openai.com",
                "category": "Text Generation",
                "capabilities": [
                    "Answer questions",
                    "Write essays and content",
                    "Summarize text",
                    "Creative writing assistance"
                ],
                "limitations": "May occasionally produce incorrect information",
                "logo": "chat-square-text"
            },
            {
                "id": "text-2",
                "name": "Hugging Face",
                "description": "Open-source platform providing access to thousands of pretrained NLP models",
                "url": "https://huggingface.co",
                "category": "Text Generation",
                "capabilities": [
                    "Text generation",
                    "Text classification",
                    "Question answering",
                    "Text summarization"
                ],
                "limitations": "Quality varies by model",
                "logo": "braces"
            },
            {
                "id": "text-3",
                "name": "Claude.ai",
                "description": "AI assistant that aims to be helpful, harmless, and honest in conversation",
                "url": "https://claude.ai",
                "category": "Text Generation",
                "capabilities": [
                    "Natural conversations",
                    "Helpful responses",
                    "Creative writing",
                    "Document analysis"
                ],
                "limitations": "May decline certain requests",
                "logo": "chat-dots"
            },
            {
                "id": "text-4",
                "name": "OpenAssistant",
                "description": "Open-source project building an assistant that operates transparently and is freely available",
                "url": "https://open-assistant.io",
                "category": "Text Generation",
                "capabilities": [
                    "Natural language understanding",
                    "Conversation capabilities",
                    "Open-source development"
                ],
                "limitations": "Still in development with evolving capabilities",
                "logo": "people"
            },
            {
                "id": "text-5",
                "name": "Bard AI",
                "description": "Google's experimental conversational AI service powered by LaMDA",
                "url": "https://bard.google.com",
                "category": "Text Generation",
                "capabilities": [
                    "Generate text content",
                    "Answer questions",
                    "Creative collaboration"
                ],
                "limitations": "Sometimes provides inaccurate information",
                "logo": "google"
            },
            {
                "id": "text-6",
                "name": "Writer.com Free Tools",
                "description": "Collection of free AI writing tools for various specific tasks",
                "url": "https://writer.com/free-tools/",
                "category": "Text Generation",
                "capabilities": [
                    "Paraphrasing tool",
                    "AI text detector",
                    "Grammar checker"
                ],
                "limitations": "Limited length for free tier tools",
                "logo": "pencil-square"
            },
            {
                "id": "text-7",
                "name": "Llama 2",
                "description": "Open-source large language model developed by Meta available for free use",
                "url": "https://ai.meta.com/llama/",
                "category": "Text Generation",
                "capabilities": [
                    "Text generation",
                    "Fine-tuning for specific uses",
                    "Local deployment option"
                ],
                "limitations": "Requires technical knowledge to implement",
                "logo": "meta"
            },
            {
                "id": "text-8",
                "name": "Falcon",
                "description": "Open-source large language model trained by the Technology Innovation Institute",
                "url": "https://falconllm.tii.ae/",
                "category": "Text Generation",
                "capabilities": [
                    "Text generation",
                    "Question answering",
                    "Multiple model sizes"
                ],
                "limitations": "May require significant computing resources",
                "logo": "lightning"
            }
        ]
    },
    {
        "category": "Image Generation",
        "tools": [
            {
                "id": "image-1",
                "name": "Midjourney (Free Trial)",
                "description": "AI art generator creating stunning images from text prompts with limited free access via Discord",
                "url": "https://www.midjourney.com",
                "category": "Image Generation",
                "capabilities": [
                    "High-quality image generation",
                    "Style customization",
                    "Artistic image creation"
                ],
                "limitations": "Limited free trial images",
                "logo": "palette2"
            },
            {
                "id": "image-2",
                "name": "Stable Diffusion",
                "description": "Open-source text-to-image model that can run locally on consumer hardware",
                "url": "https://huggingface.co/spaces/stabilityai/stable-diffusion",
                "category": "Image Generation",
                "capabilities": [
                    "High-quality image generation",
                    "Artistic style control",
                    "Image-to-image editing"
                ],
                "limitations": "Requires specific prompt engineering for best results",
                "logo": "palette"
            },
            {
                "id": "image-3",
                "name": "Craiyon",
                "description": "Free AI image generator from text descriptions (formerly DALL-E Mini)",
                "url": "https://www.craiyon.com",
                "category": "Image Generation",
                "capabilities": [
                    "Create images from text",
                    "Multiple image variations",
                    "Accessible interface"
                ],
                "limitations": "Lower quality than premium alternatives",
                "logo": "brush"
            },
            {
                "id": "image-4",
                "name": "DALL-E (Limited Free)",
                "description": "OpenAI's text-to-image model with a limited free tier for creating realistic images",
                "url": "https://labs.openai.com",
                "category": "Image Generation",
                "capabilities": [
                    "High-quality image generation",
                    "Realistic rendering",
                    "Creative concept visualization"
                ],
                "limitations": "Limited free credits per month",
                "logo": "box"
            },
            {
                "id": "image-5",
                "name": "Leonardo.AI",
                "description": "AI image generator with a generous free tier for creating various art styles",
                "url": "https://leonardo.ai",
                "category": "Image Generation",
                "capabilities": [
                    "Custom style training",
                    "High-resolution outputs",
                    "Multiple generation styles"
                ],
                "limitations": "Limited daily generations in free tier",
                "logo": "easel"
            },
            {
                "id": "image-6",
                "name": "Canva Text to Image",
                "description": "Free text-to-image generator integrated into Canva's design platform",
                "url": "https://www.canva.com/ai-image-generator/",
                "category": "Image Generation",
                "capabilities": [
                    "Integrated with design tools",
                    "Multiple styles available",
                    "Easy to use interface"
                ],
                "limitations": "Limited generations in free tier",
                "logo": "vector-pen"
            },
            {
                "id": "image-7",
                "name": "Bing Image Creator",
                "description": "Microsoft's free DALL-E powered image generator available through Bing",
                "url": "https://www.bing.com/create",
                "category": "Image Generation",
                "capabilities": [
                    "High-quality image generation",
                    "No account required",
                    "Multiple art styles"
                ],
                "limitations": "Daily usage limits",
                "logo": "microsoft"
            },
            {
                "id": "image-8",
                "name": "Playground AI",
                "description": "User-friendly AI image generation platform with limited free tier",
                "url": "https://playgroundai.com",
                "category": "Image Generation",
                "capabilities": [
                    "High-quality generation",
                    "Multiple models available",
                    "Community sharing features"
                ],
                "limitations": "Limited free generations per day",
                "logo": "stars"
            }
        ]
    },
    {
        "category": "Audio Generation",
        "tools": [
            {
                "id": "audio-1",
                "name": "Suno AI",
                "description": "Create original songs with lyrics and music using simple text prompts",
                "url": "https://suno.ai",
                "category": "Audio Generation",
                "capabilities": [
                    "Create full songs from text",
                    "Multiple genre options",
                    "High-quality vocal synthesis"
                ],
                "limitations": "Limited free tier generations",
                "logo": "music-note"
            },
            {
                "id": "audio-2",
                "name": "Bark",
                "description": "Open-source text-to-audio model that can generate realistic speech",
                "url": "https://github.com/suno-ai/bark",
                "category": "Audio Generation",
                "capabilities": [
                    "Text-to-speech synthesis",
                    "Voice cloning",
                    "Sound effects generation"
                ],
                "limitations": "Limited voice customization options",
                "logo": "mic"
            },
            {
                "id": "audio-3",
                "name": "Mubert",
                "description": "AI-powered music generation platform with free usage options",
                "url": "https://mubert.com",
                "category": "Audio Generation",
                "capabilities": [
                    "Generate royalty-free music",
                    "Customizable by mood/genre",
                    "Streaming-ready output"
                ],
                "limitations": "Limited length and download options in free tier",
                "logo": "music-player"
            },
            {
                "id": "audio-4",
                "name": "Speak",
                "description": "Simple text-to-speech tool with natural-sounding voices",
                "url": "https://www.speak.com",
                "category": "Audio Generation",
                "capabilities": [
                    "High-quality TTS",
                    "Multiple voice options",
                    "Natural intonation"
                ],
                "limitations": "Limited free usage",
                "logo": "mic-fill"
            },
            {
                "id": "audio-5",
                "name": "AudioLM",
                "description": "Language modeling approach to audio generation from Google Research",
                "url": "https://google-research.github.io/seanet/audiolm/examples/",
                "category": "Audio Generation",
                "capabilities": [
                    "Speech continuation",
                    "Music generation",
                    "Sound synthesis"
                ],
                "limitations": "Research model with limited access",
                "logo": "soundwave"
            },
            {
                "id": "audio-6",
                "name": "PlayHT",
                "description": "AI voice generator with free tier access to basic voices",
                "url": "https://play.ht",
                "category": "Audio Generation",
                "capabilities": [
                    "Text-to-speech",
                    "Multiple voice options",
                    "Emotion control"
                ],
                "limitations": "Limited word count in free tier",
                "logo": "headphones"
            },
            {
                "id": "audio-7",
                "name": "MusicLM",
                "description": "Generate music from text descriptions with impressive quality",
                "url": "https://google-research.github.io/seanet/musiclm/examples/",
                "category": "Audio Generation",
                "capabilities": [
                    "Text-to-music generation",
                    "Style-based music creation",
                    "Instrumental composition"
                ],
                "limitations": "Limited to short clips in demo",
                "logo": "music-note-beamed"
            },
            {
                "id": "audio-8",
                "name": "Free TTS",
                "description": "Simple free text-to-speech converter with multiple voices",
                "url": "https://freetts.com",
                "category": "Audio Generation",
                "capabilities": [
                    "Basic text-to-speech",
                    "Multiple language support",
                    "No account required"
                ],
                "limitations": "Basic voice quality",
                "logo": "speaker"
            }
        ]
    },
    {
        "category": "Multimodal",
        "tools": [
            {
                "id": "multi-1",
                "name": "GPT-4 Vision (Limited Free)",
                "description": "OpenAI's multimodal model that can process both text and images",
                "url": "https://openai.com/research/gpt-4",
                "category": "Multimodal",
                "capabilities": [
                    "Understand and analyze images",
                    "Answer questions about visual content",
                    "Extract text from images"
                ],
                "limitations": "May misinterpret complex visual scenes",
                "logo": "eye"
            },
            {
                "id": "multi-2",
                "name": "CLIP",
                "description": "OpenAI's model connecting text and images for zero-shot predictions",
                "url": "https://github.com/openai/CLIP",
                "category": "Multimodal",
                "capabilities": [
                    "Image classification",
                    "Text-image matching",
                    "Zero-shot learning"
                ],
                "limitations": "Limited to classification tasks",
                "logo": "link-45deg"
            },
            {
                "id": "multi-3",
                "name": "LLaVA",
                "description": "Large Language and Vision Assistant for multimodal tasks",
                "url": "https://llava-vl.github.io",
                "category": "Multimodal",
                "capabilities": [
                    "Visual question answering",
                    "Image captioning",
                    "Visual reasoning"
                ],
                "limitations": "Research project with evolving capabilities",
                "logo": "binoculars"
            },
            {
                "id": "multi-4",
                "name": "Fuyu-8B",
                "description": "Open-source multimodal model for image and text understanding",
                "url": "https://huggingface.co/adept/fuyu-8b",
                "category": "Multimodal",
                "capabilities": [
                    "Image-to-text generation",
                    "Visual question answering",
                    "Text and image understanding"
                ],
                "limitations": "Smaller model with some limitations compared to larger options",
                "logo": "images"
            },
            {
                "id": "multi-5",
                "name": "ImageBind",
                "description": "Meta's model for binding different modalities like image, text, audio",
                "url": "https://github.com/facebookresearch/ImageBind",
                "category": "Multimodal",
                "capabilities": [
                    "Cross-modal understanding",
                    "Unified embeddings across modalities",
                    "Multimodal retrieval"
                ],
                "limitations": "Requires technical knowledge to implement",
                "logo": "app"
            },
            {
                "id": "multi-6",
                "name": "CogVLM",
                "description": "Open-source visual language model with competitive performance",
                "url": "https://github.com/THUDM/CogVLM",
                "category": "Multimodal",
                "capabilities": [
                    "Visual question answering",
                    "Image captioning",
                    "Visual reasoning"
                ],
                "limitations": "Requires GPU resources for optimal performance",
                "logo": "cpu"
            }
        ]
    },
    {
        "category": "Code Assistance",
        "tools": [
            {
                "id": "code-1",
                "name": "Replit Ghostwriter",
                "description": "AI coding assistant integrated with Replit's online IDE with generous free tier",
                "url": "https://replit.com/ghostwriter",
                "category": "Code Assistance",
                "capabilities": [
                    "Code generation",
                    "Code explanation",
                    "Bug fixing"
                ],
                "limitations": "Limited usage in free tier",
                "logo": "code-slash"
            },
            {
                "id": "code-2",
                "name": "GitHub Copilot (Free for Students)",
                "description": "AI pair programmer that suggests code completions as you type",
                "url": "https://github.com/features/copilot",
                "category": "Code Assistance",
                "capabilities": [
                    "Code completion",
                    "Generate functions from comments",
                    "Suggest similar patterns"
                ],
                "limitations": "Free only for verified students",
                "logo": "code-square"
            },
            {
                "id": "code-3",
                "name": "Tabnine",
                "description": "AI code completion assistant with free community version",
                "url": "https://www.tabnine.com",
                "category": "Code Assistance",
                "capabilities": [
                    "Code completion",
                    "Code snippets",
                    "Language support for many frameworks"
                ],
                "limitations": "Free version has usage limitations",
                "logo": "code"
            },
            {
                "id": "code-4",
                "name": "CodeWhisperer",
                "description": "Amazon's AI code generator with free tier for individual developers",
                "url": "https://aws.amazon.com/codewhisperer",
                "category": "Code Assistance",
                "capabilities": [
                    "Code suggestions",
                    "Security scanning",
                    "Documentation insights"
                ],
                "limitations": "Works best with AWS services",
                "logo": "terminal"
            },
            {
                "id": "code-5",
                "name": "Codeium",
                "description": "Free AI-powered code completion tool with support for multiple editors",
                "url": "https://codeium.com",
                "category": "Code Assistance",
                "capabilities": [
                    "Code completion",
                    "Multiple IDE support",
                    "Natural language to code"
                ],
                "limitations": "May not match commercial tools in accuracy",
                "logo": "lightning"
            },
            {
                "id": "code-6",
                "name": "DeepSeek Coder",
                "description": "Open-source code model for understanding and generating code",
                "url": "https://github.com/deepseek-ai/DeepSeek-Coder",
                "category": "Code Assistance",
                "capabilities": [
                    "Code generation",
                    "Code understanding",
                    "Multiple programming language support"
                ],
                "limitations": "Requires setup to use locally",
                "logo": "file-earmark-code"
            },
            {
                "id": "code-7",
                "name": "CodeGPT",
                "description": "Open-source AI code assistant based on GPT models",
                "url": "https://codegpt.co",
                "category": "Code Assistance",
                "capabilities": [
                    "Code completion",
                    "Code generation",
                    "IDE integration"
                ],
                "limitations": "Community version has limitations compared to paid versions",
                "logo": "braces-asterisk"
            },
            {
                "id": "code-8",
                "name": "StackSpot AI",
                "description": "Free AI code assistant with focus on code generation and explanation",
                "url": "https://stackspot.com",
                "category": "Code Assistance",
                "capabilities": [
                    "Code generation",
                    "Code explanation",
                    "Framework-specific assistance"
                ],
                "limitations": "Limited usage in free tier",
                "logo": "layers"
            }
        ]
    },
    {
        "category": "Video Creation",
        "tools": [
            {
                "id": "video-1",
                "name": "Runway Gen-2",
                "description": "Text-to-video AI model with free demo capabilities",
                "url": "https://research.runwayml.com/gen2",
                "category": "Video Creation",
                "capabilities": [
                    "Generate short videos from text",
                    "Image-to-video transformation",
                    "Style transfer for videos"
                ],
                "limitations": "Free tier has length and quality restrictions",
                "logo": "film"
            },
            {
                "id": "video-2",
                "name": "GEN-1",
                "description": "Runway's tool for applying visual effects and transformations to existing videos",
                "url": "https://research.runwayml.com/gen1",
                "category": "Video Creation",
                "capabilities": [
                    "Style transfer",
                    "Visual effects",
                    "Video editing"
                ],
                "limitations": "Requires existing video footage",
                "logo": "camera-reels"
            },
            {
                "id": "video-3",
                "name": "Lumen5",
                "description": "Video creation platform with AI-powered features and free plan",
                "url": "https://lumen5.com",
                "category": "Video Creation",
                "capabilities": [
                    "Convert text to video",
                    "Auto scene selection",
                    "Media library access"
                ],
                "limitations": "Free plan has watermark",
                "logo": "play-btn"
            },
            {
                "id": "video-4",
                "name": "Synthesia (Limited Free)",
                "description": "AI video generation platform with avatar presenters and limited free access",
                "url": "https://www.synthesia.io",
                "category": "Video Creation",
                "capabilities": [
                    "AI avatars",
                    "Text-to-video",
                    "Multiple languages"
                ],
                "limitations": "Very limited free tier",
                "logo": "person-video"
            },
            {
                "id": "video-5",
                "name": "Kapwing",
                "description": "Online video editor with AI features and free tier",
                "url": "https://www.kapwing.com",
                "category": "Video Creation",
                "capabilities": [
                    "Video editing",
                    "Subtitles generation",
                    "Image enhancement"
                ],
                "limitations": "Watermark in free version",
                "logo": "film"
            },
            {
                "id": "video-6",
                "name": "InVideo",
                "description": "AI-powered video creation platform with free tier",
                "url": "https://invideo.io",
                "category": "Video Creation",
                "capabilities": [
                    "Text to video",
                    "Template-based creation",
                    "Media library"
                ],
                "limitations": "Watermark in free version",
                "logo": "camera-video"
            },
            {
                "id": "video-7",
                "name": "Pictory",
                "description": "AI video generator that turns text into videos with free trial",
                "url": "https://pictory.ai",
                "category": "Video Creation",
                "capabilities": [
                    "Text to video",
                    "Script to video",
                    "Auto B-roll generation"
                ],
                "limitations": "Limited functionality in free tier",
                "logo": "play-circle"
            }
        ]
    },
    {
        "category": "Data Analysis",
        "tools": [
            {
                "id": "data-1",
                "name": "Orange Data Mining",
                "description": "Open-source data visualization and analysis tool with machine learning components",
                "url": "https://orangedatamining.com",
                "category": "Data Analysis",
                "capabilities": [
                    "Visual programming for data analysis",
                    "Machine learning model building",
                    "Data visualization"
                ],
                "limitations": "Steeper learning curve for advanced features",
                "logo": "graph-up"
            },
            {
                "id": "data-2",
                "name": "KNIME",
                "description": "Open-source analytics platform with free version",
                "url": "https://www.knime.com",
                "category": "Data Analysis",
                "capabilities": [
                    "Data blending",
                    "Visual workflow creation",
                    "Machine learning"
                ],
                "limitations": "Advanced features require paid version",
                "logo": "table"
            },
            {
                "id": "data-3",
                "name": "RapidMiner",
                "description": "Data science platform with free tier for individuals",
                "url": "https://rapidminer.com",
                "category": "Data Analysis",
                "capabilities": [
                    "Data preparation",
                    "Machine learning",
                    "Model deployment"
                ],
                "limitations": "Row and processing limitations in free version",
                "logo": "bar-chart"
            },
            {
                "id": "data-4",
                "name": "Google Colab",
                "description": "Free cloud-based Jupyter notebook environment with AI libraries",
                "url": "https://colab.research.google.com",
                "category": "Data Analysis",
                "capabilities": [
                    "Python notebook environment",
                    "Free GPU access",
                    "Pre-installed ML libraries"
                ],
                "limitations": "Limited computing resources in free tier",
                "logo": "google"
            },
            {
                "id": "data-5",
                "name": "Tableau Public",
                "description": "Free version of popular data visualization software",
                "url": "https://public.tableau.com",
                "category": "Data Analysis",
                "capabilities": [
                    "Interactive visualizations",
                    "Data dashboard creation",
                    "Sharing capabilities"
                ],
                "limitations": "All visualizations are public",
                "logo": "pie-chart"
            },
            {
                "id": "data-6",
                "name": "Dataiku Free Edition",
                "description": "Data science platform with limited free version",
                "url": "https://www.dataiku.com/product/free-edition",
                "category": "Data Analysis",
                "capabilities": [
                    "Data preparation",
                    "Visual workflows",
                    "Basic ML capabilities"
                ],
                "limitations": "Limited to one user",
                "logo": "diagram-3"
            },
            {
                "id": "data-7",
                "name": "Kaggle",
                "description": "Platform for data science competitions with notebooks and datasets",
                "url": "https://www.kaggle.com",
                "category": "Data Analysis",
                "capabilities": [
                    "Notebook environment",
                    "Free GPU access",
                    "Dataset access"
                ],
                "limitations": "Usage limits on compute resources",
                "logo": "journal-code"
            }
        ]
    },
    {
        "category": "Conversational AI",
        "tools": [
            {
                "id": "conv-1",
                "name": "Hugging Face Chat",
                "description": "Open-source conversation models you can try directly in your browser",
                "url": "https://huggingface.co/chat",
                "category": "Conversational AI",
                "capabilities": [
                    "Text chat with multiple models",
                    "Compare different AI approaches",
                    "No login required"
                ],
                "limitations": "Quality varies by selected model",
                "logo": "chat"
            },
            {
                "id": "conv-2",
                "name": "Poe",
                "description": "Platform to interact with multiple AI chatbots for free",
                "url": "https://poe.com",
                "category": "Conversational AI",
                "capabilities": [
                    "Access to multiple AI models",
                    "Chat history",
                    "Custom bot creation"
                ],
                "limitations": "Usage limits on premium models",
                "logo": "chat-left-dots"
            },
            {
                "id": "conv-3",
                "name": "Perplexity",
                "description": "Conversational search engine with AI-powered responses",
                "url": "https://www.perplexity.ai",
                "category": "Conversational AI",
                "capabilities": [
                    "Web search with AI summaries",
                    "Citation of sources",
                    "Follow-up questions"
                ],
                "limitations": "Limited number of queries in free version",
                "logo": "search"
            },
            {
                "id": "conv-4",
                "name": "Character.AI",
                "description": "Platform for creating and chatting with AI characters",
                "url": "https://character.ai",
                "category": "Conversational AI",
                "capabilities": [
                    "Create custom AI characters",
                    "Chat with fictional personas",
                    "Community-created characters"
                ],
                "limitations": "Content restrictions",
                "logo": "person-circle"
            },
            {
                "id": "conv-5",
                "name": "ChatSonic",
                "description": "AI chatbot with real-time information and voice capability",
                "url": "https://writesonic.com/chat",
                "category": "Conversational AI",
                "capabilities": [
                    "Real-time information access",
                    "Voice conversations",
                    "Image generation"
                ],
                "limitations": "Limited prompts in free tier",
                "logo": "megaphone"
            },
            {
                "id": "conv-6",
                "name": "Pi",
                "description": "Personal AI assistant focused on being helpful and friendly",
                "url": "https://heypi.com",
                "category": "Conversational AI",
                "capabilities": [
                    "Personal conversations",
                    "Writing assistance",
                    "Creative collaboration"
                ],
                "limitations": "May provide generic responses",
                "logo": "chat-heart"
            },
            {
                "id": "conv-7",
                "name": "Replika",
                "description": "AI companion focused on friendly conversations",
                "url": "https://replika.ai",
                "category": "Conversational AI",
                "capabilities": [
                    "Emotional support",
                    "Casual conversation",
                    "Personalized responses"
                ],
                "limitations": "Advanced features require subscription",
                "logo": "emoji-smile"
            },
            {
                "id": "conv-8",
                "name": "BlenderBot",
                "description": "Meta's publicly available chatbot focused on safety and privacy",
                "url": "https://blenderbot.ai",
                "category": "Conversational AI",
                "capabilities": [
                    "Long-term memory",
                    "Internet searching",
                    "Learning from conversations"
                ],
                "limitations": "Sometimes provides incorrect information",
                "logo": "chat-text"
            }
        ]
    },
    {
        "category": "Content Writing",
        "tools": [
            {
                "id": "writing-1",
                "name": "Jasper AI (Limited Free)",
                "description": "AI writing assistant with templates and limited free access",
                "url": "https://www.jasper.ai",
                "category": "Content Writing",
                "capabilities": [
                    "Blog post generation",
                    "Marketing copy",
                    "Social media content"
                ],
                "limitations": "Very limited free functionality",
                "logo": "pencil"
            },
            {
                "id": "writing-2",
                "name": "Copy.ai",
                "description": "AI copywriting tool with free plan for basic content generation",
                "url": "https://www.copy.ai",
                "category": "Content Writing",
                "capabilities": [
                    "Marketing copy",
                    "Content ideas",
                    "Blog outlines"
                ],
                "limitations": "Limited credits in free tier",
                "logo": "file-text"
            },
            {
                "id": "writing-3",
                "name": "Anyword",
                "description": "AI copywriting assistant with free trial",
                "url": "https://anyword.com",
                "category": "Content Writing",
                "capabilities": [
                    "Sales copy",
                    "Email content",
                    "Ad creation"
                ],
                "limitations": "Limited functionality in free tier",
                "logo": "pen"
            },
            {
                "id": "writing-4",
                "name": "Rytr",
                "description": "AI writing assistant with generous free tier",
                "url": "https://rytr.me",
                "category": "Content Writing",
                "capabilities": [
                    "Blog content",
                    "Email templates",
                    "Social media posts"
                ],
                "limitations": "Usage limits in free tier",
                "logo": "pencil-square"
            },
            {
                "id": "writing-5",
                "name": "QuillBot",
                "description": "AI-powered paraphrasing and summarization tool with free tier",
                "url": "https://quillbot.com",
                "category": "Content Writing",
                "capabilities": [
                    "Paraphrasing",
                    "Summarization",
                    "Grammar checking"
                ],
                "limitations": "Character limits in free version",
                "logo": "arrow-repeat"
            },
            {
                "id": "writing-6",
                "name": "WordAI",
                "description": "AI content rewriter with limited free access",
                "url": "https://wordai.com",
                "category": "Content Writing",
                "capabilities": [
                    "Article rewriting",
                    "Content spinning",
                    "Readability improvements"
                ],
                "limitations": "Minimal free functionality",
                "logo": "file-word"
            }
        ]
    },
    {
        "category": "Design Tools",
        "tools": [
            {
                "id": "design-1",
                "name": "Canva",
                "description": "Design platform with AI features and generous free tier",
                "url": "https://www.canva.com",
                "category": "Design Tools",
                "capabilities": [
                    "AI image generation",
                    "Magic edit",
                    "Text to image"
                ],
                "limitations": "Some advanced features require premium",
                "logo": "palette"
            },
            {
                "id": "design-2",
                "name": "Remove.bg",
                "description": "AI tool to automatically remove image backgrounds",
                "url": "https://www.remove.bg",
                "category": "Design Tools",
                "capabilities": [
                    "Background removal",
                    "One-click processing",
                    "API access"
                ],
                "limitations": "Limited free uses per month",
                "logo": "scissors"
            },
            {
                "id": "design-3",
                "name": "Photopea",
                "description": "Free online photo editor with AI features",
                "url": "https://www.photopea.com",
                "category": "Design Tools",
                "capabilities": [
                    "Photoshop-like interface",
                    "Layer management",
                    "AI-powered tools"
                ],
                "limitations": "Ad-supported",
                "logo": "image"
            },
            {
                "id": "design-4",
                "name": "Vectorizer.ai",
                "description": "AI tool to convert raster images to vector graphics",
                "url": "https://vectorizer.ai",
                "category": "Design Tools",
                "capabilities": [
                    "Image to SVG conversion",
                    "Clean vector output",
                    "High accuracy"
                ],
                "limitations": "Limited free conversions",
                "logo": "bezier2"
            },
            {
                "id": "design-5",
                "name": "Patterned AI",
                "description": "AI-generated seamless pattern creator",
                "url": "https://www.patterned.ai",
                "category": "Design Tools",
                "capabilities": [
                    "Custom pattern generation",
                    "Style control",
                    "Seamless tiling"
                ],
                "limitations": "Limited options in free version",
                "logo": "grid-3x3"
            },
            {
                "id": "design-6",
                "name": "Logo.com",
                "description": "AI-powered logo generation tool with free samples",
                "url": "https://logo.com",
                "category": "Design Tools",
                "capabilities": [
                    "Logo generation",
                    "Brand identity options",
                    "Customization tools"
                ],
                "limitations": "Payment required for high-res download",
                "logo": "vector-pen"
            }
        ]
    },
    {
        "category": "Education Tools",
        "tools": [
            {
                "id": "edu-1",
                "name": "Quizlet",
                "description": "Flashcard platform with AI study tools and free tier",
                "url": "https://quizlet.com",
                "category": "Education Tools",
                "capabilities": [
                    "AI-powered explanations",
                    "Study sets generation",
                    "Learning analytics"
                ],
                "limitations": "Advanced features require subscription",
                "logo": "card-text"
            },
            {
                "id": "edu-2",
                "name": "Coursera",
                "description": "Online learning platform with free AI courses and audit options",
                "url": "https://www.coursera.org",
                "category": "Education Tools",
                "capabilities": [
                    "AI course content",
                    "Free audit option",
                    "University partnerships"
                ],
                "limitations": "Certificates require payment",
                "logo": "mortarboard"
            },
            {
                "id": "edu-3",
                "name": "Khan Academy",
                "description": "Free education platform with AI-powered Khanmigo learning assistant",
                "url": "https://www.khanacademy.org",
                "category": "Education Tools",
                "capabilities": [
                    "Personalized learning",
                    "AI tutor access",
                    "Comprehensive curriculum"
                ],
                "limitations": "Advanced AI features may require subscription",
                "logo": "book"
            },
            {
                "id": "edu-4",
                "name": "Duolingo",
                "description": "Language learning app with AI features and free tier",
                "url": "https://www.duolingo.com",
                "category": "Education Tools",
                "capabilities": [
                    "Adaptive learning",
                    "Speech recognition",
                    "Personalized lessons"
                ],
                "limitations": "Ad-supported in free version",
                "logo": "translate"
            },
            {
                "id": "edu-5",
                "name": "Socratic by Google",
                "description": "AI learning app that helps with homework questions",
                "url": "https://socratic.org",
                "category": "Education Tools",
                "capabilities": [
                    "Homework help",
                    "Explanation generation",
                    "Multi-subject support"
                ],
                "limitations": "May not cover advanced topics",
                "logo": "question-circle"
            },
            {
                "id": "edu-6",
                "name": "Miro AI",
                "description": "Collaborative whiteboard platform with AI features and free plan",
                "url": "https://miro.com/ai",
                "category": "Education Tools",
                "capabilities": [
                    "AI-powered diagramming",
                    "Content generation",
                    "Visual collaboration"
                ],
                "limitations": "Limited boards in free plan",
                "logo": "easel2"
            }
        ]
    },
    {
        "category": "Business Tools",
        "tools": [
            {
                "id": "biz-1",
                "name": "HubSpot (Free CRM)",
                "description": "CRM platform with AI features and comprehensive free tier",
                "url": "https://www.hubspot.com/products/free",
                "category": "Business Tools",
                "capabilities": [
                    "Customer data management",
                    "Email marketing tools",
                    "AI content suggestions"
                ],
                "limitations": "Advanced features require paid plans",
                "logo": "building"
            },
            {
                "id": "biz-2",
                "name": "Zapier",
                "description": "Automation tool with AI capabilities and free tier",
                "url": "https://zapier.com",
                "category": "Business Tools",
                "capabilities": [
                    "Workflow automation",
                    "AI-powered suggestions",
                    "App integrations"
                ],
                "limitations": "Limited tasks per month in free plan",
                "logo": "lightning-charge"
            },
            {
                "id": "biz-3",
                "name": "Trello",
                "description": "Project management tool with AI features and free tier",
                "url": "https://trello.com",
                "category": "Business Tools",
                "capabilities": [
                    "AI-powered automation",
                    "Card generation",
                    "Task management"
                ],
                "limitations": "Limited boards in free version",
                "logo": "kanban"
            },
            {
                "id": "biz-4",
                "name": "Notion AI (Limited Free)",
                "description": "Workspace with AI writing and organization features",
                "url": "https://www.notion.so/product/ai",
                "category": "Business Tools",
                "capabilities": [
                    "AI writing assistance",
                    "Content summarization",
                    "Task organization"
                ],
                "limitations": "Limited AI features in free tier",
                "logo": "layout-text-window"
            },
            {
                "id": "biz-5",
                "name": "Hunter.io",
                "description": "Email finding and verification tool with free tier",
                "url": "https://hunter.io",
                "category": "Business Tools",
                "capabilities": [
                    "Email verification",
                    "Domain search",
                    "Email finder"
                ],
                "limitations": "Limited searches per month in free plan",
                "logo": "envelope"
            },
            {
                "id": "biz-6",
                "name": "Calendly",
                "description": "Scheduling tool with AI features and free tier",
                "url": "https://calendly.com",
                "category": "Business Tools",
                "capabilities": [
                    "Smart scheduling",
                    "Automatic time zone detection",
                    "Calendar integration"
                ],
                "limitations": "Limited event types in free tier",
                "logo": "calendar-date"
            }
        ]
    }
]
