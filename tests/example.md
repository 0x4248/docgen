# Test file for docgen.
description: This is a test file for docgen.

file: test.c

version: 1.0

author: John Doe

date: 2012-01-01

license: GPL

see: http://www.gnu.org/licenses/gpl.html

```c
#include <stdio.h>
```
## Test function.
description: This is a test function.

### Parameters
* a: This is a test parameter.
* b: This is a test parameter.
### Return value
This is a test return value.
```c
int test(int a, int b)
```
## Main function.
description: This is a main function.

* argc: This is a test parameter.
* argv: This is a test parameter.
### Return value
This is a test return value.
```c
int main(int argc, char *argv[])
```