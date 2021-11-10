s=([70, 85, 80,70,80], [80,70,80,50,90], [90,80,70,90,80])
rows = len(s)
cols = len(s[0])
hap=0

for r in range(rows):
    for c in range(cols):
        hap=s[r][c] +hap
    print("%d" %hap)
    hap=0