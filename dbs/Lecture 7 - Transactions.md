
ACID 
atomic
consistent
isolated
durable
see slide 10 


no partial transactions, either full transaction or abort.
during the execution of transaction the DB can be in invalid state, but not at the end of the transaction.


start: BEGIN
end with COMMIT or ABORT
abort = rollback, resets the state back to before the transaction


interleaving execution 
serializable

When is there a conflict see slide 20

if all serial conflicts are the same between two transactions they are equivalent. 


dependency graph to see if conflicts are serializable
directed acyclic, if there is a cycle it is not serializable
if deadlock then rollback


enforcing serializable executions


READ psql locks and lock manager 

2-phase locking 

phase 1 growing
only request locks

phase 2 shrinking
only release locks
once you have released a lock you are in phase 2 meaning you can no longer ask for more locks.
lookup lock downgrades (don't change a lock from an exclusive (write) to a non exclusive (read))



how 2 deal with deadlocks
detect deadlock and kill one of the transactions.
prevent deadlocks and abort transactions asking too much.


optimistic vs pessimistic serializability, 
optimistic = check version number at end of transaction and hope it is not changed
pessimistic = do locks.
optimistic if low chance of working on same records at same time, else pessimistic. 

keep durability
crash recovery 
2 phases 
actions during 
actions after 
overall solution
1 write all your operations in a log of operations before anything else
2 if you fail, compare the operation in the log with what has been completed in the db 

write-ahead log
maintain a log file separate from data files that contains the changes that transactions have to make to the database.
- assume that the log is on stable storage
- log contain enough information to perform the necessary undo and redo actions to restore the database
















