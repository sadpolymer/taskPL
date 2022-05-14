try:
	from sys import argv
	script, n, m = argv
	n = int(n)
	m = int(m)
	if n > 0 and m > 0:
    		target = n + 1
    		dif = m - 1
    		array=[]
    		k = 1
    		while k != target:
      			array.append(k)
      			k = k + dif
      			if k > target:
        			#k = k - dif
        			#k = (dif - (n - k))
        			k = k - n
	else:print("Оба значения должны быть больше нуля.")
	answer = ''.join(str(e) for e in array)
	print(answer);
except Exception:
	print("Введите корректное значение.");



