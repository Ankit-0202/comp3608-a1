def NUM_IN_A_ROW(arr, count, value):
    
    if count == 4:
        return count_in_a_row(arr, count, value)

    # def count_in_a_row(arr, count, value):
    rows, cols = len(arr), len(arr[0])
    total = 0
    
    # Check rows
    for r in range(rows):
        for c in range(cols - count + 1):
            if all(arr[r][c+i] == value for i in range(count)) and \
            (c == 0 or arr[r][c-1] != value) and \
            (c + count == cols or arr[r][c+count] != value):
                total += 1
    
    # Check columns
    for c in range(cols):
        for r in range(rows - count + 1):
            if all(arr[r+i][c] == value for i in range(count)) and \
            (r == 0 or arr[r-1][c] != value) and \
            (r + count == rows or arr[r+count][c] != value):
                total += 1
    
    # Check diagonals
    for r in range(rows - count + 1):
        for c in range(cols - count + 1):
            if all(arr[r+i][c+i] == value for i in range(count)) and \
            (r == 0 or c == 0 or arr[r-1][c-1] != value) and \
            (r + count == rows or c + count == cols or arr[r+count][c+count] != value):
                total += 1
            
            if all(arr[r+i][c+count-1-i] == value for i in range(count)) and \
            (r == 0 or c + count == cols or arr[r-1][c+count] != value) and \
            (r + count == rows or c == 0 or arr[r+count][c-1] != value):
                total += 1
    
    return total

def count_in_a_row(arr, count, value):
    rows, cols = len(arr), len(arr[0])
    total = 0
    visited = set()
    
    # Check rows
    for r in range(rows):
        for c in range(cols - count + 1):
            if all(arr[r][c+i] == value for i in range(count)):
                if all((r, c+i) not in visited for i in range(count)):
                    total += 1
                    visited.update((r, c+i) for i in range(count))
    
    # Check columns
    for c in range(cols):
        for r in range(rows - count + 1):
            if all(arr[r+i][c] == value for i in range(count)):
                if all((r+i, c) not in visited for i in range(count)):
                    total += 1
                    visited.update((r+i, c) for i in range(count))
    
    # Check diagonals
    for r in range(rows - count + 1):
        for c in range(cols - count + 1):
            if all(arr[r+i][c+i] == value for i in range(count)):
                if all((r+i, c+i) not in visited for i in range(count)):
                    total += 1
                    visited.update((r+i, c+i) for i in range(count))
            
            if all(arr[r+i][c+count-1-i] == value for i in range(count)):
                if all((r+i, c+count-1-i) not in visited for i in range(count)):
                    total += 1
                    visited.update((r+i, c+count-1-i) for i in range(count))
    
    return total


arr = [['s','Q','Q','Q','Q','Q','Q'],
       ['Q','s','Q','s','Q','Q','Q'],
       ['Q','Q','s','Q','Q','Q','Q'],
       ['Q','Q','Q','s','Q','Q','Q'],
       ['Q','Q','Q','Q','s','Q','Q'],
       ['Q','Q','Q','Q','Q','s','Q']]

print(NUM_IN_A_ROW(arr, 4, 's'))