## Guessing Game
This is a simple guessing game where the user has a limited number of attempts to guess the correct whole number between 0 and 20. <br>
Two hints are given. <br>
You can quit anytime by entering 'q' or 'Q'.<br>
Typing in alphabets is forgiven and will NOT be penalized.


## Hints
- If the number is greater or less than a given value.
- If the number is odd or even.

## Example of game

<img src="Screenshot_2025-01-21_at_JupyterLab.png" height = "400" width="400"
     alt="Missing image..."/>
     
## Additional info
- Uses the random module to generate the guess number
- Game runs in a While loop which consists of 4 main sections;
    - 1. user input, error check and abort game
    - 2. Win condition
        - reports a Win and prompts player to play again
    - 3. Lose condition
        - reports a Lose and prompts player to play again
    - 4. game in progress
        - calculates and reports Incorrect with remaining tries, provides hints
- Uses dictionary and conditional statements
- 71 lines of code
- Saved as a Python script
