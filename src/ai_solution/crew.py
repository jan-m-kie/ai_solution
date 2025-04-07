from crewai import Crew, Agent, Task

from ai_solution.config import get_llm, get_memory

def build_crew():
    llm = get_llm()
    memory = get_memory()

    dev_agent = Agent(name="DevAgent", role="code-generator", llm=llm, memory=memory)
    test_agent = Agent(name="TestAgent", role="quality-assurance", llm=llm, memory=memory)
    sec_agent = Agent(name="SecAgent", role="security-auditor", llm=llm, memory=memory)
    devops_agent = Agent(name="DevOpsAgent", role="infra-automation", llm=llm, memory=memory)

    tasks = [
        Task(agent=dev_agent, description="Generate core app code."),
        Task(agent=test_agent, description="Write tests for the app."),
        Task(agent=sec_agent, description="Audit code for security flaws."),
        Task(agent=devops_agent, description="Generate Kubernetes deployment scripts.")
    ]

    return Crew(tasks=tasks)