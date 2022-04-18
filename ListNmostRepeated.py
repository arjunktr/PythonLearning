import heapq

    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d={}
        for item in nums:
            if item not in d:
                d[item]=1
            else:
                d[item]=d[item]+1
        new_list=[(value,key) for key,value in d.items()]
        heapq.heapify(new_list)
        res=heapq.nlargest(k,new_list)
        req=[]
        for index in range(k):
            req.append(res[index][1])
        return req
