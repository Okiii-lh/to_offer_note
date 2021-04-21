# encoding=utf-8
# 
import collection
def checkInclusion(s1, s2):
	  need = collection.defaultdict(int)

	  for c in s2:
	  	need[c] += 1
	  need_cnt = len(s2)
	  left = 0

	  for right, c in enumerate(s1):
	  	if need[c] > 0:
	  		need_cnt -= 1
	  	need[c] -= 1

	  	if need_cnt == 0:
	  		while left < right:
	  			c = s1[left]
	  			if need[c] == 0:
	  				if right-left+1 == len(s2):
	  					return True
	  				else:
	  					need[c] += 1
	  					left += 1
	  			need[s1[left]] += 1
	  			need_cnt += 1
	  			left += 1

	 return False


def checkInclusion(self, s1: str, s2: str) -> bool:
        return any([collections.Counter(s1) == collections.Counter(s2[i: i + len(s1)]) 
        		for i in range(0, len(s2) - len(s1) + 1)])