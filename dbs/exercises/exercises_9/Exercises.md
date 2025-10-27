

## 2. Set of relations based on ER diagram 
![[exercise_9.2.png]]
* $player(\underline{playerID}, username, email)$
* $friendOf(\underline{p1id \rightarrow player.playerID, p2id\rightarrow player.playerID})$
* $subscribes(\underline{taxID \rightarrow gameStudio.taxID, playerID \rightarrow player.PlayerID}, plan)$
* $gameStudio(\underline{taxID},studioName)$
* $game(\underline{gameID}, gameName, taxID \rightarrow gameStudio.taxID)$
* $match(\underline{gameID \rightarrow game.gameID, matchID}, startTime, endTime)$
* $plays(\underline{gameID \rightarrow match.gameID, matchID \rightarrow match.matchID, playerID \rightarrow player.playerID})$ 

## 3 Create a set of relations based on ER diagram using each of the four different method of mapping generalization (ISA)
![[exercise_9.3.png]]

**Main class**
* $character(\underline{charID}, name, level)$
* $warrior(\underline{charID}, name, level, weaponType, strength)$
* $mage(\underline{charID}, name, level, magicType, mana)$
**Full redundancy**
* $character(\underline{charID}, name, level)$
* $warrior(\underline{charID}, name, level, weaponType, strength)$
* $mage(\underline{charID}, name, level, magicType, mana)$
**Partitioning**
* $character(\underline{charID}, name, level)$
* $warrior(\underline{charID \rightarrow character.charID}, weaponType, strength)$
* $mage(\underline{charID \rightarrow character.charID}, magicType, mana)$
**Single relation**
remember to add type attribute. 
* $character(\underline{charID}, name, level, type, weaponType, strength, magicType, mana)$
