import java.util.*;

class FindDuplicateFiles {
    public static void main(String[] args) {
        String[] pathsWithFiles = {
            "root/a 1.txt(abcd) 2.txt(efgh)",
            "root/c 3.txt(abcd)",
            "root/c/d 4.txt(efgh)",
            "root 4.txt(efgh)"
        };
        System.out.println(new FindDuplicateFiles().findDuplicate(pathsWithFiles));
    }

    public List<List<String>> findDuplicate(String[] pathWithFilesArray) {
        HashMap<String, Set<String>> contentToFiles = new HashMap<>();

        for (String pathWithFiles: pathWithFilesArray) {
            String[] pathElems = pathWithFiles.split(" ");
            String dir = pathElems[0];
            for (int i = 1; i < pathElems.length; i++) {
                String fileWithContent = pathElems[i];
                int start = fileWithContent.lastIndexOf("(");
                int end = fileWithContent.lastIndexOf(")");
                String content = fileWithContent.substring(start + 1, end);

                String fileName = fileWithContent.substring(0, start);
                String filePath = String.format("%s/%s", dir, fileName);

                contentToFiles.computeIfAbsent(content, f -> new HashSet<String>())
                    .add(filePath);
            }
        }

        List<List<String>> toReturn = new ArrayList<List<String>>();
        for (Set<String> duplicateFiles: contentToFiles.values()) {
            if (duplicateFiles.size() > 1) {
                toReturn.add(new ArrayList<>(duplicateFiles));
            }
        }
        return toReturn;
    }
}

