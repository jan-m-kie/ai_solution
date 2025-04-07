from crewai import Crew, Agent, Task

def main():
    dev_agent = Agent(name="DevAgent", role="code-generator")
    task = Task(agent=dev_agent, description="Generate a Python function to sort a list of numbers.")
    crew = Crew(tasks=[task])
    results = crew.run()
    print("Results:", results)

if __name__ == "__main__":
    main()