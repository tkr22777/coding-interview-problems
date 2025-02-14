package logdeamon;

import java.time.Instant;
import java.util.Arrays;
import java.util.List;
import java.util.Map;

public class Logger {

    public static void main(String[] args) {
        for (int i = 0; i < 100; i++) {
            Instant ins = Instant.now();
            System.out.println("LOG: This is great! || Timestamp/Instance:" + ins.toString());
            // Since timestamps are very granular, it is okay to use timestamp as an identifier or
            // for more uniqueness a timestamp and the message hash as an identifier
        }
    }

    /* log related functions */
    public static void log(String message, Map<String, String> tags) {
        String fileName = currentFileName();
        String content = format(message, tags);
        appendToFile();
    }

    private static void appendToFile() {
    }

    private static String format(String message, Map<String, String> tags) {
        Instant ins = Instant.now();
        return "Some log at instant:" + ins;
    }

    private static String currentFileName() {
        //based on file capacity and current usage give me the name of the current file
        Instant ins = Instant.now();
        return "File name at ins" + ins;
    }

    /* parser and pusher related functions */
    private static void parse() throws Exception {
        while (true) {
            String filename = currentFileName();
            List<String> filenames = previousFilenames(filename);
            for (String fileName: filenames) {
                // create parsing threads for each files and create a deletion file
                System.out.println("Parse each line of this file and http call:" + fileName);
                parseAndPushFile(fileName);
            }
            Thread.sleep(30);
        }
    }

    private static void parseAndPushFile(String fileName) {
        int offset = 0;
        List<String> lines = getLines(fileName, offset);
        while (lines.size() != 0) {
            for (String line: lines) {
                try {
                    pushLog(line);
                } catch (Exception ex) {
                    //failed with exponential backoff. stop working for a while
                }
            }
            offset = offset + 20;
            lines = getLines(fileName, offset);
        }
        // when all of the lines have been pushed successfully, purge the file
    }

    // lets assume this does exponential retries
    private static void pushLog(String message) throws Exception {
        //push log with http call
    }

    private static List<String> getLines(String fileName, int offset) {
        return Arrays.asList("list of lines, with some upper limit");
    }

    private static List<String> previousFilenames(String current) {
        List<String> allFilenames = Arrays.asList("exf1", "exf2", "exf3");
        allFilenames.remove(current);
        return allFilenames;
    }
}
