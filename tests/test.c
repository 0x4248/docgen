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