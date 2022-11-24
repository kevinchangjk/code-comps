import java.io.*;
import java.util.*;

public final class P1680B {
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

  private int t;

  private P1680B(int t) {
    this.t = t;
  }

  private String[] solve() {
    class TestCase {
      private int rows;
      private int cols;
      private ArrayList<Integer[]> robots = new ArrayList<>();
      private int closest;

      public TestCase(int rows, int cols) {
        int count = 0;
        int closestDistance = Integer.MAX_VALUE;
        this.rows = rows;
        this.cols = cols;
        for (int i = 0; i < this.rows; i++) {
          String row = P1680B.sc.nextLine();
          for (int j = 0; j < this.cols; j++) {
            if (row.charAt(j) == 'R') {
              Integer[] robot = {i, j};
              this.robots.add(robot);
              int distance = i + j;
              if (distance < closestDistance) {
                closestDistance = distance;
                closest = count;
              }
              count++;
            }
          }
        }
      }

      public String solve() {
        Integer[] closestRobot = robots.get(this.closest);
        int up = closestRobot[0];
        int left = closestRobot[1];
        for (Integer[] robot : robots) {
          if (up > robot[0] || left > robot[1]) {
            return "NO";
          }
        }

        return "YES";
      }
    }


    String[] res = new String[this.t];
    for (int i = 0; i < this.t; i++) {
      int rows = P1680B.sc.nextInt();
      int cols = P1680B.sc.nextInt();
      TestCase curr = new TestCase(rows, cols);
      res[i] = curr.solve();
    }

    return res;
  }

  public static void main(String[] args) {
    sc = new MyScanner();
    out = new PrintWriter(new BufferedOutputStream(System.out));

    int t = sc.nextInt();
    P1680B problem = new P1680B(t);
    String[] res = problem.solve();
    for (int i = 0; i < t; i++) {
      out.println(res[i]);
    }
    out.close();
  }
}
