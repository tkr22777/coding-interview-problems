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
        StringBuilder result = new StringBuilder();
        int carry = 0;
        int maxLen = Math.max(a.length(), b.length());
        
        for (int i = 0; i < maxLen; i++) {
            int sum = carry;
            
            if (i < a.length()) { // Add bit from string a if available
                sum += a.charAt(a.length() - 1 - i) - '0';
            }
            
            if (i < b.length()) { // Add bit from string b if available
                sum += b.charAt(b.length() - 1 - i) - '0';
            }
            
            result.append(sum % 2);
            carry = sum / 2;
        }
        
        if (carry > 0) {
            result.append(1);
        }
        
        return result.reverse().toString();
    }
}
