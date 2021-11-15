/*
    The problem: https://leetcode.com/problems/add-binary/
*/

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
        StringBuilder sb = new StringBuilder();
        boolean carry = false;
        int max_len = Math.max(a.length(), b.length());
        for (int i = 0; i < max_len; i++) {
            short currSum = 0;

            int ai = a.length() - 1 - i;
            if (ai >= 0 && a.charAt(ai) == '1') {
                currSum++;
            }

            int bi = b.length() - 1 - i;
            if (bi >= 0 && b.charAt(bi) == '1') {
                currSum++;
            }

            if (carry) {
                currSum++;
            }

            if (currSum % 2 == 0) {
                sb.append("0");
            } else { //currSum == 1
                sb.append("1");
            }

            carry = false;
            if (currSum > 1) {
                carry = true;
            }
        }

        if (carry) {
            sb.append("1");
        }

        return sb.reverse().toString();
    }
}
