class Solution:
    def largestAltitude(self, gain):
        # start altitude is 0
        altitude = [0]
        
        # accumulate altitudes
        for g in gain:
            altitude.append(altitude[-1] + g)
        
        # return the highest altitude
        return max(altitude)
