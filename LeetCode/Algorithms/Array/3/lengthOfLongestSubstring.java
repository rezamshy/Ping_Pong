package A;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class lengthOfLongestSubstring {
    public static void main(String args []) {
        Scanner var = new Scanner(System.in);
        String s = var.next();
        System.out.println(s);
        Map <Character, Integer> m = new HashMap<>();
        int j = 0;
        int i = 0;
        int max = 0;
        while (i<s.length()){
            if(m.containsKey(s.charAt(i))){
                max = Math.max(max, i - j);
                i = m.get(s.charAt(i)) + 1;
                j = i;
                m.clear();
            }
            else{
                m.put(s.charAt(i), i);
                i++;
            }
        }
        System.out.println(max);
        var.close();
    }
}
