/**
 * // This is the HtmlParser's API interface.
 * // You should not implement it, or speculate about its implementation
 * interface HtmlParser {
 *     public List<String> getUrls(String url) {}
 * }
 */
class Solution {

    class CrawlerThread extends Thread {

        String hostname, candidate;
        HtmlParser htmlParser;
        List<String> results;

        public CrawlerThread(HtmlParser htmlParser,
                             String hostname,
                             String candidate) {
            this.htmlParser = htmlParser;
            this.hostname = hostname;
            this.candidate = candidate;
        }

        public void run() {
            this.results = new ArrayList<String>();
            List<String> temp = htmlParser.getUrls(candidate);
            for (int i = 0; i < temp.size(); i++) {
                String val = temp.get(i);
                if (val.startsWith(hostname)) {
                    results.add(val);
                }
            }
        }
    }

    public List<String> crawl(String startUrl, HtmlParser htmlParser) {

        String hostname = getHostname(startUrl);
        Set<String> candidates = new HashSet<String>(Arrays.asList(startUrl));
        Set<String> visited = new HashSet<String>();

        while (candidates.size() > 0) {

            List<CrawlerThread> crawlers = new ArrayList<CrawlerThread>();
            for (String candidate: candidates) {
                if (visited.contains(candidate)) {
                    continue;
                }
                visited.add(candidate);
                CrawlerThread ct = new CrawlerThread(htmlParser, hostname, candidate);
                ct.start();
                crawlers.add(ct);
            }

            candidates.clear();
            for (int i = 0; i < crawlers.size(); i++) {
                CrawlerThread cw = crawlers.get(i);
                try {
                    cw.join();
                } catch (Exception ex) { System.out.println("Exception:" + ex.getMessage()); }

                candidates.addAll( cw.results.stream()
                                  .filter(url -> !visited.contains(url))
                                  .collect(Collectors.toList()));
            }
        }

        return visited.stream().collect(Collectors.toList());
    }

    public static String getHostname(String url) {
        int count = 0;
        for (int i = 0; i < url.length(); i++) {

            if (url.charAt(i) - '/' == 0) {
                count++;
            }

            if (count == 3) {
                return url.substring(0, i);
            }
        }
        return null;
    }
}

