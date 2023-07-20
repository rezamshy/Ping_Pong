package LeetCode.Algorithms.Array;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class LongestSleep {
    private static Map<String, Integer> dayDic = new HashMap<String, Integer>();
    private static final int minutesInDay = 1440;
    private static final int minutesInHour = 60;

    private static void fillDic(){
        dayDic.put("Mon", 0);
        dayDic.put("Tue", 1);
        dayDic.put("Wed", 2);
        dayDic.put("Thu", 3);
        dayDic.put("Fri", 4);
        dayDic.put("Sat", 5);
        dayDic.put("Sun", 6);
    }

    private int convertDateToVal(String s, int whichPart){
        int day = dayDic.get(s.split(" ")[0]);
        int h = Integer.parseInt(s.split(" ")[1].split("-")[whichPart].split(":")[0]);
        int m = Integer.parseInt(s.split(" ")[1].split("-")[whichPart].split(":")[1]);
        return day * minutesInDay + h * minutesInHour + m;
    }

    public int solution(String S) {
        fillDic();
        String lines[] = S.split("\\r?\\n");
        int [] a = new int [2 * lines.length];
        for(int i = 0; i < 2*lines.length; i= i+2){
            a [i] = convertDateToVal(lines[i/2], 0);
            a [i+1] = convertDateToVal(lines[i/2], 1);
        }
        
        Arrays.sort(a);
        int max = a[0];
        if (max < 6*minutesInDay + 24*minutesInHour - a[2*lines.length - 1]){
            max = 6*minutesInDay + 24*minutesInHour - a[2*lines.length - 1];
        }
        for(int i = 1; i < 2*lines.length-2; i= i+2){
            if (max < a[i+1] - a[i]){
                max = a[i+1] - a[i];
            }
        }
        return max;
    }

    public static void main(String[] args){
        String s ="Sun 10:00-20:00\n"
        + "Fri 05:00-10:00\n";
        LongestSleep l = new LongestSleep();
        System.out.println(l.solution(s));
    }
}
