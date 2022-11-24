/**
 * Template class for Codeforces problems.
 * Written by @kevinchangjk
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.StringTokenizer;

class Template {
    // io class
    static class FastScanner {
        private BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        private StringTokenizer st = new StringTokenizer("");

        public String next() {
            while (!st.hasMoreTokens()) {
                try {
                    st = new StringTokenizer(br.readLine());				               
                } catch (IOException e) {}
                return st.nextToken();
            }
            return null;
        }
        
        public int nextInt() {
            return Integer.parseInt(next());
        }

        public long nextLong() {
            return Long.parseLong(next());
        }
    }

    // solution
    private static void solve(FastScanner sc, PrintWriter out) {
        int num = sc.nextInt();
        out.println(num);
    }

    public static void main(String[] args) {
        FastScanner sc = new Template.FastScanner();
        PrintWriter out = new PrintWriter(System.out);
        int tc = sc.nextInt();

        // solving for every test case
        for (int i = 0; i < tc; i++) {
            solve(sc, out);
        }

        // flush all output
        out.close();
    }
}
