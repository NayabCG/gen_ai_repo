Test Case 1: HR Agent

USER QUESTION

How many casual leaves are allowed per year?

AGENT DELEGATION

Supervisor → HR Agent → FAISS Vector Database
AI Response

Employees are eligible for 12 casual leaves per calendar year. All casual leave requests require manager approval.

Source: hr_policy.txt


Test Case 2: Finance Agent

USER QUESTION

Show my salary details for employee E101.

AGENT DELEGATION

Supervisor → Finance Agent → SQLite Database
AI Response

Employee ID: E101

Name: Ravi

Department: IT

Monthly Salary: ₹50,000


Test Case 3: IT Support Agent

USER QUESTION

I forgot my company password. How can I reset it?

AGENT DELEGATION

Supervisor → IT Support Agent → Python Tool
AI Response
1. Open the company login portal.
2. Select Forgot Password.
3. Verify your identity.
4. Create a new password.


Test Case 4: External API

USER QUESTION

What is the current weather in Hyderabad?

AGENT DELEGATION

Supervisor → General Agent → Open-Meteo API
AI Response

Current weather information is retrieved from the external API, including temperature, humidity and wind speed.


Test Case 5: Multiple Agents

USER QUESTION

Show employee E101's salary and tell me the casual leave policy.

AGENT DELEGATION

Supervisor → Finance Agent + HR Agent
AI Response

Employee Information
- Employee: Ravi
- Monthly Salary: ₹50,000
HR Policy
- Casual Leave: 12 days per year.
- Manager approval is required.


Test Case 6: Conversational Memory

FIRST QUESTION

My employee ID is E101.

FOLLOW-UP QUESTION

What is my salary?

EXPECTED BEHAVIOUR

The Supervisor uses the previous conversation context to identify E101 and delegates the salary request to the Finance Agent.