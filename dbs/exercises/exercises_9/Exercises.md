## 1. Review definitions

* Entity types
  entity types are created as relations. weak entity types are also added as relations, but have the addition that we append a foreign key of the related strong entity type to it, and that key is also part of the primary key of the relation.
* Relationship types
  many to many: create a relation, add attributes of relationship type to relation, the primary key of the relation is the union of the relations in the relationship
  one to many: 
  Option 1: create a relation, add attributes, primary key is a foreign key to the "many" side of the relation, also add a foreign key to the primary key of the other relation, but not part of primary key to new relation.
  Option 2: extend the many side of the relation, add attributes of relationship to relation of "many" side, add foreign key of the "one" side
  many to one: same as one to many, just the other side. 
  one to one:  
  Option 1: create a new relation, add attributes, primary key is one of the primary keys of the relations involved, add foreign key to other relation
  Option 2: Extend either side of the relationship (if any of them are total participation, choose that to avoid null values). Add foreign key, that is primary key of other relation in the relationship, add the attributes of the relationship to relation. If both sides have total participation, they can be merged into one relation. 
  
* Attribute types
  multi valued: create separate relation, i.e. 
![[multivalue_attribute.png]]
	composite attributes: add each root attribute instead of the composite one. 
	derived attributes: don't add in relation, since these can be calculated later. 


* Relational modelling of Specialization (ISA).
	* there are the four types seen in [[#3 Create a set of relations based on ER diagram using each of the four different method of mapping generalization (ISA)| exercise 3]] to represent specializations.
	  main class: the instances are only added in their "main class"
	  full redundancy: the instances are added in their "parent relation" and their specialization relation
	  partitioning: there is a reference to the primary key of the parent relation in the specialization relation
	  single relation: all attributes are added to one relations, along with at type attribute, values are null where not applicable, i.e. in [[#3 Create a set of relations based on ER diagram using each of the four different method of mapping generalization (ISA) | exercise 3]] a mage would have null in weaponType and strength.

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
