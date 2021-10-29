import java.util.*;

class FindDuplicateFiles {

    public static void main(String[] args) {
        String[] paths = { 
            "root/a 1.txt(abcd) 2.txt(efgh)",
            "root/c 3.txt(abcd)",
            "root/c/d 4.txt(efgh)",
            "root 4.txt(efgh)"
        };
        System.out.println(new FindDuplicateFiles().findDuplicate(paths));
    }

    public List<List<String>> findDuplicate(String[] paths) {

        HashMap<String, Set<String>> contentToFiles = new HashMap<String, Set<String>>();

        for (String path: paths) {
            String[] pathElems = path.split(" ");
            String dir = pathElems[0];
            for (int i = 1; i < pathElems.length; i++) {
                int start = pathElems[i].lastIndexOf("(");
                String fileName = pathElems[i].substring(0, start);
                String filePath = String.format("%s/%s", dir, fileName);

                int end = pathElems[i].lastIndexOf(")");
                String content = pathElems[i].substring(start + 1, end);

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

