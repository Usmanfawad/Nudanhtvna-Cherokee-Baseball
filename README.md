# Nudanhtvna-Cherokee-Baseball
A python based algorithmic assignment

## Programming Concepts Assignment (March 2020)

The purpose of this assignment is to show how well you can develop a programming project. It will give you an opportunity to display your knowledge of the Python programming language. This assignment is marked initially with a maximum score of 100. It is then weighted to contribute 25% to your overall module assessment.

## Scenario:  Nudanhtvna (Cherokee Baseball).
The first organised American baseball league did not exist before 1858 although early versions of the game can be traced back to the English game of 'stoolball' which was played by domestic servants as early as 1330. Stoolball was introduced into what became the United States of America in 1621. However some people now believe that baseball may also have roots in the pre-European Cherokee game of Nudanhtvna. This was a ritual conflict between Cherokee youths and success in playing it had important consequences within the tribe, affecting social status and marriage prospects. Evidence for the influence of Nudanhtvna in the development of baseball is found in the way that the Cherokee game was played on a typical baseball 'diamond'.

Two opponents stood at the opposite corners of the diamond-shaped playing field, one at the 'top' and the other at the 'bottom'. They then ran towards one another, each trying to reach their opponent's corner. The game was won when either the corner had been reached or the opponent successfully blocked. The game was then repeated on a carefully measured larger diamond playing field. Successive games continued on increasingly larger fields until a tribal elder announced which Cherokee youth was regarded as the winner.
What you have to do:

You will develop your version of Nudanhtvna as a computer game. You are given some code already and have to develop it further into a game for two players, A and B, who move across a diamond-shaped grid by entering the letters U, D, L or R (for up, down, left or right). They take alternate turns. A begins at the top corner of the grid and has to reach the bottom corner. B begins at the bottom and has to reach the top. A particular round of the game is won when a player reaches the corner they are moving towards, or is blocked by their opponent. The overall game will begin at 'level 8' and continue to levels 9 and 10. ('Levels' are explained below.

Here is the Python program code you begin with. (It can be pasted directly into IDLE once you have installed Python from Apps Anywhere.)


def display(A, B):
    R = A * 2 - 1
    N = -1
    K = 0
    G = A - 1
    for i in range(R):
        K = K - (i > R / 2)
        JL = (i + K * 2) * 2 + 1
        for j in range(G):
            print chr(32),
        if (i < R / 2):
            G = G - 1
        else:
            G = G + 1
        for j in range(JL):
            N = N + 1
            if (j == 0) or (j == JL - 1):
                B[N] = 35
            print chr(B[N]),
        print

def move(A, B, C):
    R = A * 2 - 1
    N = -1
    K = 0
    for i in range(R):
        K = K - (i > R / 2)
        JL = (i + K * 2) * 2 + 1
        for j in range(JL):
            N = N + 1    
            if (N == B):
                U = JL - 1 + 2 * (K < 0)
                D = JL + 1 - 2 * (K < 0) - 2 * (JL == 2 * A - 1)
    if (C == "U"):
        B = B - U
    if (C == "D"):
        B = B + D
    if (C == "L"):
        B = B - 1
    if (C == "R"):
        B = B + 1
    return B

def main():
    board = [46] * 200
    
main()
Here are two illustrations of the code being used to produce displays in the Python shell:



By writing appropriate code of your own in main() and calling the two functions provided you will be able to develop Nudanhtvna as a exciting computer game…

Important details: 

1. Your solution should be written as a Python program employing functions, with variables being passed and returned. 

2. The code must be original and not copied from anywhere else. 

3. You will probably want to work at home on the assignment. However you must always bring your work into College and work on it during class time. (This will be monitored.) 

4. Do not use object-oriented methodology. 

5. After your work is submitted you might be interviewed in order to explain sections of your program.

You must upload your work to 'Turnitin' by 4.00pm on Friday in Week 10 of the semester. 

The following are the four sections of your work which you will submit. They should form a single Word document, with relevant screen captures. 


Section A: Explanation of the problem (30 marks)

In this section you do NOT submit any algorithms or Python code. Instead you should explain informally, in ordinary language, how your computer program will allow your computer game to achieve the objectives described above. You should describe carefully all the ideas you have had for how the program will be made to work. Although you will not present any code in this section you will talk about programming constructs like for and while loops, array locations and subscripts, calling functions, passing and returning variables etc.


Section B: Algorithms required (10 marks) 

Select any one of the algorithms needed for your program and formally represent it as a flowchart.


Section C: Program code (50 marks)

Here you give your program listing. Your Python code should show that you understand how a program can achieve the following. 

Input  
Output 
Variables and assignment
Subscripted variables (arrays)
Comments
Conditional statements 
Unconditional loops 
Conditional loops
Use of functions
Validation of user input


Section D: Testing of your solution (10 marks)

You should present a minimum of two screen shots indicating that you have tested your program. Comment on what the screen shot contains and how this relates to a section of the program code you have given in Section C.


Computer software is often made available for use before it is completely working! Therefore you are not necessarily expected to produce fully operating code. Instead marks will be awarded to how well you have attempted the various tasks described above.


Section A: Learning Outcomes (LO) to be assessed 

LO	LO Description 	Comment on LO attainment	LO Achieved: Yes/No
A1	That computer programs are designed to solve problems	
	
A2
	The success of a program depends on how well the problem is understood and then broken down into identifiable components		
A5	A programmer must ensure his program can be easily understood by other programmers with appropriate structure and annotation.	
	
C3
	Ability to troubleshoot basic (hardware and) software issues		
D4	Abstraction of complex problems into manageable elements.		

Section B: ILSC Study Skills Incorporated and Tested 

Skills	
Yes/No	
Comments
Personal Development (Self-reflection, responding to feedback)	NO	N/A
Presentation Skills	YES	Flowchart in Section B, Screen capture in Section D
Listening Skills		N/A
Self - Directed Study	YES	Working on versions of main()
Writing Skills (Accuracy, Coherence)	NO	N/A
Analysis and Problem Solving	YES	Creating appropriate loops and exit conditions
Planning Aspects (Structure, Content Development)	NO	N/A
Working with Others	N/A	N/A


Marking scheme

Section A: Explanation of the problem (30 marks)

After all of the scripts have been read initially (in order to judge how the specific cohort of students has interpreted the problem) a detailed marking scheme will be written for Section A. This will award 3 marks for each relevant explanation of aspects of i) algorithm design ii) programming concepts employed. There is a maximum of 30 for this section.

Section B: Algorithms required (10 marks) 

Only ONE of these criteria will be relevant:

A: Relevant flow chart - 4 marks
B: As above plus (mostly) correct symbols – 7 marks
C: As above plus (mostly) correct logic – 10 marks

Section C: Program code (50 marks)

5 marks awarded for each of the following marking criteria up to a maximum of 50:

A: Input of data from user 
B: Display of text by program
C: Assignment of values to variables
D: Use of subscripted variables (arrays)
E: Inclusion of explanatory comments
F: Use of conditional structure 
G: Use of loop structure
H: Passing a value to a function
I: Returning a value from a function
J: Validation of user input

Section D: Testing of your solution (10 marks)

Any of these criteria will be relevant:

A: First screen shot – 3 marks
B: Discussion of first screen shot – 2 marks
C: Second screen shot – 3 marks
D: Discussion of second screen shot – 2 marks

