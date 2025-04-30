package TOClean;

public class LongestCommonPrefix {
   public static void main(String[] args) {
      String[] strings = { "flexible" , "flee", "florida"};
      String prefix = LongestCommonPrefix.longestCommonPrefix(strings);
      System.out.println("Longest Common Prefix:" + prefix);
   }

   public static String longestCommonPrefix(String[] strs) {
      if (strs.length == 0) {
         return "";
      }

      int lowest = strs[0].length();
      for (int i = 1; i < strs.length; i++) {
         lowest = Math.min(lowest, strs[i].length());
      }

      StringBuilder sb = new StringBuilder();
      for (int i = 0; i < lowest; i++) {
         if (matchesCharAt(strs, i)) {
            sb.append(strs[0].charAt(i));
         } else {
            break;
         }
      }
      return sb.toString();
   }

   private static boolean matchesCharAt(String[] strs, int i) {
      char c = strs[0].charAt(i);
      for (int j = 1; j < strs.length; j++) {
         if (c != strs[j].charAt(i)) {
             return false;
         }
      }
      return true;
   }
}

