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

    public static void main(String[] args) {
        FastScanner sc = new Template.FastScanner();
        PrintWriter out = new PrintWriter(System.out);
        int tc = sc.nextInt();

        // input reception: use with sc.next(), sc.nextInt(), sc.nextLong()

        // solution

        // output: use with out.println() then call the close() method at end
        for (int i = 0; i < tc; i++) {
            out.println(i);
        }
        out.close();
    }
}
