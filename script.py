import os
import sys

from openai import OpenAI
from vals.sdk.run import get_run_url, run_summary, wait_for_run_completion
from vals.sdk.sdk import patch, run_evaluations

# This is necessary so that the current directory (with user provided script) appears
sys.path.append(os.getcwd())
from vals_entry import vals_entry_function

# Read the suite url from
suite_url = sys.argv[1]

# Run the test suite
run_id = run_evaluations(
    suite_url,
    vals_entry_function,
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
