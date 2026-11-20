# Lab 5: Reflection

**Student:** Yashas  
**SRN:** PES2UG24CS609

> The supplied three-page handout says to answer four reflection questions, but the question text is not present in the copy provided. These responses address the main reflection themes from the completed work; they may need to be matched to the instructor's exact wording.

1. **What did static analysis reveal beyond running the program?**  
   Running the demo showed its basic behavior, but the tools exposed risks that ordinary inputs did not reveal: arbitrary code evaluation, a shell command built with a filename, a weak digest, a predictable PIN generator, shared mutable state, and style and maintainability problems.

2. **Which finding was most important to fix, and why?**  
   The `eval` call was the most urgent because it treated a discount string as executable Python. Replacing it with a numeric discount rate removed code execution and made the accepted input range explicit.

3. **What trade-offs did the fixes introduce?**  
   The revised discount function accepts a percentage rate rather than a Python expression. This is a narrower interface, but it is easier to validate and safer to use. The receipt remains readable JSON, while item fingerprints use SHA-256 and the checkout PIN uses a cryptographic random source.

4. **How will static analysis change future development?**  
   I would run the checks before and after changes, address security findings first, and keep the reports with the code. Static analysis does not prove a program is correct, so I would pair it with representative runs and tests for expected and invalid inputs.
