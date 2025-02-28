import asyncio
import time
from restack_ai import Restack
from pydantic import BaseModel

class InputParams(BaseModel):
    user_content: str
    system_content: str

async def main():
    client = Restack()

    workflow_id = f"{int(time.time() * 1000)}-ChatbotWorkflow"
    runId = await client.schedule_workflow(
        workflow_name="ChatbotWorkflow",
        workflow_id=workflow_id,
        input=InputParams(user_content="Hey, what is restack?", system_content="You are a helpful assistant")
    )

    await client.get_workflow_result(
        workflow_id=workflow_id,
        run_id=runId
    )

    exit(0)

def run_schedule_workflow():
    asyncio.run(main())

if __name__ == "__main__":
    run_schedule_workflow()