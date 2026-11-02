#L=length
#W=width

L, W=input().split()
L=float(L)
W=float(W)

Area=L*W
Perimeter=(2*L)+(2*W)

print(f"Area= {Area:.2f}", f"Perimeter= {Perimeter:.2f}")
#or print(f"{Area:.2f}{Perimeter:.2f}") #cara lain untuk print tanpa ruang antara nilai.")
