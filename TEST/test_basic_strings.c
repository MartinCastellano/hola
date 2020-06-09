#include "test_macros.h"

void test_some_strings()
{
    char *foo = "This is foo";
    char *bar = "This is bar";

    ASSERT_EQUAL_STR(foo, foo);
    ASSERT_EQUAL_STR(foo, bar);
}

int main()
{
    test_some_strings();

    return 0;
}