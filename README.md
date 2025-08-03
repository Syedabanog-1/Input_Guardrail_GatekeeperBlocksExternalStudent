Objective:
**********
This project demonstrates how to build a gatekeeping system using the OpenAI Agent SDK with @input_guardrail. The goal is to simulate a virtual school gatekeeper that only allows students from "Little Angel Public School" to enter, and blocks others gracefully.

Workflow:
*********

1- Define Output Model
A StudentCheckResult Pydantic model defines the expected output from the gatekeeper agent — a message and a boolean indicating whether the student is from another school.

2- Create Gatekeeper Agent
The gate_keeper agent evaluates the student's input (school name) and decides access based on it. If the school doesn't match, it sets isOtherSchool = True.

3- Input Guardrail Setup
The @input_guardrail decorator wraps the gate_keeper_guardrail function to act as a filter before the main agent processes any input. If the student is from another school, it triggers a GuardrailTripwire.

4- Main Agent – Student
The student_agent tries to enter the school. Its input is first passed through the gatekeeper guardrail.

5- Execution Logic
The main() function runs the logic. If the guardrail is triggered (i.e., the student is from another school), access is denied. Otherwise, the student is allowed in.



https://github.com/user-attachments/assets/49a3b8f8-63ff-4872-8175-a76f4783b7e5

<img width="1612" height="906" alt="ExternalStudent-Generation" src="https://github.com/user-attachments/assets/cb72cbc2-b1f5-43d2-ab2b-7083fbdd3d2e" />
<img width="1610" height="905" alt="gatekeeperblock-external-Generations" src="https://github.com/user-attachments/assets/594a4036-da0d-4e2a-be93-d952888ddbd4" />
<img width="1611" height="907" alt="gatekeeperblock-external-Triggered-True" src="https://github.com/user-attachments/assets/7c9ba9c5-03c2-495e-a28d-09c77a617fa4" />
<img width="1608" height="905" alt="gatekeeperblock-external-Triggered-True-Error" src="https://github.com/user-attachments/assets/c7718895-1195-4c5b-8035-552c28e38a37" />















