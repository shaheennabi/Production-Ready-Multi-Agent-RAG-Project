# 🌺 🌸 🌿 Production-Ready TripPlanner Multi-AI Agent Project 🍀 🌱 🪴

## System Design or Project Pipeline
### Main Pipeline

![TripPlanner](https://github.com/user-attachments/assets/45f1226e-2e3c-4ae7-999f-9ff0db143bc7)

### Let's Start with LLM OpenAI: (GPT-3.5 Turbo):

![Screenshot 2024-12-22 014852](https://github.com/user-attachments/assets/c33b9de0-e125-4ee7-8fff-67dc952dfe0f)

- In this example, I am loading the **GPT-3.5 Turbo** model from **taskflowai.OpenaiModels**.  
- This model is efficient, cost-effective, and performs exceptionally well for most tasks.  
- Make sure to load the OpenAI API key properly.  
- It is recommended to store the API key securely using a `.env` file or a similar approach.  

### Now let's task about the Agents:
Web Research Agent: 

  ![Screenshot 2024-12-22 014625](https://github.com/user-attachments/assets/83e0f923-6e4e-4763-b11d-09980ea09458)

- Here, I define the **Web Research Agent**, which is responsible for conducting web-based research and retrieving relevant information.  
- I assign the role of "Web Research Agent" to the agent, ensuring it focuses on researching destinations and finding related images.  
- The **goal** is set to perform thorough and comprehensive research with a visual focus.  
- I specify **attributes** like diligence, thoroughness, and visual-focus to guide the agent's behavior during tasks.  
- I load the OpenAI model using `LoadModel.load_openai_model()` to empower the agent with natural language processing capabilities.  
- I include tools like:
  - **SerperSearch**: For detailed web searches.  
  - **WikiArticles**: To fetch related articles for context.  
  - **WikiImages**: To search and retrieve relevant images.
 
Travel Agent:

![Screenshot 2024-12-22 014556](https://github.com/user-attachments/assets/2d985f64-b996-45a1-9114-534d8969f110)

- Here, I define the **Travel Agent**, which is designed to assist travelers with their queries, focusing on searching for flights and retrieving weather data.  
- The **role** assigned to the agent is "Travel Agent," ensuring its primary function is to help travelers.  
- The **goal** is set to assist travelers by providing relevant information such as flight details and weather conditions.  
- I specify **attributes** like friendliness, hard work, and attention to detail to ensure the agent delivers thorough and useful responses.  
- I load the OpenAI model using `LoadModel.load_openai_model()` to provide natural language processing capabilities.  
- I include tools like:
  - **SearchFlights**: A tool for searching and retrieving flight information using the Amadeus API.  
  - **GetWeatherData**: A tool for fetching real-time weather data from weather.com API.  

Reporter Agent:  

![Screenshot 2024-12-22 014515](https://github.com/user-attachments/assets/6928996a-69c2-49f2-af66-911be403e60f)

- Here, I define the **Travel Report Agent**, which aggregates data from various agents like the Web Search Agent and Travel Agent to generate comprehensive and summarized travel reports.  
- The **role** assigned to the agent is "Travel Report Agent," ensuring its focus on collecting and synthesizing travel-related information.  
- The **goal** is to write detailed, visual-oriented, and comprehensive travel reports based on inputs from other agents, covering destination details, dates, weather reports, flight information, and events at the location.  
- I specify **attributes** like friendliness, hard work, visual focus, and attention to detail to ensure the agent delivers well-structured, insightful, and informative reports.  
- I load the OpenAI model using `LoadModel.load_openai_model()` to provide natural language processing and text generation capabilities.  
- The agent relies on tools and data from other agents, such as:
  - **Web Search Agent**: Provides destination details and event-related information.  
  - **Travel Agent**: Supplies weather reports and flight information.  

### Now let's talk about Tools

Wiki Image Search Tool:

![Screenshot 2024-12-22 021339](https://github.com/user-attachments/assets/d3e1323f-fb04-47a2-a588-bb4a2ac7f589)

- Here, I define the **WikiImages tool**, which is responsible for searching images from Wikipedia using **TaskflowAI's WikipediaTools**.  
- The **goal** of the tool is to fetch relevant images based on specific queries or topics.  
- It leverages **WikipediaTools** from TaskflowAI to access and retrieve image data from Wikipedia.  

Wiki Article Search Tool: 

![Screenshot 2024-12-22 021756](https://github.com/user-attachments/assets/e36413f9-799f-41e0-b513-09fec0a69f9a)

- Here, I define the **WikiArticles tool**, which is responsible for fetching articles from Wikipedia using **TaskflowAI's WikipediaTools**.  
- The **goal** of the tool is to retrieve relevant articles based on specific queries or topics.  
- It utilizes **WikipediaTools** from TaskflowAI to access and fetch article data from Wikipedia.  

Serper Search Tool:

![Screenshot 2024-12-22 021920](https://github.com/user-attachments/assets/2152df64-700d-428f-a86e-597091f7af79)

- Here, I define the **SerperSearch tool**, which is responsible for performing web searches using **TaskflowAI's WebTools**.  
- The **goal** of the tool is to retrieve search results from the web based on specific queries or topics.  
- It leverages **WebTools** from TaskflowAI to perform search operations using the SerperSearch API.  

Weather Fetching Tool:

![Screenshot 2024-12-22 022133](https://github.com/user-attachments/assets/f573e7f3-abf5-4ace-9c81-c0d0abb28be4)

- Here, I define the **GetWeatherData tool**, which is responsible for fetching weather data using **TaskflowAI's WebTools** and the **Weather.com API**.  
- The **goal** of the tool is to retrieve weather-related information based on location or other relevant queries.  
- It utilizes **WebTools** from TaskflowAI to interact with the Weather.com API and fetch weather data.  

Search Fligts Tool: 

![Screenshot 2024-12-22 022445](https://github.com/user-attachments/assets/39e79100-0d2d-46db-a877-935fc0ce67f3)

- Here, I define the **SearchFlights tool**, which is responsible for searching flights using **TaskflowAI's AmadeusTools** and the **Amadeus API**.  
- The **goal** of the tool is to retrieve flight information based on specific queries such as origin, destination, dates, and other relevant parameters.  
- It leverages **AmadeusTools** from TaskflowAI to interact with the Amadeus API for flight searches.  

### Ok, so now let's talk the app.py where everything is bought together (see how tasks are defined, to later engage with UI)







### Deployment Pipeline

![Deployment Pipeline TripPlanner ](https://github.com/user-attachments/assets/2aa5d232-3766-4ac1-b48a-eb055ac1f7e7)


## Guide for Developers 🌿🎇✨💚🎆🌱🎇✨💚🎆 

### Project tree structure

```bash
├── .github/workflows/
│   └── deploy.yml
├── deployment/
│   └── app.py
├── docs/
│   ├── Agentic RAG Pipeline.md
│   └── Types of Agentic RAG.md
├── flowcharts/
│   └── project_pipeline.jpg
├── log/
│   └── timestamp(log)
├── notebooks/
│   └── TripPlanner_Multi_AI_Agent_Experimental.ipynb  
├── src/agentic/
│   ├── agents/
│   │   ├── reporter_agent.py
│   │   ├── travel_agent.py
│   │   └── web_research_agent.py
│   ├── exception/
│   │   └── __init__.py
│   ├── logger/
│   │   └── __init__.py
│   ├── tools/
│   │   ├── get_weather_data.py
│   │   ├── search_articles.py
│   │   ├── search_flights.py
│   │   ├── search_images.py
│   │   └── serper_search.py
│   └── utils/
│       ├── __init__.py
│       └── main_utils.py
├── .gitignore
├── demo.py
├── LICENSE
├── README.md
├── requirements.txt
├── scripts.sh
├── setup.py
└── template.py
```


## 📜 License
This project is licensed under the **MIT License**.  
You are free to use, modify, and share this project, as long as proper credit is given to the original contributors.  
For more details, check the [LICENSE](LICENSE) file. 🏛️

