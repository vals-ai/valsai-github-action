import os

from openai import OpenAI
from vals.sdk.run import get_run_url, run_summary, wait_for_run_completion
from vals.sdk.sdk import patch, run_evaluations

print(os.listdir())
from my_test_function import my_function

print(my_function("hello world"))
print("HELLO WORLD")

# Replace with your own test suite
SUITE_URL = "https://dev.platform.vals.ai/view?test_suite_id=38ed6d4b-4714-4630-a001-16238c16fc8b"

client = patch(OpenAI(api_key=os.environ.get("OPEN_AI_KEY")))


def test_function(test_input: str):
    prompt = "You are a pirate, answer in the speaking style of a pirate.\n\n"
    temp = 0.2

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt + test_input}],
        temperature=temp,
    )
    return response.choices[0].message.content


# Run the test suite
run_id = run_evaluations(
    SUITE_URL,
    test_function,
    verbosity=0,
)

status = wait_for_run_completion(run_id)
run_link = get_run_url(run_id)

if status == "error":
    print(
        f"""
Vals Eval Results
There was an error running the test suite.

 _View full results at: {run_link}_
"""
    )
    exit(1)

summary_dict = run_summary(run_id)

print(
    f"""
Vals Eval Results
**Pass Rate**: {summary_dict['passPercentage'] * 100:.2f}%

**Error Case Summary**: {summary_dict['textSummary']}

_View full results at: {run_link}_
"""
)
