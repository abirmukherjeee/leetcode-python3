class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftRunningSum, rightRunningSum = [nums[0]], [nums[len(nums)-1]]

        for i in range(1,len(nums)):
            leftRunningSum.append(leftRunningSum[i-1] + nums[i])

        for i in range(len(nums)-2,-1,-1):
            #rightRunningSum.append(rightRunningSum[::-1][0] + nums[i]) #Approch 1
            rightRunningSum.append(rightRunningSum[len(rightRunningSum)-1] + nums[i]) #Approch 2

        for i in range(len(leftRunningSum)):
            if leftRunningSum[i] == rightRunningSum[::-1][i]:
                return i

        return -1
