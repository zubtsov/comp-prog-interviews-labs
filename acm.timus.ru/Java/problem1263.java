
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.StreamTokenizer;
import java.io.IOException;

public class problem1263 {

    public static void main(String[] args) throws IOException {
        StreamTokenizer in = new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));

        int N, M;
        in.nextToken();
        N = (int) in.nval;
        in.nextToken();
        M = (int) in.nval;

        int[] a = new int[N];
        for (int i = 0; i < M; i++) {
            in.nextToken();
            a[((int) in.nval)-1]++;
        }
        for (int i = 0; i < N; i++) {
            System.out.print(String.format("%.2f%%\n", a[i]*100.0/M)); //use DecimalFormat
        }
    }
}