import java.math.BigInteger;


class Puzzle {

    final static BigInteger M = new BigInteger("2017");
    
    private static BigInteger compute(long n) {
    String s = "";
    for (long i = 0; i < n; i++) {
    s = s + n;
    }
    
    return new BigInteger(s.toString()).mod(M);
    }
    // 58184241583791680L
    public static void main(String args[]) {
    for (long n : new long[] {1L, 2L, 5L, 10L, 20L, 58184241583791680L }) {
    System.out.println("" + n + ": " + compute(n));

    }
    }
    
    }