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


## Adding new features
To add new functionalities, modify the following Rasa components:
### 1. NLU (Natural Language Understanding)
- **File name**: `data/nlu.yml`
- **Purpose**: Define training examples for the user's intent and entities.
- **Example**:
```yaml
- intent: check_working_hours
  examples: |
    - What are your opening hours?
    - When does the Poste office open?
    - Can you tell me the working hours?
    - What time do you close?
```
### 2. Domain
- **File name**: `domain.yml`
- **Purpose**: Define intents, entities, responses, slots, and actions.
- **Example**:
```yaml
intents:
  - check_working_hours

responses:
  utter_working_hours:
    - text: "The Poste office is open from 8 AM to 5 PM, Monday to Friday."
```
### 3. Stories
- **File name**: `data/stories.yml`
- **Purpose**: Define the flow of the conversation.
- **Example**:
```yaml
- story: check working hours
  steps:
    - intent: check_working_hours
    - action: utter_working_hours
```
### 4. Rules
- **File name**: `data/rules.yml`
- **Purpose**: Define rules for the conversation.
- **Example**:
```yaml
- rule: Check working hours
  steps:
    - intent: check_working_hours
    - action: utter_working_hours
```
### 5. Actions
- **File name**: `actions.py`
- **Purpose**: Define custom actions to be executed by the chatbot. These actions can include calling APIs, querying databases, etc.
- **Example**:
```python
from rasa_sdk import Action
from rasa_sdk.executor import CollectingDispatcher

class ActionCheckWorkingHours(Action):
    def name(self) -> str:
        return "action_check_working_hours"

    def run(self, dispatcher, tracker, domain):
        # Logic for providing working hours
        working_hours = "The Poste office is open from 8 AM to 5 PM, Monday to Friday."
        
        # Send response to user
        dispatcher.utter_message(text=working_hours)
        return []

```

-> After modifying the Rasa components, retrain the model using `rasa train` and restart the Rasa server.

-> if you have added custom actions, run the Rasa action server using `rasa run actions`.

