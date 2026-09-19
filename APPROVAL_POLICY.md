+++
max_risk_score = 1
minimum_confidence = "high"
required_checks = ["approval-policy-fixture"]
human_review_paths = ["restricted/*"]
+++
# Test repository approval policy

## Documentation only
Only non-executable prose may change. Explain why it has no behavioral impact.

## Complete inspection
Inspect every changed line and establish that there are no unresolved findings or required human decisions.
