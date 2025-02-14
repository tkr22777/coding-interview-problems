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
        StringBuilder stringBuilder = new StringBuilder();
        boolean carry = false;
        int maxLen = Math.max(a.length(), b.length());
        for (int i = 0; i < maxLen; i++) {
            short currentSum = 0;

            int ai = a.length() - 1 - i;  // reading from the lsb
            if (ai >= 0 && a.charAt(ai) == '1') {
                currentSum++;
            }

            int bi = b.length() - 1 - i; // reading from the lsb
            if (bi >= 0 && b.charAt(bi) == '1') {
                currentSum++;
            }

            if (carry) {
                currentSum++;
            }

            if (currentSum % 2 == 0) {
                stringBuilder.append("0");
            } else { //currSum == 1
                stringBuilder.append("1");
            }

            carry = currentSum > 1;
        }

        if (carry) {
            stringBuilder.append("1");
        }

        return stringBuilder.reverse().toString();
    }
}
