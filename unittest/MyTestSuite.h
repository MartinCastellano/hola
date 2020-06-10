#include <cxxtest/TestSuite.h>


    // cxxtestgen --error-printer -o tests.cpp MyTestSuite.h
    // g++ -o main tests.cpp
    // ./main

  class MyTestSuite : public CxxTest::TestSuite
  {
  public:
      void testAddition( void )
      {
          TS_ASSERT( 1 + 1 > 1 );
          TS_ASSERT_EQUALS( 1 + 1, 2 );
      }
  };
