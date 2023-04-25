import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.StreamTokenizer;
import java.io.IOException;

public class problem1881 {

    public static void main(String[] args) throws IOException {

        BufferedReader in2 = new BufferedReader(new InputStreamReader(System.in));
        StreamTokenizer in = new StreamTokenizer(in2);

        int h, w, n;

        in.nextToken();
        h = (int) in.nval;
        in.nextToken();
        w = (int) in.nval;
        in.nextToken();
        n = (int) in.nval;
        in2.readLine(); //BEZ ETOI STROCHKI WA#4

        int pageCounter = 1;
        int lineCounter = 1;
        int symbolsCounter = 0;
        int l;

        for (int i = 0; i < n; i++) {
            l = in2.readLine().length();
            if (symbolsCounter + l <= w) {
                symbolsCounter += (l + 1);
            } else if (lineCounter + 1 <= h) {
                lineCounter++;
                symbolsCounter = l + 1;
            } else {
                pageCounter++;
                lineCounter = 1;
                symbolsCounter = l + 1;
            }
        }
        System.out.print(pageCounter);
    }
}