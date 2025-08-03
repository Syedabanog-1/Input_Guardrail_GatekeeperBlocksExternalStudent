import rich
import asyncio
from connection import config
from pydantic import BaseModel
from agents import (
    Agent,
    Runner,
    input_guardrail,
    trace,
    GuardrailFunctionOutput,
    InputGuardrailTripwireTriggered,
)

# Output model that the gatekeeper will return
class StudentCheck(BaseModel):
    message: str
    isOtherSchool: bool

# Gate Keeper Agent who checks students
gate_keeper = Agent(
    name="School Gate Keeper",
    instructions="""
        Your task is to allow only students from 'Little Angel Public School'.
        If a student is from another school, gracefully stop them and set isOtherSchool = True.
        Otherwise, welcome them and set isOtherSchool = False.
    """,
    output_type=StudentCheck
)

# Input guardrail using the gate_keeper agent
@input_guardrail
async def gate_keeper_guardrail(ctx, agent, input):
    result = await Runner.run(gate_keeper, input, run_config=config)
    rich.print(result.final_output)

    return GuardrailFunctionOutput(
        output_info=result.final_output.message,
        tripwire_triggered=result.final_output.isOtherSchool
    )

# Main agent representing the student
student_agent = Agent(
    name="Student",
    instructions="You are trying to enter the school.",
    input_guardrails=[gate_keeper_guardrail]
)

# Execution logic
async def main():
    with trace("GatekeeperBlockExteriorStudent"):
        try:
            # Change this input to test different schools
            result = await Runner.run(student_agent, "I am from City Public School.", run_config=config)
            print("Student is allowed to enter.")
        except InputGuardrailTripwireTriggered:
            print("Access Denied: You are not from this school.")

# Run the main logic
if __name__ == "__main__":
    asyncio.run(main())
