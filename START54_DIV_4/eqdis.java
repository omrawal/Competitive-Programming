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
            int n = sc.nextInt();
            int arr[] = new int[n];
            for (int i = 0; i < n; i++) {
                arr[i] = sc.nextInt();
            }
            HashSet<Integer> set = new HashSet<>();
            for (int i = 0; i < n; i++) {
                set.add(arr[i]);
            }
            int setSize = set.size();
            if (setSize % 2 == 0 || (setSize % 2 == 1 && setSize < n)) {
                System.out.println("YES");
            } else {
                System.out.println("NO");
            }

            t--;
        }
        sc.close();
    }
}
