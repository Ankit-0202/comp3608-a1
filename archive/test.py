def NUM_IN_A_ROW(arr, n, char):

    count = 0
        
    # check rows
    for row in arr:
        consecutive_count = 0
        for i in range(len(row)):
            if row[i] == char:
                consecutive_count += 1
                if consecutive_count == n:
                    count += 1
                    consecutive_count = 0
            else:
                consecutive_count = 0
    
    # check columns
    for j in range(len(arr[0])):
        consecutive_count = 0
        for i in range(len(arr)):
            if arr[i][j] == char:
                consecutive_count += 1
                if consecutive_count == n:
                    count += 1
                    consecutive_count = 0
            else:
                consecutive_count = 0
    
    # check diagonals
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if i + n <= len(arr) and j + n <= len(arr[0]):
                # check diagonal from top-left to bottom-right
                consecutive_count = 0
                for k in range(n):
                    if arr[i+k][j+k] == char:
                        consecutive_count += 1
                        if consecutive_count == n:
                            count += 1
                            consecutive_count = 0
                    else:
                        consecutive_count = 0
                        
                # check diagonal from bottom-left to top-right
                consecutive_count = 0
                for k in range(n):
                    if arr[i+n-1-k][j+k] == char:
                        consecutive_count += 1
                        if consecutive_count == n:
                            count += 1
                            consecutive_count = 0
    
    if count != 0:
        
        if n == 2:
            count = count - NUM_IN_A_ROW(arr, 4, char)*3 - NUM_IN_A_ROW(arr, 3, char)*2
        if n == 3:
            count = count - NUM_IN_A_ROW(arr, 4, char)*2
    
    return count


stub =      [[0,0,0,0,0,0,0],
             [0,0,0,1,0,0,0],
             [0,0,1,0,0,0,0],
             [0,0,0,1,0,0,0],
             [0,0,0,0,1,0,0],
             [0,0,0,0,0,0,0]]

print(NUM_IN_A_ROW(stub, 4, 1))
print(NUM_IN_A_ROW(stub, 3, 1))
print(NUM_IN_A_ROW(stub, 2, 1))