# 10번


# 11번
def get_final_position(N,matrix,move_list):
    directs = [(-1,0),(1,0),(0,-1),(0,1)]
    cur_r,cur_c = 0, 0
    
    for r in range(N):
        for c in range(N):
            if matrix[r][c] == 1:
                cur_r, cur_c = r, c
                break
        else:
            continue
        break
    
    for move in move_list :
        cur_r += directs[move][0]
        cur_c += directs[move][1]
        if cur_r < 0 or cur_r >= N or cur_c < 0 or cur_c >= N:
            return None
        
    return [cur_r,cur_c]