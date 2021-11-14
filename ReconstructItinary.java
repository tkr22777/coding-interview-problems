/*
 * https://leetcode.com/problems/reconstruct-itinerary/submissions/
 */
import java.util.*;

class ReconstructItinary {
    public static void main(String[] args) {
        /* {
         *  {"EZE","TIA"},{"EZE","HBA"},{"AXA","TIA"},{"JFK","AXA"}, {"ANU","JFK"},
         *  {"ADL","ANU"},{"TIA","AUA"},{"ANU","AUA"},{"ADL","EZE"},{"ADL","EZE"},
         *  {"EZE","ADL"},{"AXA","EZE"},{"AUA","AXA"},{"JFK","AXA"},{"AXA","AUA"},
         *  {"AUA","ADL"},{"ANU","EZE"},{"TIA","ADL"},{"EZE","ANU"},{"AUA","ANU"}
         * }
         */
    }

    public List<String> findItinerary(List<List<String>> tickets) {
        int totalTickets = tickets.size();
        Map<String, ArrayList<String>> departToArrive = new HashMap<String, ArrayList<String>>();

        //building the adjacency map
        for (List<String> ticket: tickets) {
            String depart = ticket.get(0);
            String arrive = ticket.get(1);
            departToArrive.computeIfAbsent(depart, a -> new ArrayList<String>())
                .add(arrive);
        }

        departToArrive.keySet()
            .forEach(k -> Collections.sort(departToArrive.get(k)));
        return findItineraryRecursive(departToArrive, "JFK", totalTickets);
    }

    private ArrayList<String> findItineraryRecursive(Map<String, ArrayList<String>> departToArrive, String depart, int totalTickets) {
        //no tickets left, we are at the end of our itinerary!
        if (totalTickets == 0) {
            return new ArrayList<>(Arrays.asList(depart));
        }

        //unacceptable base case, no ticket with the current departure; empty itinerary
        if (!departToArrive.containsKey(depart)) {
            return null;
        }

        ArrayList<String> arrivals = departToArrive.get(depart);
        for (int i = 0; i < arrivals.size(); i++) {
            String newDepart = arrivals.get(i);
            arrivals.remove(i); //removing the newDepart prior to rest of calculation
            ArrayList<String> anItin = findItineraryRecursive(departToArrive, newDepart, totalTickets - 1);
            arrivals.add(i, newDepart);
            if (anItin != null) { // found an valid itinerary
                anItin.add(0, depart); //adding to front
                return anItin;
            }
        }
        return null;
    }
}
