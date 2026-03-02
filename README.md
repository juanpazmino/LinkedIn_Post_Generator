# LinkedIn Post Generator

A CLI tool that takes a prompt from you and returns a ready-to-publish LinkedIn post — with a title, body, hashtags, and category.

It uses Azure OpenAI (GPT-4.1 nano) under the hood and returns structured output via Pydantic, so the response is always consistent.

## How it works

Run the script, type what you want to post about, and get back a formatted post. You can keep generating posts in the same session or type `/exit` to quit.

```
$ python main.py

Welcome to the LinkedIn Post Generator!

Enter your prompt (or type '/exit' to quit): I just got promoted to senior engineer after 3 years at my company

Title: Three Years Later — What I Learned on the Way to Senior Engineer
Content: ...
Hashtags: #SoftwareEngineering, #CareerGrowth, #SeniorEngineer
Category: Career
```

## Setup

1. Clone the repo and install dependencies:

```bash
pip install -r requirements.txt
```

2. Create a `.env` file with your Azure OpenAI credentials:

```
AZURE_OPENAI_API_KEY=your_key
AZURE_OPENAI_ENDPOINT=your_endpoint
OPENAI_API_VERSION=your_api_version
```

3. Run:

```bash
python main.py
```

## Project structure

```
.
├── main.py               # Entry point
├── core/
│   ├── api_client.py     # Azure OpenAI client and API calls
│   └── chatbot.py        # Chatbot logic
├── models/
│   └── linkedin_post.py  # Pydantic model for structured output
└── requirements.txt
```
