# Welcome to my Hangman-Game

## Play some Hangman from within in your terminal!

Hangman is a fun and interactive game where the user plays a word-guessing game by guessing the letters of a random word generated by the computer. The user will have up to 6 chances for guessing a wrong letter, until the visual on the screen will depict a 'hanged man' indicating you have lost the game. Complete the word in full before your 7 chances are up and you have won the game.

## User Experience (UX)
### User Stories

* As user engaging with the application I want to be able to participate in a word game.
* As user playing the game I want the instructions to be clear.
* As user I want to interact easily with the application.
* As user I want to see my progress on a visual level.
* As a user I want to be informed when my actions/decisions were right or wrong.
* As user I want be able to play again or exit once the game is over.

### Application Goals
* Create a words based guessing challenge for the user.
* Provide the user with an interface to input required actions for the game to be played.
* Include visuals of the user's current status within the game as they play.
* Inform the user when they have used all their chances, or if they have won the game.
* Have the user be able to answer all questions in succession.
* Let the user be able to revert back to the start if they choose play the game again.

### How to Play/Use the App
* User is greeted with a question whether they want to start the game by typing 'yes'.


* User is shown the four rules of the game.


* Message prompts user to to guess the correct randomly generated word and displays a line depicting the length of word.


* User is given 8 chances to guess the wrong letter. On the 8th wrong guess, user loses the game.


* Upon guessing each correct letter, they will appear in their respective position in the word.


* If user guesses the wrong letter, part of a picture will be displayed of a hanging man. 


* Each wrong guess completes the picture further.  


* If user guesses the correct word within the designated amount of tries, they will win the game and be congratulated.


## Application Flow of logic and features

### Start-Game Logic & Workflow

![start-game-logic](images/workflow-charts/start-game-logic.png)

### In-Game Logic & Workflow

![in-game-logic](images/workflow-charts/in-game-logic.png)

<br>

# Technology, Frameworks and Programs used.

## Languages

- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

## Dependencies and Frameworks

- [Time Library](https://docs.python.org/3/library/time.html)
    - Used to time code execution.

- [Random Library](https://docs.python.org/3/library/random.html)
    - Used to randomize words if API is down giving status code 503.

- [OS](https://docs.python.org/3/library/os.html)
    - Used to clear terminal before new word is being displayed.

- [Patorjk.com](https://patorjk.com/software/taag/#p=display&f=Big&t=)
    - Used to make ASCII art

- [PEP8 Code Institute](https://pep8ci.herokuapp.com/#)
    - Used to linter Python code and see if any mistakes or issues came up.


# FEATURES
### Click to expand the info for each feature
<details>
  <summary>Starting the game</summary>

  FEATURE | IMAGE | DESCRIPTION
  :---:|:---:|:---:
  Prompt to initialize game | ![](images/features/initialize-game.png) | User gets greeted and asked to start game
  
</details>

<details>
  <summary>Displaying rules of the game</summary>

  FEATURE | IMAGE | DESCRIPTION
  :---:|:---:|:---:
  Rules are displayed one by one to the user before the first play can be made | ![](images/features/game-rules.png) | User can examine the rules of the game before starting to play
  
</details>

<details>
  <summary>In-Game display</summary>

  FEATURE | IMAGE | DESCRIPTION
  :---:|:---:|:---:
  User can see the depiction of the gallows followed by in-game information | ![](images/features/in-game-display.png) | User can see additional information such as the amount of letters needed to be guessed, the amount of tries available, letters guessed correctly and incorrectly
  
</details>

<details>
  <summary>In-Game Progress</summary>

  FEATURE | IMAGE | DESCRIPTION
  :---:|:---:|:---:
  User can see how they are faring as they continue to play the game | ![](images/features/in-game-progress.png) | All in-game information is updated according to what letters they guessed correctly and incorrectly. Ascii art displays hanging man inaccordance with amount of wrong guesses
  
</details>

<details>
  <summary>User Completes the Word</summary>

  FEATURE | IMAGE | DESCRIPTION
  :---:|:---:|:---:
  User is displayed with a congratulatory message | ![](images/features/completed-word.png) | Once the word is completed the user is congratulated and prompted to either play again or otherwise quit the game.
  
</details>

<details>
  <summary>User Loses/ Runs out of Guesses</summary>

  FEATURE | IMAGE | DESCRIPTION
  :---:|:---:|:---:
  User is displayed with a message saying the game is over | ![](images/features/game-over.png) | Game-Over message is dislayed with some prompts to encourage user to try again and given instructions how to continue or quit
  
</details>

<details>
  <summary>User Chooses to Play Again</summary>

  FEATURE | IMAGE | DESCRIPTION
  :---:|:---:|:---:
  User is prompted to go again | ![](images/features/go-again.png) | Visuals appear to encourage user to go again. Rules are displayed again followed by in-game display
  
</details>

<details>
  <summary>User Chooses to Quit</summary>

  FEATURE | IMAGE | DESCRIPTION
  :---:|:---:|:---:
  User is displayed a goodbye message | ![](images/features/goodbye.png) | Visual ascii art appears to say: "See ya next time". Game exits
  
</details>

<br>

# TESTING

## Manual Testing Within Terminal

- I have made various attempts to make sure that each feature and function runs according to my workflow charts as depicted above. I made sure to implement manual testing methods after writing each function to see whether the game performs each task as intended. I would write a function, implement it where I would want it to run/display, and then run the app in my terminal to see whether it has achieved the desired outcome. I followed these steps after each individual function and/or feature was implemented.

- I was able to see visual progress during each testing phase. However not always did everything go according to plan. Some amount of bugs were caught, which were then dealt with accordingly as shown below.


## Bugs
### Click to expand the info for each bug
<details>
  <summary>Error: Line too long</summary>

  ERROR | IMAGE | DESCRIPTION | SOLUTION
  :---:|:---:|:---:|:---:
  Lines were too long in the terminal | [![Error Image](images/bugs/error-line-too-long.png)](images/bugs/error-line-too-long.png) | String lines were all too long in the terminal. This was everywhere in my code template. I had to break each line into shorter pieces using quotation marks. | [![Solution Image](images/bugs/line-too-long-solution.png)](images/bugs/line-too-long-solution.png)
  
</details>

<details>
  <summary>Error: Wrong Ascii image displayed at start</summary>

  ERROR | IMAGE | DESCRIPTION | SOLUTION
  :---:|:---:|:---:|:---:
  At the start of the game, the final image of the hangman art was displaying instead of the first | [![Error Image](images/bugs/error-showing-final-art-not-first.png)](images/bugs/error-showing-final-art-not-first.png) | The wrong image was called at the start of the game and I had to ammend code to call the first image showing the gallows. Code ammended was adding an array within the function calling for the images from the start. "print(hangman_image[hangman_count])" | [![Solution Image](images/features/in-game-display.png)](images/features/in-game-display.png)
  
</details>

<details>
  <summary>Error: Past rounds filling up space in the terminal</summary>

  ERROR | IMAGE | DESCRIPTION | SOLUTION
  :---:|:---:|:---:|:---:
  Each attempt stays in displayed instead of being erased | [![Error Image](images/bugs/error-handling-displays-past-attempts.png)](images/bugs/error-handling-displays-past-attempts.png) | I wanted to clear the terminal of past attempts to have everything look cleaner, as the game is set up aleady to display the users current game state on each new try. There was no need for showing the history of guesses in the terminal, so I imported os and ran"os.system('cls' if os.name == 'nt' else 'clear')" within various functions to clear the terminal after guesses and showing the most current game state.| [![Solution Image](images/features/in-game-progress.png)](images/features/in-game-progress.png)
  
</details>

<details>
  <summary>Error: User was able to guess with numbers</summary>

  ERROR | IMAGE | DESCRIPTION | SOLUTION
  :---:|:---:|:---:|:---:
  Numbers were being passed as valid inputs | [![Error Image](images/bugs/error-can-restart-game-with-number-input.png)](images/bugs/error-can-restart-game-with-number-input.png) | The user should not be allowed to use numbers, spaces or punctuation as inputs. I had to write some error-handling code to prevent such inputs from happening| [![Solution Image](images/bugs/erro-handling.png)](images/bugs/erro-handling.png)
  
</details>

<br>

## PEP 8 Linting

I used Code Institute's PEP 8 Linter to check for errors in my code templates, as can be seen below:

- run.py ran through pep8 linter and found no errors
    <details><summary>run.py</summary>
    <img src="images/PEP8/PEP8-runpy.png" alt="no errors">
    </details>
<br>

- utils.py ran through pep8 linter and found no errors
    <details><summary>utils.py</summary>
    <img src="images/PEP8/PEP8-utils.png" alt="no errors">
    </details>
<br>

- hangman_ascii_art.py ran through pep8 linter and found multiple errors. These errors were tolerated as they were all only warnings regarding indentations and spacings around the ascii art used
    <details><summary>hangman_ascii_art.py</summary>
    <img src="images/PEP8/PEP8-ascii-art.png" alt="multiple errors">
    </details>
<br>

## Testing User Stories
### Click to expand the info for each User Story
<details>
  <summary>User Story 1</summary>

  USER STORY | IMAGE | STATUS
  :---:|:---:|:---:
  As user engaging with the application I want to be able to participate in a word game. | ![](images/features/initialize-game.png) | Complete
  
</details>

<details>
  <summary>User Story 2</summary>

  USER STORY | IMAGE | STATUS
  :---:|:---:|:---:
  As user playing the game I want the instructions to be clear. | ![](images/features/game-rules.png) | Complete
  
</details>

<details>
  <summary>User Story 3</summary>

  USER STORY | IMAGE | STATUS
  :---:|:---:|:---:
  As user I want to interact easily with the application. | ![](images/features/interaction.png) | Complete
  
</details>

<details>
  <summary>User Story 4</summary>

  USER STORY | IMAGE | STATUS
  :---:|:---:|:---:
  As user I want to see my progress on a visual level. | ![](images/features/in-game-progress.png) | Complete
  
</details>

<details>
  <summary>User Story 5</summary>

  USER STORY | IMAGE | STATUS
  :---:|:---:|:---:
  As a user I want to be informed when my actions/decisions were right or wrong. | ![](images/features/wrong-guess.png) | Complete
  
</details>

<details>
  <summary>User Story 6</summary>

  USER STORY | IMAGE | STATUS
  :---:|:---:|:---:
  As user I want be able to play again or exit once the game is over. | ![](images/features/try-again.png) | Complete
  
</details>

<br>

# Deployment

- This application was created locally and deployed with Heroku afterwrds, and not making use of any external libraries or API's. The only datasheet used is a 'words.txt' file stored locally.

- Make use of the following steps for manual deployment:

1. Go to [GitHub](https://github.com/) and login if you arent yet, then go to [this link](https://github.com/Aron-M/Play-Hangman). It will open my repository, then press **< CODE >** and press **Local** then press Copy to clipboard button.
    <details><summary>Picture</summary>
    <img src="images/deployment/hangman-github-repo.png" alt="github"/>
    </details>
    <br>