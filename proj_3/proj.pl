/*

SAMPLE QUERY: board(16,Rows), solver(Rows).
IMPORTANT NOTE: THIS FILE IS ONLY MY SOURCE CODE, I DEVELOPED AND TESTED
      THIS PROGRAM AT THE SWISH ONLINE INTERPRETER. YOU CAN SEE AND QUERY
      THE PROJECT AT:   https://swish.swi-prolog.org/p/Sudoku_AI_2018.pl

*/
:- use_module(library(clpfd)).

solver(Rows) :-
        length(Rows, 16), maplist(same_length(Rows), Rows),
        append(Rows, Vs), Vs ins 0..15,
        maplist(all_distinct, Rows),
        transpose(Rows, Columns),
        maplist(all_distinct, Columns),
        Rows = [A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P],
        blocks(A, B, C, D), blocks(E, F, G, H), blocks(I, J, K, L), blocks(M, N, O, P).

blocks([], [], [], []).
blocks([A,B,C,D|Bs1], [E,F,G,H|Bs2], [I,J,K,L|Bs3], [M,N,O,P|Bs4]) :-
        all_distinct([A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P]),
        blocks(Bs1, Bs2, Bs3,Bs4).

/*
lst_2_lst_of_lst([], _N, []).

lst_2_lst_of_lst(L, N, LL) :-
    writeln(L),
    lst_2_lst_of_lst_helper(L, 1, N, LL).

lst_2_lst_of_lst_helper([H|T], N, N, [[H]|LL]):-
    lst_2_lst_of_lst(T, N, LL).

lst_2_lst_of_lst_helper([H|T], N1 , N, [[H|TMP]|LL]):-
    N2 is N1 + 1,
    lst_2_lst_of_lst_helper(T, N2 , N, [TMP| LL]).
*/

main :-
    %open('HexSudoku.txt', read, Str),
    %read_file(Str,Lines),
    %close(Str),

    problem(1,Rows),
    sudoku(Rows).

/*
read_file(Stream,[]) :-
    at_end_of_stream(Stream).

read_file(Stream,[X|L]) :-
    \+at_end_of_stream(Stream),
    get_char(Stream,Y),
    (Y = a -> copy_term(10,X)
    ; (Y = b -> copy_term(11,X)
      ; (Y = c -> copy_term(12,X)
        ; (Y = d -> copy_term(13,X)
          ; (Y = e -> copy_term(14,X)
            ; (Y = f -> copy_term(15,X)
              ; copy_term(Y,X)
              )
            )
          )
        )
      )
    ),
    read_file(Stream,L).
*/
board(16, [[1,_,_,_,_,12,3,_,_,_,5,_,_,_,_,10],
            [_,4,3,8,_,0,13,5,_,_,15,10,11,_,_,_],
            [_,11,9,_,_,7,_,15,_,_,13,_,1,3,_,_],
            [_,7,_,_,_,9,_,14,_,4,_,_,_,_,6,0],
            [4,14,_,_,_,15,_,_,8,_,_,_,_,_,11,12],
            [_,6,13,_,9,_,_,8,7,_,_,1,2,4,_,15],
            [_,2,_,1,3,_,_,_,_,13,_,_,_,5,_,_],
            [_,_,8,_,6,_,_,_,_,_,_,5,0,_,9,_],
            [_,12,_,4,14,_,_,_,_,_,_,15,_,2,_,_],
            [_,_,11,_,_,_,4,_,_,_,_,8,3,_,10,_],
            [3,_,1,7,2,_,_,11,4,_,_,12,_,6,0,_],
            [15,8,_,_,_,_,_,9,_,_,10,_,_,_,12,11],
            [7,13,_,_,_,_,15,_,6,_,1,_,_,_,14,_],
            [_,_,6,14,_,11,_,_,2,_,7,_,_,0,13,_],
            [_,_,_,9,8,4,_,_,5,12,3,_,10,11,1,_],
            [8,_,_,_,_,2,_,_,_,0,14,_,_,_,_,3]
      ]).
