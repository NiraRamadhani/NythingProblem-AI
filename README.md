# NythingProblem-AI
N-ything problem is a modification of the N-queen problem.
The difference is that chess is considered not only queen (queen), but also includes knights, elephants (bishops), and rooks. 
Like the N-queen problem, the problem of N-ything problem is to look for the arrangement of chess pieces on an 8x8 chessboard 
with the number of chess pieces that attack other chess pieces at a minimum.

More formally, look for the arrangement of chess pieces so that the number of ordered pairs (p, q) where p attacks q is minimum. 
Note that if p attacks q, it's not necessarily that q also attacks p. Note also that (p, q) and (q, p) are considered as 
two different pairs.
The nature of this attack follows the nature of attack on chess games in general. For example, a fortress can attack other chess 
pieces in a vertical / horizontal path if the chess pieces are not blocked by other chess pieces, and so on.

I use the following three local search algorithms:
  1. Hill Climbing
  2. Simulated Annealing
  3. Genetic Algorithm
  
This program can handle 2 colors of chess pieces, namely black and white. 
This program will look for the composition of chess pieces so that the number of ordered pairs (p, q) where p attacks q becomes 
the minimum when p and q are the same color, and becomes maximum when p and q are different colors.


Input       : The number of each chess piece (knight, bishop, rook, queen) is a non-negative integer. 
              The total number of chess pieces must be less than 64.
Input format: <color> <type of chess pieces> <number> (input in the form of files)
