# AI-Assisted Git Workflow and Python Data Parsing

Student name: Gab Claro  
Section: TS31

## Project purpose

This project demonstrates a local Git development workflow while parsing fictional network data stored in XML, JSON, and YAML formats. The work used a feature branch, meaningful commits, unit testing, manual output inspection, merging, and deliberate conflict resolution.

## How to run

```powershell
py parser_template.py
py -m unittest -v
```

`parser_template.py` prints a combined summary of the three data files. The unit-test command runs all seven supplied tests.

## Git workflow summary

The repository began with a baseline commit on `main`. Parser development was completed on `feature/data-parsers` using separate commits for the XML, JSON, YAML, and combined-summary implementations. After all seven tests passed, the feature branch was merged into `main`.

The `docs/ai-note` branch changed the controlled validation line to `AI reviewed`, while `main` changed the same line to `Tests passed`. Merging the branches produced the expected conflict. I removed the conflict markers and combined both meanings into `Validation status: AI reviewed and tests passed.`

## Parser results

The XML parser returned `merge` as the default operation and `test-then-set` as the test option.

The JSON parser identified the `FEU-Tech-Lab` site, counted three devices, listed `R1` and `SW1` as enabled, and returned the roles `router`, `switch`, and `wireless-ap`.

The YAML parser returned the `Saturday-Lab` maintenance window, an approval value of `true`, a duration of 90 minutes, the devices `R1` and `SW1`, and the action `validate-configuration`.

## AI disclosure

I used Codex to recommend implementations one function at a time. I manually inspected the supplied data before implementation, reviewed every Git diff, ran the relevant unit tests, and compared the final program output with my predictions. The code recommendations were accepted only after validation.

I modified the suggested terminal commands to use the Windows `py` launcher instead of `python3`. The installed interpreter version and passing tests confirmed that this adjustment was appropriate for my environment.

## Safety statement

Only the fictional files supplied for this classroom activity were used. No passwords, authentication tokens, private repository data, institutional secrets, or personal information were submitted to the AI tool.