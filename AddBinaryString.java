import java.util.*;

class AddBinaryString {

    /*
     string binStr = `0101`,
     len(binStr) -> 4

     binStr[0]   -> 0
     binStr[1]   -> 1
     binStr[2]   -> 0
     binStr[3]   -> 1
    */

    public static void main(String[] args) {
        String a = "1011001";
        String b = "1011101";
        System.out.println("  A: " + a);
        System.out.println("  B: " + b);
        System.out.println("A+B:" + addBinary(a, b));
    }

    public static String addBinary(String a, String b) {

        int max_len = Math.max(a.length(), b.length());

        boolean carry = false;

        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < max_len; i++) {
            short currSum = 0;

            if (a.length() - 1 - i >= 0 && a.charAt(a.length() - 1 - i) == '1') {
                currSum++;
            }

            if (b.length() - 1 - i >= 0 && b.charAt(b.length() - 1 - i) == '1') {
                currSum++;
            }

            if (carry) {
                currSum++;
            }

            if (currSum == 0 || currSum == 2) {
                sb.append("0");
            } else {
                sb.append("1");
            }

            carry = currSum > 1 ? true:false;
        }

        if (carry) {
            sb.append("1");
        }

        return sb.reverse().toString();
    }
}
