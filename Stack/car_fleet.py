class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars,stack=[],[]
        for p,s in zip(position,speed):
            t=(target-p)/s
            cars.append([p,t])
        cars.sort(reverse=True)
        for p,t in cars:
            stack.append([p,t])
            if len(stack)>=2 and stack[-2][1]>=stack[-1][1]:
                stack.pop()
        return len(stack)