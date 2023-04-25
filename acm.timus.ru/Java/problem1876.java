
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.StreamTokenizer;
import java.io.IOException;

public class problem1876 {

    public static void main(String[] args) throws IOException {
        StreamTokenizer in = new StreamTokenizer(new BufferedReader(new BufferedReader(new InputStreamReader(System.in))));

        in.nextToken();
        int a = (int) in.nval;
        in.nextToken();
        int b = (int) in.nval;

        if (2*a-1 > 2*b) {
            System.out.print(40 + 2*a-1);
        } else {
            System.out.print(40+2*b);
        }
    }
}
