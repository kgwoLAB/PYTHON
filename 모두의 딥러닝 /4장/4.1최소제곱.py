import numpy as np
# numpy 배열
x = np.array([2,4,6,8])
y = np.array([81, 93, 91, 97])

# 평균
mx = np.mean(x)
my = np.mean(y)

# 기울기 공식 
# 분모
divisor = sum([(i-mx)**2 for i in x])

# 분자
def top(x, mx, y, my):
    d = 0
    for i in range(len(x)):
        d += (x[i] - mx) * (y[i] - my)
    return d

dividend = top(x,mx,y,my)

# 기울기 
a = dividend /divisor

# 절편
b = my - (mx*a)

print("기울기",a)
print("전편",b)


