class Solution(object):
    def averageWaitingTime(self, customers):
        """
        :type customers: List[List[int]]
        :rtype: float
        """
        total_waiting_time=0.0
        current_time=0.0

        for arrival,service_time in customers:
            if current_time < arrival:
                current_time = arrival
            waiting_time = current_time - arrival + service_time
            total_waiting_time += waiting_time
            current_time += service_time
        
        return total_waiting_time/len(customers)
