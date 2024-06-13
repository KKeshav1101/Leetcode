class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
        seats.sort()
        students.sort()
        ans=0
        for seat,student in zip(seats,students):
            ans=ans+abs(seat-student)
        return ans
