## Creating AI Agent using LangChain with ReAct Architecture 

Components: 

- create_react_agent --> produce a runnable object 
- AgentExecutor --> it give the actual call (its a for loop)

The agent will have the following tools: 
- Tavily search tool --> to search the internet 










----------------Project Initiatialization-------------------
1. git init 
2. uv init 
3. uv add langchain langchain-openai langchain-ollama langchain-tavily
4. uv add python-dotenv black isort
5. create .env file 
6. create .gitignore file 



Other requirements 
1. openai login 
2. tavily login 