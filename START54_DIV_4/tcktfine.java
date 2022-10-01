import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Codechef {
    public static void main(String[] args) throws java.lang.Exception {
        // your code goes here
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while (t != 0) {
            int x = 0, p = 0, q = 0;
            x = sc.nextInt();
            p = sc.nextInt();
            q = sc.nextInt();
            System.out.println(x * (p - q));
            t--;
        }
        sc.close();
    }
}
