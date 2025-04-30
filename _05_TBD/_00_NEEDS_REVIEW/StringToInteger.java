class Solution {

    public static void main(String[] args) {
        System.out.println(new Solution().myAtoi(" -455ASD"));
    }
    
    public int myAtoi(String str) {

        boolean negative = false;
        int startIndex = -1;
        int endIndex = -1;

        if (str.length() == 0) {
            return 0;
        }

        if (str.length() == 1) {
            int digit = getDigit(str.charAt(0));
            if (digit == -1) {
                return 0;
            } else {
                return digit;
            }
        }

        for (int i = 0; i < str.length(); i++) {
            char charAtI = str.charAt(i);
            if (charAtI == ' ') {
                continue;
            }

            if (charAtI == '+' || charAtI == '-') {
                if ( i + 1 < str.length() && getDigit( str.charAt(i+1) ) >= 0)  {
                    startIndex = i + 1;
                    if (charAtI == '-') {
                        negative = true;
                    }
                    break;
                } else {
                    return 0;
                }
            }

            if (getDigit(charAtI) >= 0) {
                startIndex = i;
                break;
            } else {
                return 0;
            }
        }


        if (startIndex == -1) {
            return 0;
        }


        for (int i = startIndex; i < str.length(); i++) {
            char charAtI = str.charAt(i);
            if (getDigit(charAtI) == -1) {
                break;
            }
            endIndex = i + 1;
        }

        for (int i = startIndex; i < endIndex; i++) {
            char charAtI = str.charAt(i);
            if (getDigit(charAtI) == 0) {
                startIndex = i;
            } else {
                break;
            }
        }

        if (startIndex == endIndex) {
            return 0;
        }

        //System.out.println("|"+ str.substring(startIndex, endIndex) + "|");
        long  result;
        if (negative) {
            if (endIndex - startIndex > 10) {
                return Integer.MIN_VALUE;
            }
            result = Long.parseLong(str.substring(startIndex, endIndex));
            result *= -1;
            if (result < Integer.MIN_VALUE) {
                return Integer.MIN_VALUE;
            }
        } else {
            if (endIndex - startIndex > 10) {
                return Integer.MAX_VALUE;
            }
            result = Long.parseLong(str.substring(startIndex, endIndex));
            if (result > Integer.MAX_VALUE) {
                return Integer.MAX_VALUE;
            }
        }

        return (int) result;
    }

    public int getDigit(char c) {
        if (c >= '0' && c <= '9') {
            switch (c) {
                case '0':
                    return 0;
                case '1':
                    return 1;
                case '2':
                    return 2;
                case '3':
                    return 3;
                case '4':
                    return 4;
                case '5':
                    return 5;
                case '6':
                    return 6;
                case '7':
                    return 7;
                case '8':
                    return 8;
                case '9':
                    return 9;
            }
        }
        return -1;
    }
}

