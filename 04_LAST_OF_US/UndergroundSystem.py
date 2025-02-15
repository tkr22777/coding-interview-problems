
class UndergroundSystem:

    def __init__(self):
        self.events = {}
        self.duration = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.events[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        sS, t1 = self.events[id]
        del self.events[id]

        key = sS + "->" + stationName
        tot_duration, trip_count = 0, 0
        if key in self.duration:
            tot_duration, trip_count = self.duration[key]

        tot_duration += t - t1
        trip_count += 1

        self.duration[key] = (tot_duration, trip_count)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = startStation + "->" + endStation
        tot_duration, trip_count = self.duration[key]
        return float(tot_duration) / trip_count


# travel_events:
# id, sS, t1
# id, eS, t2 
# look up by id to get sS and create a duration event

# duration:
# add events by sSeS, total_duration_accross_trips, and total trip count
# sS, eS, 10, count

ugs = UndergroundSystem()
ugs.checkIn(45, "Leyton", 3)
ugs.checkIn(32, "Paradise", 8)
ugs.checkIn(27, "Leyton", 10)
ugs.checkOut(45, "Waterloo", 15)  # Customer 45 "Leyton" -> "Waterloo" in 15-3 = 12
ugs.checkOut(27, "Waterloo", 20)  # Customer 27 "Leyton" -> "Waterloo" in 20-10 = 10
ugs.checkOut(32, "Cambridge", 22)  # Customer 32 "Paradise" -> "Cambridge" in 22-8 = 14
ugs.print()
print(ugs.getAverageTime("Paradise", "Cambridge"))  # return 14.00000. One trip "Paradise" -> "Cambridge", (14) / 1 = 14
print(ugs.getAverageTime("Leyton", "Waterloo"))  # return 11.00000. Two trips "Leyton" -> "Waterloo", (10 + 12) / 2 = 11
ugs.checkIn(10, "Leyton", 24)
print(ugs.getAverageTime("Leyton", "Waterloo"))  # return 11.00000
ugs.checkOut(10, "Waterloo", 38)  # Customer 10 "Leyton" -> "Waterloo" in 38-24 = 14
print(ugs.getAverageTime("Leyton",
                         "Waterloo"))  # return 12.00000. Three trips "Leyton" -> "Waterloo", (10 + 12 + 14) / 3 = 12
