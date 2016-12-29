% horizon -- adjust this for different inputs
%#const h=40.

% floors, items, and initial conditions should be defined in the input file

% reify items
item(X) :- generator(X).
item(X) :- microchip(X).

direction(up).
direction(down).

% Choice rule for actions move(X,Dir,T): moves a item X or two items in the elevator up or down between times T and T+1.
{ move(X,Dir,T) : item(X), direction(Dir) } 2 :- T = 0..h-1.

:- move(X,_,T), on(X,F,T), elevator(FF,T), F != FF.

% on(X,F,T): the item X is on floor F at time T
% elevator(F,T): the elevator is on floor F at time T

% moving rule: an item changes floor if it moves; hardcoded in directions to improve efficiency
on(X,Dest,T+1) :- move(X,up,T), on(X,Src,T), above(Dest,Src).
elevator(Dest,T+1) :- move(_,up,T), elevator(Src,T), above(Dest,Src).
on(X,Dest,T+1) :- move(X,down,T), on(X,Src,T), above(Src,Dest).
elevator(Dest,T+1) :- move(_,down,T), elevator(Src,T), above(Src,Dest).

% don't allow moving up from the top floor or down from the bottom floor; hardcoded in directions and floors for efficiency
:- move(_,up,T), elevator(fourth,T).
:- move(_,down,T), elevator(first,T).

% Impossible to be on multiple floors at the same time
:- on(X,F1,T), on(X,F2,T), F1 != F2.
:- elevator(F1,T), elevator(F2,T), F1 != F2.

% inertia
on(X,F,T+1) :- on(X,F,T), not move(X,_,T), T=0..h-1.
elevator(F,T+1) :- elevator(F,T), not move(_,_,T), T=0..h-1.

% test to make sure that items don't irradiate each other
:- on(M1,F1,T), on(G2,F1,T), microchip(M1), generator(G2), corresponds(M1,G1), G1 != G2, not on(G1,F1,T).

% goal -- again, hardcoded in final floor for efficiency
:- not on(X,fourth,h), item(X).

#show move/3.
