# Week 1 — C Cheatsheet

## Compile & Run
```bash
make filename          # Compile (CS50 IDE)
clang -o out file.c    # Compile manually
./out                  # Run
```

## Data Types
```c
int     x = 10;
long    y = 1000000L;
float   f = 3.14f;
double  d = 3.14159265;
char    c = 'A';
bool    b = true;       // #include <stdbool.h>
string  s = "hello";    // CS50 library
```

## printf Format Specifiers
```c
%i  %d   // int
%f       // float/double
%c       // char
%s       // string
%li      // long
%.2f     // float with 2 decimal places
```

## Control Flow
```c
if (x > 0) { }
else if (x < 0) { }
else { }

for (int i = 0; i < n; i++) { }
while (condition) { }
do { } while (condition);
```

## CS50 Input Functions
```c
get_int("Prompt: ")
get_float("Prompt: ")
get_string("Prompt: ")
get_long("Prompt: ")
get_char("Prompt: ")
```
