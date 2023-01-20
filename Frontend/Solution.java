import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

// class Result {

//     Scanner scanner =new Scanner(System.in);
//     long size =scanner.nextLong();
//     Map<Long,Long> map=new HashMap<>();
//     long operations=scanner.nextLong();
//     for(long i=0;i<operations;i++){
//         long start=scanner.nextLong();
//         long end = scanner.nextLong();
//         long value= scanner.nextLong(); 
//         map.put(start,(map.containsKey(start)?map.get(start):0)+value);
//         map.put(start,(map.containsKey(end+1)?map.get(end+1):0)-value);
//     }
    
//         long max=0;
//         long value=0;
//         for(long i=0;i<size;i++){
//             value +=(map.containsKey(i+1)?map.get(i+1):0);
//             max= Math.max(max,value);
//         }
//     System.out.println(max);
// }

public class Solution {
    public static void main(String[] args) throws IOException 
    {
        Scanner scanner = new Scanner(System.in);
        long size = scanner.nextLong();

        Map<Long, Long> map = new HashMap<>();
        long operations = scanner.nextLong();

        for (long i = 0; i < operations; i++) {
            long start = scanner.nextLong();
            long end = scanner.nextLong();
            long value = scanner.nextLong();

            map.put(start, (map.containsKey(start) ? map.get(start) : 0) + value);
            map.put(end + 1, (map.containsKey(end + 1) ? map.get(end + 1) : 0) - value);
        }

        long max = 0;
        long value = 0;
        for (long i = 0; i < size; i++) {
            value += (map.containsKey(i + 1) ? map.get(i + 1) : 0);
            max = Math.max(max, value);
        }

        System.out.println(max);
    }
}