
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
