from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Sample dataset for GATE CSE questions in MCQ format
questions_db = {
    "easy": [
{
  "question": "Consider the following statements regarding the front-end and back-end of a compiler.",
  "options": [
      "Only S1 is TRUE.",
      "Only S1 and S2 are TRUE.",
      "S1, S2, and S3 are all TRUE.",
      "Only S1 and S3 are TRUE."
  ],
  "answer": "Only S1 and S2 are TRUE."
},
{
  "question": "Which one of the following sequences when stored in an array at locations A[1], . . . , A[10] forms a max-heap?",
  "options": [
      "23, 17, 10, 6, 13, 14, 1, 5, 7, 12",
      "23, 17, 14, 7, 13, 10, 1, 5, 6, 12",
      "23, 17, 14, 6, 13, 10, 1, 5, 7, 15",
      "23, 14, 17, 1, 10, 13, 16, 12, 7, 5"
  ],
  "answer": "23, 17, 14, 7, 13, 10, 1, 5, 6, 12"
},
{
  "question": "Let f: R -> R be a function such that f(x) = max{x, x^3}, x ∈ R, where R is the set of all real numbers. The set of all points where f(x) is NOT differentiable is",
  "options": [
    "-1, 1, 2",
    "-2, -1, 1",
    "0, 1",
    "-1, 0, 1"
  ],
  "answer": "-1, 0, 1"
},
{
  "question": "Consider a permutation sampled uniformly at random from the set of all permutations of {1, 2, 3, ..., n} for some n ≥ 4. Let X be the event that 1 occurs before 2 in the permutation, and Y the event that 3 occurs before 4. Which one of the following statements is TRUE?",
  "options": [
    "The events X and Y are mutually exclusive",
    "The events X and Y are independent",
    "Either event X or Y must occur",
    "Event X is more likely than event Y"
  ],
  "answer": "The events X and Y are independent"
},
{
  "question": "Consider a system that uses 5 bits for representing signed integers in 2's complement format. In this system, two integers A and B are represented as A = 01010 and B = 11010. Which one of the following operations will result in either an arithmetic overflow or an arithmetic underflow?",
  "options": [
    "A + B",
    "A - B",
    "B - A",
    "2 * B"
  ],
  "answer": "A + B"
},
{
  "question": "A bag contains 10 red balls and 15 blue balls. Two balls are drawn randomly without replacement. Given that the first ball drawn is red, the probability (rounded off to 3 decimal places) that both balls drawn are red is __",
  "options": [
    "0.231",
    "0.333",
    "0.429",
    "0.500"
  ],
  "answer": "0.231"
},
{
  "question": "A user starts browsing a webpage hosted at a remote server. The browser opens a single TCP connection to fetch the entire webpage from the server. The webpage consists of a top-level index page with multiple embedded image objects. Assume that all caches (e.g., DNS cache, browser cache) are all initially empty. The following packets leave the user's computer in some order.\n(i) HTTP GET request for the index page\n(ii) DNS request to resolve the web server's name to its IP address\n(iii) HTTP GET request for an image object\n(iv) TCP SYN to open a connection to the web server\nWhich one of the following is the CORRECT chronological order (earliest in time to latest) of the packets leaving the computer?",
  "options": [
    "(iv), (ii), (iii), (i)",
    "(ii), (iv), (iii), (i)",
    "(ii), (iv), (i), (iii)",
    "(iv), (ii), (i), (iii)"
  ],
  "answer": "(ii), (iv), (i), (iii)"
},
{
  "question": "Given an integer array of size N, we want to check if the array is sorted (in either ascending or descending order). An algorithm solves this problem by making a single pass through the array and comparing each element of the array only with its adjacent elements. The worst-case time complexity of this algorithm is",
  "options": [
    "both O(N) and Ω(N)",
    "O(N) but not Ω(N)",
    "Ω(N) but not O(N)",
    "neither O(N) nor Ω(N)"
  ],
  "answer": "both O(N) and Ω(N)"
},
{
  "question": "Consider the following C program:\nc\n#include <stdio.h>\nvoid fX();\nint main() {\n    fX();\n    return 0;\n}\nvoid fX() {\n    char a;\n    if((a=getchar()) != '\\n') fX();\n    if(a != '\\n') putchar(a);\n}\n\nAssume that the input to the program from the command line is 1234 followed by a newline character. Which one of the following statements is CORRECT?",
  "options": [
    "The program will not terminate",
    "The program will terminate with no output",
    "The program will terminate with 4321 as output",
    "The program will terminate with 1234 as output"
  ],
  "answer": "The program will terminate with 4321 as output"
},
{
  "question": "The product of all eigenvalues of the matrix [1 2 3; 4 5 6; 7 8 9] is:",
  "options": [
    "-1",
    "0",
    "1",
    "2"
  ],
  "answer": "0"
},
{
  "question": "Consider a system that uses 5 bits for representing signed integers in 2's complement format. In this system, two integers A and B are represented as A = 01010 and B = 11010. Which one of the following operations will result in either an arithmetic overflow or an arithmetic underflow?",
  "options": [
    "A + B",
    "A - B",
    "B - A",
    "2 * B"
  ],
  "answer": "A + B"
},
{
  "question": "Consider a permutation sampled uniformly at random from the set of all permutations of {1, 2, 3, ..., n} for some n ≥ 4. Let X be the event that 1 occurs before 2 in the permutation, and Y the event that 3 occurs before 4. Which one of the following statements is TRUE?",
  "options": [
    "The events X and Y are mutually exclusive",
    "The events X and Y are independent",
    "Either event X or Y must occur",
    "Event X is more likely than event Y"
  ],
  "answer": "The events X and Y are independent"
},
{
  "question": "Which one of the following statements is FALSE?",
  "options": [
    "In the cycle stealing mode of DMA, one word of data is transferred between an I/O device and main memory in a stolen cycle",
    "For bulk data transfer, the burst mode of DMA has a higher throughput than the cycle stealing mode",
    "Programmed I/O mechanism has a better CPU utilization than the interrupt driven I/O mechanism",
    "The CPU can start executing an interrupt service routine faster with vectored interrupts than with non-vectored interrupts"
  ],
  "answer": "Programmed I/O mechanism has a better CPU utilization than the interrupt driven I/O mechanism"
},
{
  "question": "The product of all eigenvalues of the matrix [1 2 3; 4 5 6; 7 8 9] is:",
  "options": [
    "-1",
    "0",
    "1",
    "2"
  ],
  "answer": "0"
},
{
  "question": "A user starts browsing a webpage hosted at a remote server. The browser opens a single TCP connection to fetch the entire webpage from the server. The webpage consists of a top-level index page with multiple embedded image objects. Assume that all caches (e.g., DNS cache, browser cache) are all initially empty. The following packets leave the user's computer in some order.\n(i) HTTP GET request for the index page\n(ii) DNS request to resolve the web server's name to its IP address\n(iii) HTTP GET request for an image object\n(iv) TCP SYN to open a connection to the web server\nWhich one of the following is the CORRECT chronological order (earliest in time to latest) of the packets leaving the computer?",
  "options": [
    "(iv), (ii), (iii), (i)",
    "(ii), (iv), (iii), (i)",
    "(ii), (iv), (i), (iii)",
    "(iv), (ii), (i), (iii)"
  ],
  "answer": "(ii), (iv), (i), (iii)"
},
{
  "question": "Consider the following C program:\nc\n#include <stdio.h>\nvoid fX();\nint main() {\n    fX();\n    return 0;\n}\nvoid fX() {\n    char a;\n    if((a=getchar()) != '\\n') fX();\n    if(a != '\\n') putchar(a);\n}\n\nAssume that the input to the program from the command line is 1234 followed by a newline character. Which one of the following statements is CORRECT?",
  "options": [
    "The program will not terminate",
    "The program will terminate with no output",
    "The program will terminate with 4321 as output",
    "The program will terminate with 1234 as output"
  ],
  "answer": "The program will terminate with 4321 as output"
},
{
    "question": "Let SLLdel be a function that deletes a node in a singly-linked list given a pointer to the node and a pointer to the head of the list. Similarly, let DLLdel be another function that deletes a node in a doubly-linked list given a pointer to the node and a pointer to the head of the list. Let n denote the number of nodes in each of the linked lists. Which one of the following choices is TRUE about the worst-case time complexity of SLLdel and DLLdel?",
    "options": [
        "SLLdel is O(1) and DLLdel is O(n)",
        "Both SLLdel and DLLdel are O(log(n))",
        "Both SLLdel and DLLdel are O(1)",
        "SLLdel is O(n) and DLLdel is O(1)"
    ],
    "answer": "Both SLLdel and DLLdel are O(1)"
},
{
    "question": "Consider the Deterministic Finite-state Automaton (DFA) shown below. The DFA runs on the alphabet {0, 1}, and has the set of states {s, p, q, r}, with s being the start state and p being the only final state. Which one of the following regular expressions correctly describes the language accepted by the DFA?",
    "options": [
        "1(0*11)1(0*11)",
        "0(0+1)0(0+1)",
        "1(0+11)1(0+11)",
        "1(110*)1(110)*"
    ],
    "answer": "1(0*11)1(0*11)"
},
{
    "question": "The Lucas sequence Ln is defined by the recurrence relation: Ln = Ln-1 + Ln-2, for n ≥ 3, with L1 = 1 and L2 = 3. Which one of the options given is TRUE?",
    "options": [
        "Ln = (1+√5/2)^n + (1-√5/2)^n",
        "Ln = (1+√5/2)^n - (1-√5/3)^n",
        "Ln = (1+√5/2)^n + (1-√5/3)^n",
        "Ln = (1+√5/2)^n - (1-√5/2)^n"
    ],
    "answer": "Ln = (1+√5/2)^n + (1-√5/2)^n"
},
{
    "question": "Which one of the options given below refers to the degree (or arity) of a relation in relational database systems?",
    "options": [
        "Number of attributes of its relation schema.",
        "Number of tuples stored in the relation.",
        "Number of entries in the relation.",
        "Number of distinct domains of its relation schema."
    ],
    "answer": "Number of attributes of its relation schema."
},
{
    "question": "Suppose two hosts are connected by a point-to-point link and they are configured to use Stop-and-Wait protocol for reliable data transfer. Identify in which one of the following scenarios, the utilization of the link is the lowest.",
    "options": [
        "Longer link length and lower transmission rate",
        "Longer link length and higher transmission rate",
        "Shorter link length and lower transmission rate",
        "Shorter link length and higher transmission rate"
    ],
    "answer":  "Longer link length and lower transmission rate"
},
{
    "question": "Let A = [[1, 2, 3, 4], [4, 1, 2, 3], [3, 4, 1, 2], [2, 3, 4, 1]] and B = [[3, 4, 1, 2], [4, 1, 2, 3], [1, 2, 3, 4], [2, 3, 4, 1]]. Let det(A) and det(B) denote the determinants of the matrices A and B, respectively. Which one of the options given below is TRUE?",
    "options": [
        "det(A) = det(B)",
        "det(B) = - det(A)",
        "det(A)=0",
        "det(AB) = det(A) + det(B)"
    ],
    "answer": "det(B) = - det(A)"
},
{
    "question": "An algorithm has to store several keys generated by an adversary in a hash table. The adversary is malicious who tries to maximize the number of collisions. Let k be the number of keys, m be the number of slots in the hash table, and k > m. Which one of the following is the best hashing strategy to counteract the adversary?",
    "options": [
        "Division method, i.e., use the hash function h(k)=kmodm",
        "Multiplication method, i.e., use the hash function h(k)=⌊m(kA−⌊kA⌋)⌋, where A is a carefully chosen constant.",
        "Universal hashing method.",
        "If k is a prime number, use Division method. Otherwise, use Multiplication method"
    ],
    "answer": "Universal hashing method."
},
{
    "question": "The output of a 2-input multiplexer is connected back to one of its inputs as shown in the figure.",
    "options": [
        "D Flip-flop",
        "D Latch",
        "Half-adder",
        "Demultiplexer"
    ],
    "answer": "D Latch"
},
{
    "question": "Describe the use of pipelining in modern processors.",
    "options": [
        "To store data in cache",
        "To fetch instructions one at a time",
        "To execute multiple instructions simultaneously",
        "To increase memory access speed"
    ],
    "answer": "To execute multiple instructions simultaneously"
},
{
    "question": "What is the 2's complement representation of -7 in 4-bit binary?",
    "options": [
        "1001",
        "0111",
        "1111",
        "1000"
    ],
    "answer": "1001"
},
{
    "question": "Which of the following matrix properties is true for any two square matrices A and B of the same size?",
    "options": [
        "det(AB) = det(A) * det(B)",
        "(A + B)^2 = A^2 + 2AB + B^2",
        "(AB)^T = A^T * B^T",
        "A^2 - B^2 = (A + B)(A - B)"
    ],
     "answer": "det(AB) = det(A) * det(B)"
  },
  {
    "question": "Which of the following is a necessary condition for deadlock?",
    "options": [
        "Mutual exclusion",
        "Hold and wait",
        "No preemption",
        "Circular wait"
    ],
    "answer": "Circular wait"
},
{
    "question": "Which of the following is NOT a property of a group?",
    "options": [
        "Closure",
        "Associativity",
        "Commutativity",
        "Identity element"
    ],
    "answer": "Commutativity"
},
{
    "question": "In a complete binary tree with n nodes, the number of leaf nodes is:",
    "options": [
        "n/2",
        "(n+1)/2",
        "n/2 + 1",
        "(n-1)/2"
    ],
    "answer": "(n+1)/2"
},
{
    "question": "What is the time complexity of finding the minimum element in a min-heap?",
    "options": [
        "O(1)",
        "O(log n)",
        "O(n)",
        "O(n log n)"
    ],
    "answer": "O(1)"
},
{
    "question": "In a graph with n vertices, the maximum number of edges in a simple undirected graph is:",
    "options": [
        "n(n-1)/2",
        "n^2",
        "n(n+1)/2",
        "n-1"
    ],
    "answer": "n(n-1)/2"
},
{
  "question": "What is the time complexity of linear search in the worst case?",
  "options": [
      "O(1)",
      "O(log n)",
      "O(n)",
      "O(n log n)"
  ],
  "answer": "O(n)"
},
{
  "question": "Which data structure is best suited for implementing a priority queue?",
  "options": [
      "Linked List",
      "Array",
      "Heap",
      "Stack"
  ],
  "answer": "Heap"
},
{
  "question": "Given a relational database with the following four schemas and their respective instances, what is the number of rows returned by the following SQL query?\n\n[SQL query]",
  "options": [
      "0",
      "1",
      "2",
      "More than 2"
  ],
  "answer": "0"
}

    ],

    
    "medium": [
        {
  "question": "Explain Merge Sort.",
  "options": [
      "A sorting algorithm using bubble swaps",
      "A divide and conquer sorting technique",
      "An iterative sorting algorithm",
      "A heuristic-based sorting algorithm"
  ],
  "answer": "A divide and conquer sorting technique"
},
{
  "question": "What is the time complexity of Binary Search?",
  "options": [
      "O(n)",
      "O(log n)",
      "O(n^2)",
      "O(n log n)"
  ],
  "answer": "O(log n)"
},
{
  "question": "Which one of the following statements is FALSE?",
  "options": [
    "In the cycle stealing mode of DMA, one word of data is transferred between an I/O device and main memory in a stolen cycle",
    "For bulk data transfer, the burst mode of DMA has a higher throughput than the cycle stealing mode",
    "Programmed I/O mechanism has a better CPU utilization than the interrupt driven I/O mechanism",
    "The CPU can start executing an interrupt service routine faster with vectored interrupts than with non-vectored interrupts"
  ],
  "answer": "Programmed I/O mechanism has a better CPU utilization than the interrupt driven I/O mechanism"
},
{
  "question": "Consider a memory management system that uses a page size of 2 KB. Assume that both the physical and virtual addresses start from 0. Assume that the pages 0, 1, 2, and 3 are stored in the page frames 1, 3, 2, and 0, respectively. The physical address (in decimal format) corresponding to the virtual address 2500 (in decimal format) is __",
  "options": [
    "512",
    "1024",
    "2048",
    "4096"
  ],
  "answer": "1024"
},
{
  "question": "Consider the following two regular expressions over the alphabet {0,1}: r = 0* + 1* s = 01* + 10* The total number of strings of length less than or equal to 5, which are neither in r nor in s, is __",
  "options": [
    "10",
    "11",
    "12",
    "13"
  ],
  "answer": "11"
},
{
  "question": "Let G = (V, E) be an undirected graph with |V| = n and |E| = m. What is the worst-case time complexity of a depth-first search (DFS) algorithm on G?",
  "options": [
    "O(n)",
    "O(m)",
    "O(n + m)",
    "O(nm)"
  ],
  "answer": "O(n + m)"
},
{
  "question": "Consider a binary search tree T. The in-order traversal of T yields the sorted sequence 1, 2, 3, ..., n. Which of the following traversals of T will also yield a sorted sequence?",
  "options": [
    "Preorder",
    "Postorder",
    "Level order",
    "None of the above"
  ],
  "answer": "None of the above"
},
{
    "question": "Consider a disk with a rotational speed of 7200 RPM and an average seek time of 10 milliseconds. The disk has 2000 tracks, and each track has 512 sectors. The average transfer time per sector is 0.2 milliseconds. The average time taken for reading a random sector on the disk is approximately:",
    "options": [
      "12.2 milliseconds",
      "15.4 milliseconds",
      "18.6 milliseconds",
      "21.8 milliseconds"
      ],
  "answer": "18.6 milliseconds"
},
{
"question": "Consider a cache memory with a block size of 4 words. The cache can hold a total of 32 words. Assuming a direct-mapped cache organization, the number of tag bits required is",
  "options": [
      "5",
      "6",
      "7",
      "8"
    ],
  "answer": "5"
},
{
  "question": "Given an integer array of size N, we want to check if the array is sorted (in either ascending or descending order). An algorithm solves this problem by making a single pass through the array and comparing each element of the array only with its adjacent elements. The worst-case time complexity of this algorithm is",
  "options": [
    "both O(N) and Ω(N)",
    "O(N) but not Ω(N)",
    "Ω(N) but not O(N)",
    "neither O(N) nor Ω(N)"
  ],
  "answer": "both O(N) and Ω(N)"
},
{
  "question": "Consider the following C program:\nc\n#include <stdio.h>\nvoid fX();\nint main() {\n    fX();\n    return 0;\n}\nvoid fX() {\n    char a;\n    if((a=getchar()) != '\\n') fX();\n    if(a != '\\n') putchar(a);\n}\n\nAssume that the input to the program from the command line is 1234 followed by a newline character. Which one of the following statements is CORRECT?",
  "options": [
    "The program will not terminate",
    "The program will terminate with no output",
    "The program will terminate with 4321 as output",
    "The program will terminate with 1234 as output"
  ],
  "answer": "The program will terminate with 4321 as output"
},
{
  "question": "The product of all eigenvalues of the matrix [1 2 3; 4 5 6; 7 8 9] is:",
  "options": [
    "-1",
    "0",
    "1",
    "2"
  ],
  "answer": "0"
},
{
  "question": "A user starts browsing a webpage hosted at a remote server. The browser opens a single TCP connection to fetch the entire webpage from the server. The webpage consists of a top-level index page with multiple embedded image objects. Assume that all caches (e.g., DNS cache, browser cache) are all initially empty. The following packets leave the user's computer in some order.\n(i) HTTP GET request for the index page\n(ii) DNS request to resolve the web server's name to its IP address\n(iii) HTTP GET request for an image object\n(iv) TCP SYN to open a connection to the web server\nWhich one of the following is the CORRECT chronological order (earliest in time to latest) of the packets leaving the computer?",
  "options": [
    "(iv), (ii), (iii), (i)",
    "(ii), (iv), (iii), (i)",
    "(ii), (iv), (i), (iii)",
    "(iv), (ii), (i), (iii)"
  ],
  "answer": "(ii), (iv), (i), (iii)"
},
{
  "question": "Given an integer array of size N, we want to check if the array is sorted (in either ascending or descending order). An algorithm solves this problem by making a single pass through the array and comparing each element of the array only with its adjacent elements. The worst-case time complexity of this algorithm is",
  "options": [
    "both O(N) and Ω(N)",
    "O(N) but not Ω(N)",
    "Ω(N) but not O(N)",
    "neither O(N) nor Ω(N)"
  ],
  "answer": "both O(N) and Ω(N)"
},
{
  "question": "A computer system uses 32-bit virtual addresses and 32-bit physical addresses. The page size is 4 KB. The size of the page table for each process is",
  "options": [
    "4 MB",
    "8 MB",
    "16 MB",
    "32 MB"
  ],
  "answer": "4 MB"
},
{
  "question": "Which of the following is NOT a characteristic of a process?",
  "options": [
    "Program counter",
    "Stack",
    "Data segment",
    "Open files"
  ],
  "answer": "Open files"
},
{
  "question": "A critical section is a piece of code that:",
  "options": [
    "Must be executed atomically",
    "Must be executed by at most one process at a time",
    "Must be executed by all processes",
    "Must be executed exactly once by each process"
  ],
  "answer": "Must be executed by at most one process at a time"
},
{
  "question": "Consider a disk with 1000 cylinders. The current position of the disk arm is cylinder number 500. The next request to be serviced is at cylinder number 140. The disk arm moves at a speed of 100 cylinders per millisecond. The seek time for this request is",
  "options": [
    "3.6 milliseconds",
    "4.0 milliseconds",
    "3.4 milliseconds",
    "4.4 milliseconds"
  ],
  "answer": "3.6 milliseconds"
},
{
  "question": "Which of the following is a correct regular expression for the language of all strings over {a, b} that contain at least two consecutive a's?",
  "options": [
    "(a+b)aa(a+b)",
    "(a+b)aa(a+b)*a",
    "(a+b)aa(a+b)*b",
    "(a+b)aa(a+b)*a*b"
  ],
  "answer": "(a+b)aa(a+b)"
},
{
  "question": "A Turing machine (TM) is a mathematical model of computation that manipulates symbols on a strip of tape according to a table of rules. Which of the following statements is TRUE about Turing machines?",
  "options": [
    "All Turing machines halt for all input strings.",
    "There exists a Turing machine that can decide the halting problem.",
    "Turing machines can recognize all recursively enumerable languages.",
    "Turing machines are limited to finite memory."
  ],
  "answer": "Turing machines can recognize all recursively enumerable languages."
},
{
  "question": "A context-free grammar (CFG) is a formal grammar that defines a context-free language. Which of the following is NOT a characteristic of a CFG?",
  "options": [
    "It consists of a finite set of production rules.",
    "Each production rule has a non-terminal symbol on the left-hand side.",
    "The right-hand side of a production rule can contain only terminal symbols.",
    "The right-hand side of a production rule can contain both terminal and non-terminal symbols."
  ],
  "answer": "The right-hand side of a production rule can contain only terminal symbols."
},
{
  "question": "A finite automaton (FA) is a mathematical model of a computational device that accepts or rejects a given input string. Which of the following is NOT a component of a finite automaton?",
  "options": [
    "A finite set of states",
    "A finite set of input symbols",
    "A transition function",
    "A stack"
  ],
  "answer": "A stack"
},
{
  "question": "Consider a graph G with n vertices and m edges. A depth-first search (DFS) algorithm is performed on G. The worst-case time complexity of the DFS algorithm is:",
  "options": [
    "O(n)",
    "O(m)",
    "O(n + m)",
    "O(nm)"
  ],
  "answer": "O(n + m)"
},
{
  "question": "Consider a binary search tree (BST) is a binary tree with the following properties:\n* The left subtree of a node contains only nodes with keys less than the node's key.\n* The right subtree of a node contains only nodes with keys greater than the node's key.\n* Both the left and right subtrees must also be binary search trees.\nGiven a BST, which of the following traversals will always output the keys in sorted order?",
  "options": [
    "Preorder",
    "Inorder",
    "Postorder",
    "Level order"
  ],
  "answer": "Inorder"
},
{
  "question": "Which one of the following options is a CORRECT replacement for operands in the position (U1, U2, U3, U4) in the above assembly code?",
  "options": [
      "(8, 4, 1, Lo2)",
      "(3, 4, 4, Lo1)",
      "(8, 1, 1, Lo2)",
      "(3, 1, 1, Lo1)"
  ],
  "answer": "(8, 1, 1, Lo2)"
},
{
  "question": "The input memory addresses (IA11-IA0), in decimal, for the starting locations (Addr=0) of each block (indicated as X1, X2, X3, X4 in the figure) are among the options given below. Which one of the following options is CORRECT?",
  "options": [
      "(0, 1, 2, 3)",
      "(0, 1024, 2048, 3072)",
      "(0, 8, 16, 24)",
      "(0, 0, 0, 0)"
  ],
  "answer": "(0, 1024, 2048, 3072)"
},
{
  "question": "Which one of the given values of (Q1, Q2, Q3) can NEVER be obtained with this digital circuit?",
  "options": [
      "(0, 0, 1)",
      "(1, 0, 0)",
      "(1, 0, 1)",
      "(1, 1, 1)"
  ],
  "answer": "(1, 1, 1)"
},
{
  "question": "Which one of the following set of values of (X0, X1, X2, X3, X4, X5, X6, X7) will realise the Boolean function Aˉ+Aˉ⋅Cˉ+A⋅Bˉ⋅C?",
  "options": [
      "(1, 1, 0, 0, 1, 1, 1, 0)",
      "(1, 1, 0, 0, 1, 1, 0, 1)",
      "(1, 1, 0, 1, 1, 1, 0, 0)",
      "(0, 0, 1, 1, 0, 1, 1, 1)"
  ],
  "answer": "(1, 1, 0, 0, 1, 1, 1, 0)"
},
{
  "question": "Which one of the following corresponds to the product of these numbers (i.e., P x Q), represented in the IEEE-754 single precision format?",
  "options": [
      "0x404C2EF4",
      "0x405C2EF4",
      "0xC15C2EF4",
      "0xC14C2EF4"
  ],
  "answer": "0x405C2EF4"
},
{
  "question": "When A contains n elements, which one of the following statements about the worst case running time of these two operations is TRUE?",
  "options": [
      "Both Extract-Max(A) and Insert(A,key) run in O(1).",
      "Both Extract-Max(A) and Insert(A,key) run in O(log(n)).",
      "Extract-Max(A) runs in O(1) whereas Insert(A,key) runs in O(n).",
      "Extract-Max(A) runs in O(1) whereas Insert(A,key) runs in O(log(n))."
  ],
  "answer": "Both Extract-Max(A) and Insert(A,key) run in O(log(n))."
},
{
  "question": "When foo is called with a pointer to the root node of the given binary tree, what will it print?",
  "options": [
      "3 8 5 13 11 10",
      "3 5 8 10 11 13",
      "3 8 16 13 24 50",
      "3 16 8 50 24 13"
  ],
  "answer": "C"
},
{
  "question": "How many permutations of U separate A from B?",
  "options": [
      "n!",
      "(n choose 2k) * (n-2k)!",
      "(n choose 2k) * (n-2k)! * (k!)^2",
      "2 * (n choose 2k) * (n-2k)! * (k!)^2"
  ],
  "answer": "D"
},
{
  "question": "What is the time complexity of the following Python code?\npython\ndef linear_search(arr, x):\n    for i in range(len(arr)):\n        if arr[i] == x:\n            return i\n    return -1\n",
  "options": [
      "O(1)",
      "O(log n)",
      "O(n)",
      "O(n^2)"
  ],
  "answer": "O(n)"
},
{
  "question": "Explain the difference between a list and a tuple in Python.",
  "options": [
      "Lists are mutable, tuples are immutable",
      "Lists are ordered, tuples are unordered",
      "Lists can store different data types, tuples can only store one data type",
      "Lists are faster than tuples"
  ],
  "answer": "Lists are mutable, tuples are immutable"
},
{
  "question": "How do you define a function in Python?",
  "options": [
      "Using the def keyword",
      "Using the function keyword",
      "Using the procedure keyword",
      "Using the method keyword"
  ],
  "answer": "Using the def keyword"
},
{
  "question": "Consider a complete binary tree. What is the maximum number of nodes at level i (root is level 0)?",
  "options": [
      "2^i",
      "2^(i-1)",
      "2^(i+1)",
      "2^i - 1"
  ],
  "answer": "2^i"
},
{
  "question": "What is the time complexity of the merge sort algorithm?",
  "options":[ 
      "O(n)",
      "O(n log n)",
      "O(n^2)",
      "O(2^n)"
  ],
  "answer": "O(n log n)"
},

    ],

    "hard": [
        {
  "question": "Explain Turing Machines.",
  "options": [
      "A physical machine for arithmetic",
      "A conceptual computing model",
      "A machine for sorting algorithms",
      "A cryptographic tool"
  ],
  "answer": "A conceptual computing model"
},
{
  "question": "The value of the definite integral ∫(from -3 to 3) ∫(from -2 to 2) ∫(from -1 to 1) (4x^2y - z^3) dz dy dx is?",
  "options": [
      "288",
      "0",
      "-288",
      "144"
  ],
  "answer": "288"
},
{
  "question": "Consider a digital logic circuit consisting of three 2-to-1 multiplexers M1, M2, and M3 as shown below. X1 and X2 are inputs of M1. X3 and X4 are inputs of M2. A, B, and C are select lines of M1, M2, and M3, respectively. For an instance of inputs X1=X2=1, X3=0, and X4=0, the number of combinations of A, B, C that give the output Y=1 is ___",
  "options": [
    "2",
    "3",
    "4",
    "5"
  ],
  "answer": "4"
},
{
  "question": "Consider sending an IP datagram of size 1420 bytes (including 20 bytes of IP header) from a sender to a receiver over a path of two links with a router between them. The first link (sender to router) has an MTU (Maximum Transmission Unit) size of 542 bytes, while the second link (router to receiver) has an MTU size of 360 bytes. The number of fragments that would be delivered at the receiver is ___",
  "options": [
    "3",
    "4",
    "5",
    "6"
  ],
  "answer": "6"
},
{
  "question": "The number of edges present in the forest generated by the DFS traversal of an undirected graph G with 100 vertices is 40. The number of connected components in G is __",
  "options": [
    "60",
    "61",
    "62",
    "63"
  ],
  "answer": "61"
},
{
  "question": "The value of the definite integral ∫(from -3 to 3) ∫(from -2 to 2) ∫(from -1 to 1) (4x^2y - z^3) dz dy dx is ___. (Rounded off to the nearest integer)",
  "options": [
    "288",
    "0",
    "-288",
    "144"
  ],
  "answer": "288"
},
{
  "question": "Which one of the following regular expressions correctly represents the language of the finite automaton given below?",
  "options": [
      "ab*bab* + ba*aba*",
      "(ab*b)ab + (ba*a)ba",
      "(ab*b + ba*a)(a + b*)",
      "(ba*a + ab*b)(ab + ba*)"
  ],
  "answer": "(ab*b + ba*a)(a + b*)"
},
{
  "question": "Which one of the following statements is TRUE?",
  "options": [
      "The LALR(1) parser for a grammar G cannot have reduce-reduce conflict if the LR(1) parser for G does not have reduce-reduce conflict.",
      "Symbol table is accessed only during the lexical analysis phase.",
      "Data flow analysis is necessary for run-time memory management.",
      "LR(1) parsing is sufficient for deterministic context-free languages."
  ],
  "answer": "The LALR(1) parser for a grammar G cannot have reduce-reduce conflict if the LR(1) parser for G does not have reduce-reduce conflict."
},
{
  "question": "In a relational data model, which one of the following statements is TRUE?",
  "options": [
      "A relation with only two attributes is always in BCNF.",
      "If all attributes of a relation are prime attributes, then the relation is in BCNF.",
      "Every relation has at least one non-prime attribute.",
      "BCNF decompositions preserve functional dependencies."
  ],
  "answer": "BCNF decompositions preserve functional dependencies."
},
{
  "question": "Consider the problem of reversing a singly linked list. To take an example, given the linked list below,\n\n[attachment_0](attachment)\n\nthe reversed linked list should look like\n\n[attachment_1](attachment)\n\nWhich one of the following statements is TRUE about the time complexity of algorithms that solve the above problem in O(1) space?",
  "options": [
      "The best algorithm for the problem takes θ(n) time in the worst case.",
      "The best algorithm for the problem takes θ(nlogn) time in the worst case.",
      "The best algorithm for the problem takes θ(n^2) time in the worst case.",
      "It is not possible to reverse a singly linked list in O(1) space."
  ],
  "answer": "The best algorithm for the problem takes θ(n) time in the worst case."
},
{
  "question": "What is the output of the following Python code?\npython\ndef factorial(n):\n    if n == 0:\n        return 1\n    else:\n        return n * factorial(n - 1)\n\nprint(factorial(5))\n",
  "options": [
      "120",
      "24",
      "60",
      "10"
  ],
  "answer": "120"
},
{
  "question": "Explain the concept of inheritance in Python.",
  "options": [
      "A way to create new classes from existing ones",
      "A way to hide data from other parts of the program",
      "A way to create multiple instances of the same class",
      "A way to pass arguments to a function"
  ],
  "answer": "A way to create new classes from existing ones"
},
{
  "question": "What is the difference between a shallow copy and a deep copy in Python?",
  "options": [
      "Shallow copies create new objects, deep copies create references to existing objects",
      "Shallow copies create references to existing objects, deep copies create new objects",
      "Shallow copies are faster than deep copies",
      "Deep copies are faster than shallow copies"
  ],
  "answer": "Shallow copies create references to existing objects, deep copies create new objects"
}

    ]
}

@app.route('/api/getQuestions', methods=['GET'])
def get_questions():
    # Get the difficulty level from query parameters
    difficulty = request.args.get('difficulty', '').lower()

    # Validate difficulty level
    if difficulty not in questions_db:
        return jsonify({"error": "Invalid difficulty level. Choose from 'easy', 'medium', or 'hard'."}), 400

    # Fetch questions based on difficulty
    questions = questions_db[difficulty]

    # Respond with questions
    return jsonify({"difficulty": difficulty, "questions": questions})

if __name__ == '__main__':
    app.run(debug=True)
