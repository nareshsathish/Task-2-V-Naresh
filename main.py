questions = open("logic_questions.txt", "r").read()
prompt = f"""
You are a Chain-of-Thought Logic Engine.
Instructions:
1. Read each problem carefully.
2. Solve step by step.
3. Explain reasoning.
4. Perform self-correction.
5. Then provide final answer.
Problems:
{questions}
"""
with open("output.txt", "w") as file:
    file.write(prompt)
print("Project 2 prompt generated successfully!")