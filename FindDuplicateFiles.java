import java.*;
import java.util.*;

class FindDuplicateFiles {

    public static void main(String[] args) {
        System.out.println("Compiling");
    }

    public List<List<String>> findDuplicate(String[] paths) {

        HashMap<String, Set<String>> contentToFiles = new HashMap<String, Set<String>>();

        for (String path: paths) {
            String[] pathElements = path.split(" ");
            String directory = pathElements[0];
            for (int i = 1; i < pathElements.length; i++) {
                int start = pathElements[i].lastIndexOf("(");
                int end = pathElements[i].lastIndexOf(")");
                String filePath = directory + "/" + pathElements[i].substring(0, start);
                String content = pathElements[i].substring(start + 1, end);
                contentToFiles.computeIfAbsent(content, f -> new HashSet<String>())
                    .add(filePath);
            }
        }

        List<List<String>> toReturn = new ArrayList<List<String>>();
        for (Set<String> duplicateFiles: contentToFiles.values()) {
            if (duplicateFiles.size() > 1) {
                toReturn.add(new ArrayList<String>(duplicateFiles));
            }
        }

        return toReturn;
    }
}

