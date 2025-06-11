from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        
        rows, cols = len(matrix), len(matrix[0])
        total_elements = rows * cols
        
        # Direction flags
        move_r = True
        move_d = move_l = move_u = False
        
        # Boundaries
        top, bottom = 0, rows - 1
        left, right = 0, cols - 1
        
        # Current position
        row, col = 0, 0
        result = []
        
        while len(result) < total_elements:
            if move_r:  # Moving right
                while col <= right:
                    print(f"Moving right: row={row}, col={col}, right_limit={right}")
                    result.append(matrix[row][col])
                    if col == right:  # Hit right boundary
                        move_r, move_d = False, True
                        top += 1  # Shrink top boundary
                        row += 1  # Move down to next row
                        break
                    col += 1
                    
            elif move_d:  # Moving down
                while row <= bottom:
                    print(f"Moving down: row={row}, col={col}, bottom_limit={bottom}")
                    result.append(matrix[row][col])
                    if row == bottom:  # Hit bottom boundary
                        move_d, move_l = False, True
                        right -= 1  # Shrink right boundary
                        col -= 1  # Move left to next column
                        break
                    row += 1
                    
            elif move_l:  # Moving left
                while col >= left:
                    print(f"Moving left: row={row}, col={col}, left_limit={left}")
                    result.append(matrix[row][col])
                    if col == left:  # Hit left boundary
                        move_l, move_u = False, True
                        bottom -= 1  # Shrink bottom boundary
                        row -= 1  # Move up to next row
                        break
                    col -= 1
                    
            elif move_u:  # Moving up
                while row >= top:
                    print(f"Moving up: row={row}, col={col}, top_limit={top}")
                    result.append(matrix[row][col])
                    if row == top:  # Hit top boundary
                        move_u, move_r = False, True
                        left += 1  # Shrink left boundary
                        col += 1  # Move right to next column
                        break
                    row -= 1
        
        print(f"Final result: {result}")
        return result


# More Elegant Solution using Direction Vectors
class SolutionElegant:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        
        rows, cols = len(matrix), len(matrix[0])
        
        # Direction vectors: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction_names = ["right", "down", "left", "up"]
        current_dir = 0
        
        # Boundaries that shrink as we complete each layer
        top, bottom = 0, rows - 1
        left, right = 0, cols - 1
        
        row, col = 0, 0
        result = []
        
        print(f"Starting spiral traversal on {rows}x{cols} matrix")
        
        while len(result) < rows * cols:
            dr, dc = directions[current_dir]
            dir_name = direction_names[current_dir]
            
            # Determine how many steps we can take in current direction
            if current_dir == 0:  # Moving right
                steps = right - col + 1
                boundary_update = lambda: globals().update({'top': top + 1}) or (top + 1,)
            elif current_dir == 1:  # Moving down
                steps = bottom - row + 1
                boundary_update = lambda: globals().update({'right': right - 1}) or (right - 1,)
            elif current_dir == 2:  # Moving left
                steps = col - left + 1
                boundary_update = lambda: globals().update({'bottom': bottom - 1}) or (bottom - 1,)
            else:  # Moving up
                steps = row - top + 1
                boundary_update = lambda: globals().update({'left': left + 1}) or (left + 1,)
            
            print(f"Moving {dir_name}: taking {steps} steps from ({row},{col})")
            
            # Take all steps in current direction
            for step in range(steps):
                if len(result) < rows * cols:  # Safety check
                    print(f"  Step {step+1}: visiting ({row},{col}) = {matrix[row][col]}")
                    result.append(matrix[row][col])
                    
                    # Move to next position (except on last step)
                    if step < steps - 1:
                        row, col = row + dr, col + dc
            
            # Update boundary and change direction
            if current_dir == 0:  # After moving right
                top += 1
                row += 1  # Move down for next direction
            elif current_dir == 1:  # After moving down
                right -= 1
                col -= 1  # Move left for next direction
            elif current_dir == 2:  # After moving left
                bottom -= 1
                row -= 1  # Move up for next direction
            else:  # After moving up
                left += 1
                col += 1  # Move right for next direction
            
            current_dir = (current_dir + 1) % 4
            
            print(f"  Updated boundaries: top={top}, bottom={bottom}, left={left}, right={right}")
        
        print(f"Final elegant result: {result}")
        return result


# Ultra-Clean Solution using Layer Peeling
class SolutionUltraClean:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        
        result = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        
        print(f"Processing {len(matrix)}x{len(matrix[0])} matrix layer by layer")
        
        while top <= bottom and left <= right:
            print(f"Processing layer: top={top}, bottom={bottom}, left={left}, right={right}")
            
            # Traverse right across top row
            for col in range(left, right + 1):
                print(f"  Right: ({top},{col}) = {matrix[top][col]}")
                result.append(matrix[top][col])
            top += 1
            
            # Traverse down right column
            for row in range(top, bottom + 1):
                print(f"  Down: ({row},{right}) = {matrix[row][right]}")
                result.append(matrix[row][right])
            right -= 1
            
            # Traverse left across bottom row (if we still have rows)
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    print(f"  Left: ({bottom},{col}) = {matrix[bottom][col]}")
                    result.append(matrix[bottom][col])
                bottom -= 1
            
            # Traverse up left column (if we still have columns)
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    print(f"  Up: ({row},{left}) = {matrix[row][left]}")
                    result.append(matrix[row][left])
                left += 1
        
        print(f"Final ultra-clean result: {result}")
        return result

