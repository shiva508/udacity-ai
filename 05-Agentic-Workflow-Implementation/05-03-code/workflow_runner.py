from workflow_agents import ResearchAgent, SummarizerAgent, FactCheckerAgent


def run_agentic_workflow():
    research_agent = ResearchAgent(name="ResearchAgent")
    summarizer_agent = SummarizerAgent(name="SummarizerAgent")
    fact_checker_agent = FactCheckerAgent(name="FactCheckerAgent")

    print("\n🚀 Starting 'Information Processing' workflow\n")
    # Run the agentic workflow
    query = "Agentic workflows in AI systems"

    research_results = research_agent.run(query)
    summary = summarizer_agent.run(research_results)
    fact_check_results = fact_checker_agent.run(summary)

    print(f"\n✅ Workflow completed successfully!")
    print(f"Final Results:")
    print(f" - Research: {research_results}")
    print(f" - Summary: {summary}")
    print(f" - Fact Check: {fact_check_results}")

if __name__ == '__main__':
    run_agentic_workflow()