class BusBooking:

    def __init__(self, n: int):
        self.booked=set()
        self.cost={}
        self.total_time=0
        

    def toggle(self, seat: str) -> None:
        if seat in self.booked:
            self.booked.remove(seat)
            self.total_time-=self.cost[seat]
            del self.cost[seat]
        else:
            time=1
            if seat[0]=="A" and "B"+seat[1:] in self.booked:
                time=3
            elif seat[0]=="D" and "C"+seat[1:] in self.booked:
                time=3
            self.booked.add(seat)
            self.cost[seat]=time
            self.total_time+=time    
    def getTotalTime(self) -> int:
        return self.total_time
        

    def getMinTime(self) -> int:
        return len(self.booked)
        


# Your BusBooking object will be instantiated and called as such:
# obj = BusBooking(n)
# obj.toggle(seat)
# param_2 = obj.getTotalTime()
# param_3 = obj.getMinTime()