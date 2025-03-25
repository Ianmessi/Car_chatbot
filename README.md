# Car Troubleshooting Chatbot

A web-based chatbot that helps users diagnose common car problems. The chatbot uses natural language processing to understand various ways users might describe their car issues and provides relevant causes and solutions.

## Features
- Natural language understanding
- Comprehensive database of car problems
- Modern, responsive UI
- Real-time responses
- Mobile-friendly design

## Technologies Used
- Python
- Flask
- FuzzyWuzzy for natural language matching
- HTML/CSS/JavaScript
- Font Awesome icons

## Local Development
1. Clone the repository
2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python app.py
   ```
5. Visit `http://localhost:5000` in your browser

## Deployment
This project is configured for deployment on Render.com. The deployment process is automated through the Render dashboard. 