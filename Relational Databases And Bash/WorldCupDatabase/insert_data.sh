#! /bin/bash

if [[ $1 == "test" ]]
then
  PSQL="psql --username=postgres --dbname=worldcuptest -t --no-align -c"
else
  PSQL="psql --username=freecodecamp --dbname=worldcup -t --no-align -c"
fi

# Do not change code above this line. Use the PSQL variable above to query your database.
echo $($PSQL "TRUNCATE TABLE games, teams;")
echo $($PSQL "ALTER SEQUENCE teams_team_id_seq RESTART WITH 1")
echo $($PSQL "ALTER SEQUENCE games_game_id_seq RESTART WITH 1") 

cat games.csv | while IFS=',' read year round winner opponent winner_goals opponent_goals
do
  if [[ $year != 'year' ]]
  then
    # INSERTING TEAMS
    WTEAM=$($PSQL "SELECT name FROM teams WHERE name='$winner'")
    if [[ -z $WTEAM ]]
    then
      INSERT_WTEAM=$($PSQL "INSERT INTO teams(name) VALUES('$winner')")
    fi
    OTEAM=$($PSQL "SELECT name FROM teams WHERE name='$opponent' AND team_id IS NOT NULL")
    if [[ -z $OTEAM ]]
    then
      INSERT_OTEAM=$($PSQL "INSERT INTO teams(name) VALUES('$opponent')")
    fi
    # INSERTING GAMES
    GET_WID=$($PSQL "SELECT team_id FROM teams WHERE name='$winner'")
    GET_OID=$($PSQL "SELECT team_id FROM teams WHERE name='$opponent'")
    INSERT_GAME=$($PSQL "INSERT INTO games(year, round, winner_id, opponent_id, winner_goals, opponent_goals) VALUES($year, '$round', $GET_WID, $GET_OID, $winner_goals, $opponent_goals)") 
  fi
done