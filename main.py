from dotenv import load_dotenv
load_dotenv()

from langchain import hub
from langchain.agents import AgentExecutor
from langchain.agents.react.agent import create_react_agent

from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

from langchain_tavily import TavilySearch

tools = [TavilySearch()]

llm = ChatOllama(model="gemma3:1b")
# llm = ChatOllama(model="gpt-oss:latest")

react_prompt = hub.pull("hwchase17/react")

agent = create_react_agent(
    llm= llm, 
    tools=tools, 
    prompt=react_prompt
)

agent_executor = AgentExecutor(agent=agent, 
                               tools=tools, 
                               verbose=True, 
                               handle_parsing_errors=True, 
                               return_intermediate_steps=True)

chain = agent_executor


def main():
    result = chain.invoke(input =
                          {"input": "search for 3 job postings for an ai engineer using langchain in the United Kingdom on linkedin and list their details"})
    print(result)


if __name__ == "__main__":
    main()
