/**
*   S: START POLE,
*   E: END POLE,
*   H: HELP POLE,
*   D: DISKS,
*   T: TEMPORARY VARIABLE.
*/

solve(1,S,E,_):-
    write('Move top disk from '),
    write(S),
    write(' to '),
    write(E),
    nl.

solve(D,S,E,H):-
    D>1,
    T is D-1,
    solve(T,S,E,H),
    solve(1,S,E,_),
    solve(T,H,E,S).