package TOClean;

import java.util.StringJoiner;

public class StringArraySerializeDeserialize {
}

// In the language of your choice write two functions:
// One that takes a list of strings and returns a single
// string, and a second that takes the output of the first
// function and returns the original list.

class MyCode {
    private static String DELIM = "XX";

    public static void main (String[] args) {
        System.out.println("Hello Java");

        String joined = joinString(new String[] {"abc", "def", "XXX", "X\\XX"});
        String joined2 = joinString(new String[] {"|", "||", "|||", "|||", "|||||||"});

        //"abcd|efg" ,  "ab"
        //"abcd\|efg|ab"
        //"abcd\" "efg" "ab"

        System.out.println(joined);

        String[] unjoined = unjoin(joined);
        for (String str: unjoined) {
            System.out.println(str);
        }
    }

    public static String joinString(String[] input) {
        StringJoiner sj = new StringJoiner(DELIM, "", "");
        for (String str: input) {
            String str1 = str.replace("X", "\\X\\");
            sj.add(str1);
        }
        return sj.toString();
    }

    public static String[] unjoin(String input) {
        String[] split = input.split(DELIM);
        for (int i = 0; i < split.length; i++) {
            split[i] = split[i].replace("\\X\\", "X");
        }

        //return parts.toArray(new String[parts.size()]);
        return split;
    }

}
