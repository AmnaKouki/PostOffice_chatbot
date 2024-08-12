# Chatbot - Tunisian Post

This chatbot 
is designed to assist users with their queries related to the Tunisian Post. It can provide information on 
services offered, tracking packages, and more.

## Installation

### Prerequisites
- Node.js and npm
- Python 3.10+
- Angular CLI
- Rasa CLI

### Setup

1. Clone the repository
2. Install dependencies using `npm i` (Angular) and `pip install -r requirements.txt` (Rasa)
3. Run the Angular application using `ng serve`
4. Run the Rasa application using `rasa run --enable-api --cors="*"`
5. Run the Rasa action server: `rasa run actions`

## How to train

1. Run `rasa train` to train the model
2. Run `rasa run --enable-api --cors="*"` to run the Rasa

## Integrate the Chatbot in a Web Page

1. In "iframe" folder, you will find an example on how to integrate this chatbot into your web page.
2. Simple, add this script at the end of your body tag.
```
<script scr="chatbot.js" chatbot-url="http://example.com"></script>
```

3. Replace "http://example.com" with the URL of your chatbot.