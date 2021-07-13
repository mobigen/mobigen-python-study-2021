1.	python 의 list / tuple 의 차이점이 뭘까요?
	1) list
       a) 수정가능	
	2) tuple
	   a) 수정 불가능
	   b) list 보다 작다
	   a= (1,2,3,4,5,6,7,8,9,0)
	   b= [1,2,3,4,5,6,7,8,9,0]

	   print('a=',a.__sizeof__())
       print('b=',b.__sizeof__())
	   

2.	python 의 특징은 뭐가 있을 까요?
	1) 변수의 타입을 정하지 않아도 자동으로 추측한다.
	2) interpreter가 소스를 라인단위로 해석한다.
	
3.	array / list 의 공통점 / 차이점이 뭐가 있을까요?
	1) 공통점 
	수정가능하고 값이 유일한 값(unique)일 필요없다.
	2) 차이점
	array는 데이터 타입이 동일해야 하고, list는 데이터 타입이 달라도 된다.

4.	dict 의 특징은 뭘까요?
	key, value로 구성되어 있다.

5.	imutable / mutable 객체는 뭐가 있나요?
	1) imutable
	tuple,string,number
	2) mutable
	list,set,dict

6.	split() join() 함수가 무엇 인가요?
	1) split
	데이터를 구분자를 기준으로(delimiter) 자른다.
	2) join
	list 데이터등을 구분자을 붙여 연결한다.

7.	iterable 이란 무엇 인가요?
	for 문을 이용해서 데이터를 순회할 수 있다.
	1) iterable unpacking
	grades = [("Ashley", 93), ("Brad", 95), ("Cassie", 84)]
	for entry in grades:
		print(entry)
	2) enumerating iterable
	for entry in enumerate("abcd"):
        print(entry)
	
	

