def add(a, b):
    return a + b

# _ : snake_case 사용 (파이썬, 데이터베이스 필드명)
# getInfo() : camelCase 사용 ()
PI = 3.141952
def number_input():
    output = input("숫자 입력 ")
    return float(output)

def get_circ(radius):
    return 2 * PI * radius

def get_area(radius):
    return PI * radius * radius


# 함수 실행
if __name__ == "__main__":
    print("module 내부", get_circ(5))
    print("module 외부", get_circ(5))