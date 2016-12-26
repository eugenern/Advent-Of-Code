% horizon -- adjust this for different inputs
#const h=11.

% floors, items, and initial conditions should be defined in the input file

% reify items
item(X) :- generators(X).
item(X) :- microchip(X).

direction(up).
direction(down).

% Choice rule for actions move(X,Dir,T): moves a item X or two items in the elevator up or down between times T and T+1.
{ move(X,Dir,T) : item(X), direction(Dir) } 2 :- T = 0..h-1.

% on(X,F,T): the item X is at floor F at time T
% elevator(F,T): the elevator is at floor F at time T

% moving rule: an item changes floor if it moves
on(X,Dest,T+1) :- move(X,Dir,T), on(X,Src,T), goes_to(Src,Dir,Dest).
elevator(Dest,T+1) :- move(_,T), elevator(Src,T), goes_to(Src,Dir,Dest).

% definition of the goes_to relation between floors
goes_to(F1,up,F2) :- loc(F1), loc(F2), above(F2,F1).
goes_to(F1,down,F2) :- loc(F1), loc(F2), above(F1,F2).

% Impossible to be at multiple floors at the same time
:- on(X,F1,T), on(X,F2,T), F1 != F2.
:- elevator(F1,T), elevator(F2,T), F1 != F2.

% Disallow one item moving in two directions at the same time
:- move(X, Dir1, T), move(X, Dir2, T), Dir1 != Dir2.

% inertia
on(X,F,T+1) :- on(X,F,T), not move(X,_,T), T=0..h-1.
elevator(F,T+1) :- elevator(F,T), not move(_,_,T), T=0..h-1.

% test to make sure that items don't irradiate each other
% (requires the implementation of assoc'ing generators w/ chips by element)

% goal
:- not on(X,F,h), item(X), loc(F), final(F).
:- not elevator(F,h), loc(F), final(F) .

#show move/3.
