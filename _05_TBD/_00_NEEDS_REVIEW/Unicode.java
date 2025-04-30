package com.company;

public class Unicode {

    public static void main(String[] args) {
        // write your code here
        //48 - 57
        printUnicodeOfChars("0123456789");
        //48 - 57
        printUnicodeOfChars("ABCDEFGHIJKLMNOPQRSTUVWXYZ");
        //48 - 57
        printUnicodeOfChars("abcdefghijklmnopqrstuvwxyz");
        //48 - 57
        printUnicodeOfCharsUsingChars("0123456789");
        //48 - 57
        printUnicodeOfCharsUsingChars("ABCDEFGHIJKLMNOPQRSTUVWXYZ");
        //48 - 57
        printUnicodeOfCharsUsingChars("abcdefghijklmnopqrstuvwxyz");
    }


    public static void printUnicodeOfChars(String str) {
        for(int i = 0; i < str.length(); i++) {
            System.out.println("Character: " + str.charAt(i) + " corresponding code:" + str.codePointAt(i));
        }
    }

    public static void printUnicodeOfCharsUsingChars(String str) {
        for(int i = 0; i < str.length(); i++) {
            Character character = str.charAt(i);
            System.out.println("Character: " + character + " char value:" + Character.toChars((int) character)[0]);
        }
    }
}
