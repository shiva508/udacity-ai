
if __package__:
    from .workflow_agents import DataFetchingAgent, DataProcessingAgent
else:
    from workflow_agents import DataFetchingAgent, DataProcessingAgent

def run_user_data_workflow(user_id_to_process):
    """
    This function implements the agentic workflow.
    """
    print(f"\n--- Starting User Data Workflow for User ID: {user_id_to_process} ---")
    # === 2. Agent Instantiation Logic ===
    # Create specific instances (objects) of agent classes and configure them.
    # Each agent can be customized for its specific role or task.

    data_fetching_agent = DataFetchingAgent(name="DataFetchingAgent", data_source="MainUserDatabase")
    data_processing_agent = DataProcessingAgent(name="DataProcessingAgent", fields_to_extract=["name", "occupation", "user_id"])

    print("--- Agents Instantiated ---")

    # === 3. Workflow Implementation Logic ===
    # Define the sequence of tasks and how data is passed between agents.

    # Step 1: Fetch user data
    print("\nStep 1: Fetching Data...")
    fetched_user_data = data_fetching_agent.execute(user_id=user_id_to_process)
    print(f"Fetcher Output: {fetched_user_data}")
    if 'error' in fetched_user_data and fetched_user_data['error']:
        print(f"Workflow stopped due to error in fetching: {fetched_user_data['error']}")
        return {"status": "Error", "details": fetched_user_data['error']}
    # Step 2: Process fetched data
    print("\nStep 2: Processing Data...")
    processed_data_report = data_processing_agent.execute(fetched_data=fetched_user_data)
    print(f"Processor Output: {processed_data_report}")

    print("--- Workflow Completed ---")
    return {"status": "Success", "data": processed_data_report}

if __name__ == '__main__':
    # Example 1: Successful run
    result1 = run_user_data_workflow("123")
    print(f"\nFinal Result for User 123: {result1}\n")

    # Example 2: User not found
    result2 = run_user_data_workflow("456")
    print(f"Final Result for User 456: {result2}")
