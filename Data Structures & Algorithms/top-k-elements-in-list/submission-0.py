class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}

        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        
        buckets = [[]] * (len(nums) + 1)

        for i in freq:
            copy = buckets[freq[i]].copy()
            copy.append(i)
            buckets[freq[i]] = copy

        topk = []

        for index in range(len(nums), -1, -1):
            if len(topk) < k:
                if len(topk) + len(buckets[index]) <= k:
                    print(buckets[index])
                    topk.extend(buckets[index])
                else:
                    topk.extend(buckets[index][: k - len(topk)])
     
        # print(freq)
        # print(buckets)
        # print(topk)

        return topk

        