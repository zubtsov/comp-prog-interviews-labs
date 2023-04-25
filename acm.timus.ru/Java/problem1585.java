
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.StreamTokenizer;
import java.io.IOException;

public class problem1585 {

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new BufferedReader(new InputStreamReader(System.in)));
        StreamTokenizer st = new StreamTokenizer(in);

        st.nextToken();
        int N = (int) st.nval;
        int[] a = new int[3];
        in.readLine(); //bez etogo WA#3

        for (int i = 0; i < N; i++) {
            switch (in.read()) {
                case (int) 'E':
                    a[0]++;
                    break;
                case (int) 'L':
                    a[1]++;
                    break;
                case (int) 'M':
                    a[2]++;
                    break;
            }
            in.readLine();
        }
        int max = Math.max(Math.max(a[0], a[1]), a[2]);
        if (max == a[0]) {
            System.out.print("Emperor Penguin");
        } else if (max == a[1]) {
            System.out.print("Little Penguin");
        } else {
            System.out.print("Macaroni Penguin");
        }
    }
}
