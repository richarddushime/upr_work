alive(0, _).
alive(3, _).
alive(X, X).

other_side(M, C, M_other, C_other) :-
    M_other is 3 - M,
    C_other is 3 - C.

transport(M, C, left, M_new, C, right) :-
    M_new is M - 1,
    M_new >= 0.

transport(M, C, left, M_new, C, right) :-
    M_new is M - 2,
    M_new >= 0.

transport(M, C, left, M, C_new, right) :-
    C_new is C - 1,
    C_new >= 0.

transport(M, C, left, M, C_new, right) :-
    C_new is C - 2,
    C_new >= 0.

transport(M, C, left, M_new, C_new, right) :-
    M_new is M - 1,
    M_new >= 0,
    C_new is C - 1,
    C_new >= 0.

transport(M, C, right, M_new, C_new, left) :-
    other_side(M, C, M_right, C_right),
    transport(M_right, C_right, left, M_new_right, C_new_right, right),
    other_side(M_new_right, C_new_right, M_new, C_new).

solve(0, 0, right, [(0, 0, right)], _).

solve(M, C, Side, [(M, C, Side) | Solution], Visited) :-
    \+member((M, C, Side), Visited),
    transport(M, C, Side, M_new, C_new, Side_new),
    alive(M_new, C_new),
    solve(M_new, C_new, Side_new, Solution, [(M, C, Side) | Visited]).