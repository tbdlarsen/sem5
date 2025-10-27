

## 2. Set of relations based on ER diagram 
![[dbs/exercises/exercises_9/exercise_2.png]]
* $player(\underline{playerID}, username, email)$
* $friendOf(\underline{p1id \rightarrow player.playerID, p2id\rightarrow player.playerID})$
* $subscribes(\underline{taxID \rightarrow gameStudio.taxID, playerID \rightarrow player.PlayerID}, plan)$
* $gameStudio(\underline{taxID},studioName)$
* $game(\underline{gameID}, gameName, taxID \rightarrow gameStudio.taxID)$
* $match(\underline{gameID \rightarrow game.gameID, matchID}, startTime, endTime)$
* $plays(\underline{gameID \rightarrow match.gameID, matchID \rightarrow match.matchID, playerID \rightarrow player.playerID})$ 