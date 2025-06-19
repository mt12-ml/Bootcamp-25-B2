class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        def merge_valleys(idx, valleys):
            if idx == len(valleys) - 1:
                return valleys
            
            if valleys[idx][0] > valleys[idx][len(valleys[idx]) - 1] and valleys[idx+1][len(valleys[idx+1]) - 1] > valleys[idx][len(valleys[idx]) - 1]:
        
                valley_1 = valleys.pop(idx)
                valley_2 = valleys.pop(idx)
                valley_1.pop()
                merged_valley = valley_1 + valley_2
                
                if not valleys:
                    valleys = [merged_valley]
                else:
                    valleys.insert(idx, merged_valley)

                return merge_valleys(idx, valleys)
            
            else:
                return merge_valleys(idx + 1, valleys)
        
        def merge_global(idx, valleys):
           
            if idx == len(valleys) - 1:
                return valleys
            
            if idx == len(valleys) - 2:
                return merge_valleys(0, valleys)
            
            if valleys[idx][0] <= valleys[idx][len(valleys[idx]) - 1] and valleys[idx+1][0] <= valleys[idx+1][len(valleys[idx+1]) - 1]:
                return merge_global(idx + 1, valleys)
            
            if valleys[idx][0] <= valleys[idx][len(valleys[idx]) - 1] and valleys[idx+1][0] >= valleys[idx+1][len(valleys[idx+1]) - 1]:
                return merge_global(idx + 1, valleys)

            val = valleys[idx][len(valleys[idx]) - 1]
            start = idx
            end = idx + 1
    
            while end < len(valleys) and valleys[end][len(valleys[end]) - 1] <= valleys[end - 1][len(valleys[end - 1]) - 1]:
                
                end += 1
            while end < len(valleys) and valleys[end][len(valleys[end]) - 1] > valleys[end - 1][len(valleys[end - 1]) - 1] :
    
                if valleys[end][len(valleys[end]) - 1] >= val and valleys[end][len(valleys[end]) - 1] >= valleys[start][0]:
                    break
                end += 1
            
            if end < len(valleys) and valleys[end][len(valleys[end]) - 1] >= val and valleys[end][len(valleys[end]) - 1] >= valleys[start][0]:
                
                valley = valleys.pop(start)
                valley.pop()
                for i in range(end - start - 1):
                    temp_valley = valleys.pop(start)
                    valley += temp_valley
                    valley.pop()
                temp_valley = valleys.pop(start)
                valley += temp_valley
                valleys.insert(start, valley)
                return merge_global(start, valleys)
            
            else:
                return merge_global(idx + 1, valleys)


        if len(height) <= 1:
            return 0

        while len(height) > 1:
            if (height[0] <= height[1]):
                height.pop(0)
            else:
                break

        if len(height) <= 1:
            return 0
        
        while height:
            if height[len(height) - 1] <= height[len(height) - 2]:
                height.pop(len(height) - 1)
            else:
                break
        
        if not height:
            return 0

        valleys = []
        i = 0
        while i < len(height):
            valley = []
            while  i+1 < len(height) and height[i] >= height[i+1]:
                valley.append(height[i])
                i += 1
                if i >= len(height) - 1:
                    break
            
            if i >= len(height) - 1:
                break

            flag = False
            while i+1 < len(height) and  height[i] <= height[i+1]:
                flag = True
                valley.append(height[i])
                i += 1
                if i >= len(height) - 1:
                    break
               
            if flag:
                valley.append(height[i])
            valleys.append(valley)
            
       
        valleys = merge_valleys(0, valleys)
        print(valleys)
        valleys = merge_global(0, valleys)
        print(valleys)


        total_water = 0
        for i in range(len(valleys)):
            if valleys[i][0] > valleys[i][len(valleys[i]) - 1]:
                total_area = len(valleys[i]) * valleys[i][len(valleys[i]) - 1]
                brick_area = valleys[i][len(valleys[i]) - 1]
                for j in range(1, len(valleys[i])):
                    if valleys[i][j] > valleys[i][len(valleys[i]) - 1]:
                        brick_area += valleys[i][len(valleys[i]) - 1]
                    else:
                        brick_area += valleys[i][j]
                water_area = total_area - brick_area
                total_water += water_area
            
            elif valleys[i][0] <= valleys[i][len(valleys[i]) - 1]:
                total_area = len(valleys[i]) * valleys[i][0]
                brick_area = valleys[i][0]
                for j in range(0, len(valleys[i]) - 1):
                    if valleys[i][j] > valleys[i][0]:
                        brick_area += valleys[i][0]
                    else:
                        brick_area += valleys[i][j]
                water_area = total_area - brick_area
           
                total_water += water_area
             
        return total_water



        
        
