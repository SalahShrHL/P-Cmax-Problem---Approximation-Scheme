# P||Cmax Problem - Approximation Scheme

This project focuses on an approximation scheme for the P||Cmax problem, also known as the makespan minimization problem. This problem is widely studied in operational research and algorithmic complexity theory.

## Description

The P||Cmax problem is a scheduling problem where the goal is to minimize the maximum completion time (makespan) of a set of tasks scheduled on parallel resources.

This Python script uses an approximation scheme to schedule tasks on parallel machines, aiming to minimize the maximum completion time. It first schedules the 10 tasks with the longest processing times using a permutation method, then schedules the remaining tasks using the Longest Processing Time (LPT) rule.

The results, including the schedule and the maximum completion time (Cmax), are written to a file named "Ordononcement.txt".
