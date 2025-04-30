package TOClean;

import java.util.*;

class Event {
    int id;
    int start;
    int end;
    public Event(int id, int start, int end) { this.id = id; this.start = start; this.end = end;};
    public String toString() {
        return  "ID:" + id;
    }
}

public class Conflicts {

    public static void main(String[] args) {
        Event[] events = {
            new Event(1, 1, 2),
            new Event(2, 2, 4),
            new Event(3, 3, 5),
            new Event(4, 5, 8),
            new Event(5, 9, 12),
            new Event(6, 10, 16),
            new Event(7, 11, 13),
            new Event(8, 14, 15),
            new Event(9, 17, 18),
            new Event(10, 17, 18),
        };
        System.out.println("test");
        Event[] conflicts = findConflicts(events);
        System.out.println(Arrays.toString(conflicts));
    }

    // A [    ]
    // B        [                   ]
    // C            [     ]
    // E               [    ]
    // F                    [    ]
    // G                     [        ]
    // H                            [       ]
    public static Event[] findConflicts(Event[] events) {
        if (events.length == 0) {
            return new Event[0];
        }
        Arrays.sort(events, Comparator.comparingInt(a -> a.start));

        Set<Event> conflicts = new HashSet<>();
        Event latest = events[0];
        for (int i = 1; i < events.length; i++) {
            if (events[i].start < latest.end) {
                conflicts.add(latest);
                conflicts.add(events[i]);
            }

            if (latest.end < events[i].end) {
                latest = events[i];
            }
        }

        Event[] array = new Event[conflicts.size()];
        conflicts.toArray(array); // fill the array
        return array;
    }
}
