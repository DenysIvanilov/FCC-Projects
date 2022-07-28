#!/bin/bash
PSQL="psql --username=freecodecamp --dbname=number_guess -t --no-align -c"

echo "Enter your username:"
read USERNAME
GET_USER=$($PSQL "SELECT username FROM users WHERE username='$USERNAME'")
if [[ -z $GET_USER ]]
then
  ADD_USER=$($PSQL "INSERT INTO users(username) VALUES('$USERNAME')")
  echo "Welcome, $USERNAME! It looks like this is your first time here."
else
  GET_GAMES=$($PSQL "SELECT games_played FROM users WHERE username='$USERNAME'")
  GET_BEST=$($PSQL "SELECT best_game FROM users WHERE username='$USERNAME'")
  echo -e "\nWelcome back, $USERNAME! You have played $GET_GAMES games, and your best game took $GET_BEST guesses."
fi
SECRET_NUMBER=$[ $RANDOM % 1000 + 1 ]
echo "Guess the secret number between 1 and 1000:"
NUMBER_OF_GUESSES=0
while [[ $USER_INPUT != $SECRET_NUMBER ]]
do
  read USER_INPUT
  if [[ ! $USER_INPUT =~ ^[0-9]+$ ]]
  then
    ((NUMBER_OF_GUESSES++))
    echo "That is not an integer, guess again:"
  else
    if [[ $USER_INPUT > $SECRET_NUMBER ]]
    then
      ((NUMBER_OF_GUESSES++))
      echo "It's lower than that, guess again:"
    elif [[ $USER_INPUT < $SECRET_NUMBER ]]
    then
      ((NUMBER_OF_GUESSES++))
      echo "It's higher than that, guess again:"
    elif [[ $USER_INPUT = $SECRET_NUMBER ]]
    then
      ((NUMBER_OF_GUESSES++))
      echo -e "\nYou guessed it in $NUMBER_OF_GUESSES tries. The secret number was $SECRET_NUMBER. Nice job!"
    fi
  fi
done
UPDATE_GAMES_PLAYED=$($PSQL "UPDATE users SET games_played = games_played + 1 WHERE username='$USERNAME'")
if [[ $NUMBER_OF_GUESSES < $GET_BEST || -z $GET_BEST ]]
then
  ADD_NEW_BEST=$($PSQL "UPDATE users SET best_game = $NUMBER_OF_GUESSES WHERE username='$USERNAME'")
fi

