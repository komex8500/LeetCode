class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        l1 = len(img)
        l2 = len(img[0])
        result = [[0] * l2 for _ in range(l1)]
        for j in range(l1):
            for k in range(l2):
                sum = 0
                size = 0
                for x in range(j-1, j+2):
                    for y in range(k-1, k+2):
                        if x < 0 or y < 0 or x > l1-1 or y > l2-1:
                            continue
                        sum += img[x][y]
                        size += 1
                result[j][k] = sum//size
        return result