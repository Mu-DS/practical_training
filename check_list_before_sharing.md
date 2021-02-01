# Check-List before sharing your code

Thank you for wanting to share your code!
And thank you even more for trying to make sure it is helpful rather than sending the person in circles!
Research needs more people like you!

## Code is read way more frequently than it is written

[ ] Does your code abide by Python naming rules?

    [ ] ALL functions are snake_case
    [ ] ALL classes are UpperCamelCase
    [ ] ALL variables are snake_case
    [ ] ALL constants are UPPER_CASE
    [ ] ALL packages are lowercase

[ ] No. There are no exceptions because you prefer them...
[ ] Are your custom data structures clearly described?

    [ ] Shape?
    [ ] Data Types?
    [ ] Hierarchy?

[ ] Do ALL public functions have docstrings?
[ ] Remember that function that took you ages to write? Read the code: if you can immediately understand it you are good - otherwise, rewrite it to be more explicit.
[ ] Do ANY functions have >2 brackets opening? Split it into more lines.
[ ] Have ALL your abbreviations been defined in the same file?
[ ] No, not everyone knows that abbreviation...
[ ] Have you set up an auto-formatter?
[ ] Has the formatter configuration been documented?
[ ] Okay. Now run the formatter again.

## Code is more often debugged than it is written

[ ] Do you have notebooks?

    [ ] Restart Kernel
    [ ] Run all
    [ ] Repeat until no error shows up

[ ] Are ALL your private functions unit tested?

    [ ] Does it guarantee ALL functionality the function allows?
    [ ] Are your mathematical methods tested for convergence?
    [ ] Yes, even wrappers around standard libraries.

[ ] Have you set up a CI?

    [ ] For the NEWEST versions of packages?
    [ ] For the NEWEST versions of the language?
    [ ] Have you checked that these are really the newest?
    [ ] Does it run all notebooks?

[ ] Has it passed all tests for all versions?
[ ] Have you checked every box? Congratulations, you can now share the code :)

## Automating the boring stuff

[ ] Use **black** auto-formatting on save
[ ] Use **pylint** in CI to fail when stuff (e.g. docstrings) are missing
[ ] Use **TravisCI** to test against the newest versions from pip
[ ] Use **codecov** to ensure you are not missing unit tests

## Have more tips?

Please do let us know or simply submit your own PR to this repo!
