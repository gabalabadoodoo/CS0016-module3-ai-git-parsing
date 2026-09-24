# AI Usage and Validation Log

Student name: Gab Claro
Section: TS31
AI tool used: Codex

## Pre-implementation predictions

### XML

- Default namespace: `urn:ietf:params:xml:ns:netconf:base:1.0`
- Expected `default_operation`: `merge`
- Expected `test_option`: `test-then-set`

### JSON

- Expected `site`: `FEU-Tech-Lab`
- Expected `device_count`: `3`
- Expected `enabled_devices`: `["R1", "SW1"]`
- Expected `roles`: `["router", "switch", "wireless-ap"]`

### YAML

- Expected `name`: `Saturday-Lab`
- Expected `approved`: `true`
- Expected `duration_minutes`: `90`
- Expected `devices`: `["R1", "SW1"]`
- Expected `action`: `validate-configuration`

## Entry 1 - XML parsing

Prompt:
I am completing an authorized classroom Python lab. Review the parse_xml function stub and the supplied fictional XML structure. Recommend an implementation that returns exactly the keys described in the docstring. Explain default-namespace handling, returned data types, possible errors, and each ElementTree function used. Do not invent files, credentials, network calls, or test results. I will validate the recommendation using unit tests and Git diffs.

AI recommendation summary:
Codex recommended parsing the file with ET.parse() and obtaining the root element with getroot(). Because the XML uses a default NETCONF namespace, the recommendation creates an nc namespace mapping and includes that prefix in the findtext() paths. The function retrieves default-operation and test-option, checks that neither value is missing, and returns both values as strings in a dictionary.

Decision: accepted / modified / rejected
`accepted`

Validation evidence:
The two XML unit tests passed. I inspected the Git diff and confirmed that only `parse_xml` changed. The function returned `merge` and `test-then-set`, matching my manual predictions.

## Entry 2 - JSON parsing

Prompt:
I am completing an authorized classroom Python lab. Review the `parse_json` function stub and the supplied fictional JSON structure. Recommend an implementation that returns exactly the keys described in the docstring. Explain list processing, returned data types, possible errors, and each JSON library function used. Do not invent files, credentials, network calls, or test results. I will validate the recommendation using unit tests and Git diffs.

AI recommendation summary:
Codex recommended opening the file as UTF-8 text and using `json.load()` to convert the JSON into a Python dictionary. The implementation stores the device list in a variable, uses `len()` to count the devices, and uses list comprehensions to collect enabled hostnames and all device roles while preserving their original order.

Decision: 
`accepted`

Validation evidence:
All three JSON unit tests passed. I inspected the Git diff and confirmed that only `parse_json` changed. The device count, enabled hostnames, and roles matched my manual predictions.

## Entry 3 - YAML parsing and integration

Prompt:
I am completing an authorized classroom Python lab. Review the `parse_yaml` function stub and the supplied fictional YAML structure. Recommend an implementation that returns exactly the keys described in the docstring. Explain nested mapping access, list and Boolean handling, returned data types, possible errors, and each PyYAML function used. Do not invent files, credentials, network calls, or test results. I will validate the recommendation using unit tests and Git diffs.

AI recommendation summary:
Codex recommended opening the YAML file as UTF-8 text and parsing it with `yaml.safe_load()`. The implementation accesses the nested `window` mapping for the name, approval status, and duration, while reading the device list and action from the top-level mapping. For integration, Codex recommended calling each validated parser inside `build_summary` and storing the results under the `xml`, `json`, and `yaml` keys.

Decision:
`accepted`

AI recommendation summary:
Codex recommended opening the YAML file as UTF-8 text and parsing it with `yaml.safe_load()`. The implementation accesses the nested `window` mapping for the name, approval status, and duration, while reading the device list and action from the top-level mapping. For integration, Codex recommended calling each validated parser inside `build_summary` and storing the results under the `xml`, `json`, and `yaml` keys.

## Controlled merge-conflict line

Validation status: Tests passed

## Final reflection

Describe one AI suggestion that you changed or rejected and explain the evidence that guided your decision.