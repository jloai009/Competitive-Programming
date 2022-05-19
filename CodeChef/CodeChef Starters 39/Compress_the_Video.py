T = int(input())

for _ in range(T):
    N = int(input())
    frame_values = input().split()
    min_frames = min(N, 1)
    for i in range(len(frame_values)-1):
        if frame_values[i] != frame_values[i+1]:
            min_frames += 1
            
    print(min_frames)