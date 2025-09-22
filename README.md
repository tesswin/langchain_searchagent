## Creating AI Agent using LangChain with ReAct Architecture 

Components: 

- create_react_agent --> produce a runnable object 
- AgentExecutor --> it give the actual call (its a for loop) 
- llm --> the reasoning engine 

> I am using gemma3:1b and gpt-oss:latest from ollama as my llm 
> react prompt --> 
> coding example: react_prompt = hub.pull("hwchase17/react")
> its a prompt template object 
> agent using create_react_agent 
> This will just return a runnable object 
> agent executor will be the orchestrator of the prompt, i.e., it will decide the next action like call a tool, or do another prompt to another llm, etc. 




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
3. ollama pull gpt-oss:latest
4. ollama pull gemma3:1b 