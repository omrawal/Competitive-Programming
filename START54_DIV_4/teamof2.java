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
            boolean flag = false;
            int n = sc.nextInt();
            ArrayList<ArrayList<Integer>> mat = new ArrayList<ArrayList<Integer>>();
            for (int i = 0; i < n; i++) {
                ArrayList<Integer> lst = new ArrayList<>();
                int count = sc.nextInt();
                lst.add(count);
                for (int j = 0; j < count; j++) {
                    lst.add(sc.nextInt());
                }
                mat.add(lst);
            }
            for (int i = 0; i < mat.size(); i++) {
                for (int j = i + 1; j < mat.size(); j++) {
                    if (mat.get(i).get(0) + mat.get(j).get(0) >= 5) {
                        boolean[] count = { false, false, false, false, false };
                        for (int k = 1; k <= mat.get(i).get(0); k++) {
                            int index = mat.get(i).get(k);
                            count[index - 1] = true;
                        }
                        for (int k = 1; k <= mat.get(j).get(0); k++) {
                            int index = mat.get(j).get(k);
                            count[index - 1] = true;
                        }
                        if (Arrays.equals(count, new boolean[] { true, true, true, true, true })) {
                            System.out.println("YES");
                            flag = true;
                            break;
                        }
                    }
                }
                if (flag)
                    break;
            }
            if (!flag)
                System.out.println("NO");

            t--;
        }
        sc.close();
    }
}
