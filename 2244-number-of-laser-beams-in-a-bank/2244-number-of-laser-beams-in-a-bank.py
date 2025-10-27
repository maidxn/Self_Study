class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        # Count number of devices per row
        device_counts = [row.count('1') for row in bank if '1' in row]
        
        total_beams = 0
        # Each valid pair of consecutive non-empty rows contributes product of device counts
        for i in range(1, len(device_counts)):
            total_beams += device_counts[i - 1] * device_counts[i]
        
        return total_beams