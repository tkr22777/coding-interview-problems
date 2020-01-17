class DecodeString {

    public String decodeString(String s) {

        Stack<Character> theStack = new Stack<Character>();

        for (int i = 0; i < s.length(); i++) {
            Character current = s.charAt(i);
            if (current == ']') {
                String toRepeatStr = this.getChars(theStack);
                theStack.pop(); // poping the '[' char
                int repeatCount = getNumber(theStack);
                String decoded = this.decode(repeatCount, toRepeatStr);
                for (int j = 0; j < decoded.length(); j++) {
                    theStack.push(decoded.charAt(j));
                }
            } else {
                theStack.push(current);
            }
        }

        StringBuilder toReturn = new StringBuilder();
        while (!theStack.isEmpty()) {
            toReturn.append(theStack.pop());
        }
        return toReturn.reverse().toString();
    }

    private int getNumber(Stack<Character> theStack) {
        StringBuilder sb = new StringBuilder();
        while (!theStack.isEmpty() && Character.isDigit(theStack.peek())) {
            sb.append(theStack.pop());
        }
        return Integer.parseInt(sb.reverse().toString()); //data pushed into stacked gets reversed
    }

    private String getChars(Stack<Character> theStack) {
        StringBuilder sb = new StringBuilder();
        while (!theStack.isEmpty() && Character.isAlphabetic(theStack.peek())) {
            sb.append(theStack.pop());
        }
        return sb.reverse().toString(); //data pushed into stacked gets reversed
    }

    private String decode(int num, String s) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < num; i++) {
            sb.append(s);
        }
        return sb.toString();
    }
}

