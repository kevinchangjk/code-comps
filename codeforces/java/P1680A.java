import java.io.*;
import java.util.*;

public final class P1680A {
  private int t;
  private int[][] inputs;

  private P1680A(int t) {
    this.t = t;
  }

  private int[] solve() {
    class TestCase {
      private int minLeft;
      private int minRight;
      private int maxLeft;
      private int maxRight;

      public TestCase(int[] input) {
        this.minLeft = input[0];
        this.minRight = input[1];
        this.maxLeft = input[2];
        this.maxRight = input[3];
      }

      public int solve() {
        if (this.minRight < this.maxLeft || this.maxRight < this.minLeft) {
          return this.minLeft + this.maxLeft;
        }
        return this.minLeft < this.maxLeft ? this.maxLeft : this.minLeft;
      }
    }

    int[] res = new int[this.t];
    for (int i = 0; i < this.t; i++) {
      int[] input = new int[4];
      for (int j = 0; j < 4; j++) {
        input[j] = P1680A.sc.nextInt();
      }
      TestCase curr = new TestCase(input);
      res[i] = curr.solve();
    }
    return res;
  }

  public static void main(String[] args) {
    sc = new MyScanner();
    out = new PrintWriter(new BufferedOutputStream(System.out));

    int t = sc.nextInt();
    P1680A main = new P1680A(t);
    int[] res = main.solve();
    for (int i = 0; i < t; i++) {
      out.println(res[i]);
    }
    out.close();
  }

  //-----------PrintWriter for faster output---------------------------------
  public static PrintWriter out;
  public static MyScanner sc;

  //-----------MyScanner class for faster input----------
  public static class MyScanner {
    BufferedReader br;
    StringTokenizer st;

    public MyScanner() {
      br = new BufferedReader(new InputStreamReader(System.in));
    }

    String next() {
      while (st == null || !st.hasMoreElements()) {
        try {
          st = new StringTokenizer(br.readLine());
        } catch (IOException e) {
          e.printStackTrace();
        }
      }
      return st.nextToken();
    }

    int nextInt() {
      return Integer.parseInt(next());
    }

    long nextLong() {
      return Long.parseLong(next());
    }

    double nextDouble() {
      return Double.parseDouble(next());
    }

    String nextLine(){
      String str = "";
      try {
        str = br.readLine();
      } catch (IOException e) {
        e.printStackTrace();
      }
      return str;
    }

  }
}
