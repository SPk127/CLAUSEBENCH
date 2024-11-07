## Instruction:

### Task Description:
You are assigned to determine and interpret the presence and meaning of a specific licensing term within a portion of an open-source software license. You will be provided with the whole license text, along with some relevent license information. Your goal is to analyze these excerpts and identify whether they address the term and, if so, the term's implications for users according to predefined categories.

To classify the term's meaning, you may only use the following Simplified Markers: CAN, CANNOT, MUST, MUST NOT, OPTIONAL, and NOT SPECIFIED. Your analysis should strictly adhere to this set of markers without any additional terminology to ensure consistency. If the meaning is ambiguous, or if the term is absent, you must still choose one of the above markers.

### Simplified Markers for License Terms

#### Empowering Clauses: For terms that grant permissions (e.g., Distribute, Modify, Commercial Use, Relicense, Hold Liable, Use Patent Claims, Sublicense, Use Trademark), use the following markers:
- CAN: If the license explicitly permits the action.
- MUST NOT: If the license explicitly prohibits the action.

#### Responsibility Clauses: For terms that impose obligations (e.g., Include Copyright, Disclose Source, Give Credit, Rename, Contact Author), use these markers:
- MUST: If the license mandates the action or condition.
- OPTIONAL: If the license suggests the action but does not require it.

#### Ambiguous Cases: If the term is mentioned but lacks clear implications regarding permissions or obligations, or if it is entirely absent, use:
- NOT SPECIFIED: Indicating that the license does not explicitly address the term or its implications.

## Input:
The following structured information will be provided to help determine the status of the term in the license:

- License Information:
  - License Name: {case['license_name']}.
  - License Category: {case['license_info']['category']}.

- Specific Term to Evaluate:
  - Term Name: {case['license_terms']}.
  - Term Description: {case['terms_description']}.

- License Content for Analysis:
  - License Text: {case['license_body']}.


## Output:

### Expected Output Format:
Generate a JSON object with the following keys:
- marker: One of the following values: "CAN", "MUST", "MUST NOT", "OPTIONAL", or "NOT SPECIFIED".


### Example Output:
```json
{{
  "marker": "CAN"
}}
```

### Notes:
- Ensure that the marker strictly adheres to one of the specified values.
- Answer only the terms given in the Input.
- NO explanation needed.