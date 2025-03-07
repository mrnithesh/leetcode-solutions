class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        import math
        primes=[]
        #calculate primes bw the range
        for i in range(left,right+1):
            if i<2:
                continue
            if i==2:
                primes.append(i)
                continue
            
            if i%2==0:
                isprime=False
                continue

            isprime=True
            for j in range(3,int(math.sqrt(i)+1),2):
                if i % j==0:
                    isprime=False
                    break
            if isprime:
                primes.append(i)

        #edge case if only one prime or no prime exists
        if len(primes)<2:
            return [-1,-1]        

        #sliding window to find the closest pair
        i=0
        closest_dis= primes[1]-primes[0]
        pair= [primes[0],primes[1]]
        while i<len(primes)-1:
            if primes[i+1]-primes[i]<closest_dis:
                closest_dis = primes[i+1]-primes[i]
                pair=[primes[i],primes[i+1]]
            i+=1
        return pair
