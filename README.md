# Docgen

A simple script to generate markdown documentation from C source code

## Usage
The program takes a single argument, the path to the input file. The generated documentation will be printed to stdout.

```
python3 main.py <input file>
```

If you want to write the output to a file you can run.

```
python3 main.py <input file> > <output file>
```

## Example
The following example shows the input file and the generated documentation.
```c
/**
 * Test file for docgen.
 * @description: This is a test file for docgen.
 * @file: test.c
 * @version: 1.0
 * @author: John Doe
 * @date: 2012-01-01
 * @license: GPL
 * @see: http://www.gnu.org/licenses/gpl.html
*/

#include <stdio.h>
#include <stdlib.h>

/**
 * Test function.
 * @description: This is a test function.
 * @param: a: This is a test parameter.
 * @param: b: This is a test parameter.
 * @return: This is a test return value.
*/
int test(int a, int b)
{
    return a + b;
}

/**
 * Main function.
 * @description: This is a main function.
 * @param: argc: This is a test parameter.
 * @param: argv: This is a test parameter.
 * @return: This is a test return value.
*/
int main(int argc, char *argv[])
{
    int a = 1;
    int b = 2;
    int c = test(a, b);
    printf("c = %d", c);
    return 0;
}
```

````markdown
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
````

## License
This project is licensed under the GPL-3.0 License - see the [LICENCE](LICENCE) file for details.