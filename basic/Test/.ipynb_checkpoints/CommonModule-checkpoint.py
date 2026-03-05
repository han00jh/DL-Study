 
# -----------------------------------------------------------------------------------

class MyCalcClass :

    point = 100

    def myprint(self):
        print("..." + self)

    def add(a, b):
        print("basic/Test/ > CommonModule.py > MyCalcClass > add() ")
        return a + b

    def adds(self, a, b):
        print("basic/Test/ > CommonModule.py > MyCalcClass > add() ")
        return a + b

    def mul(a, b):
        print("basic/Test/ > CommonModule.py > MyCalcClass > mul() ")
        return a * b


# -----------------------------------------------------------------------------------


''' **클래스(Class)와 인스턴스(Object)**가 메모리에 어떻게 로드되는지 확인 '''

''' 생성자 함수  ->  Memory Loaded _ 메모리 초기화(새 주소(memory)에 저장) '''
addr1 = MyCalcClass( )
addr2 = MyCalcClass( )

print(addr1)                # <__main__.MyCalcClass object at 0x00000260C9E87FA0>
print(addr2)                # <__main__.MyCalcClass object at 0x00000260C9E87F10>

print(MyCalcClass)          # <class '__main__.MyCalcClass'>

print(MyCalcClass.__dict__) # {'__module__': '__main__'
                            #  , 'point': 100
                            #  , 'add': <function MyCalcClass.add at 0x000002273EC46C20>
                            #  , 'mul': <function MyCalcClass.mul at 0x000002273EC46CB0>
                            #  , '__dict__': <attribute '__dict__' of 'MyCalcClass' objects>
                            #  , '__weakref__': <attribute '__weakref__' of 'MyCalcClass' objects>
                            #  , '__doc__': None}

# -----------------------------------------------------------------------------------

print(addr1.__dict__)       # {}
print(addr1.__dir__)        # <built-in method __dir__ of MyCalcClass object at 0x000002273EB3A1D0>

print(addr2.__dict__)       # {}
print(addr2.__dir__)        # <built-in method __dir__ of MyCalcClass object at 0x000002273EB3AB60>

# -----------------------------------------------------------------------------------


print(dir(addr1))           # [ (각종 내장 함수들), 'add', 'mul', 'point']
print(dir(addr2))           # [ (각종 내장 함수들), 'add', 'mul', 'point']
# 즉, addr1.add로 호출 시,
# MyCalcClass 내 add가 호출된게 아니라, addr1의 add가 호출됨


#MyCalcClass.myprint()       # TypeError: MyCalcClass.myprint() missing 1 required positional argument: 'self'
MyCalcClass.myprint("a")    # ...a

addr1.add(5,5)           # TypeError: MyCalcClass.add() takes 2 positional arguments but 3 were given
addr1.myprint("a")          # TypeError: MyCalcClass.myprint() takes 1 positional argument but 2 were given


# -----------------------------------------------------------------------------------


''' 함수 이름(key)이 같으면 안되는 이유 : 기존 주소(value_1)를 덮어버리고 최종 주소(value_2) 1개만 남는다.'''
''' 최종 출력 값 { key : value_2 } => Python만 이렇게 저장됨 '''

# 파이썬은 설계상 인스턴스 메서드를 호출할 때 인스턴스(self)를 자동으로 넘겨주기로 약속되어 있습니다.
# 즉, addr1의 주소가 자동으로 들어가게 되어있음


# -----------------------------------------------------------------------------------


''' 인스턴스 메서드 (Instance Method) '''
# Class 내부에서 정의된 함수에 인자로 self를 가지는 경우, -> ''' 자체 생성 및 사용 '''
#   외부 호출 시 반드시 주소가 날라가야함 (새로 정의(addr1=MyClacClass)해서 호출해야함)
#   외부 호출으로 사용 절대 불가 (물론 파이썬은 넘기기는하는데, 다른 언어는 다 Error)
#       self는 **객체 고유의 저장소(__dict__)**에 접근할 수 있는 '열쇠' 역할

''' 정적 메서드 (Static Method) '''
# Class 내부 함수에 인자로 self가 없는 경우,            -> ''' 기존 class 함수 가져옴 '''
#   외부 호출 시, 해당 Class 명으로 호출해줘야함 (주소만 저장하는거고 함수를 가져오는건 아님)


''' cf. 클래스 메서드(Class Method) '''
# Class 내부 함수에 인자로 cls가 있는 경우,
#   - self는 생성된 객체의 주소가 참조 대상
#   - cls는  클래스 파일의 주소가 참조 대상


# -----------------------------------------------------------------------------------

''''''''''''''' cf. 숨김 변수 '''''''''''''''

''' 1. 진짜 숨기고 싶을 때: 던더(Double Underscore) __ 
        변수명 앞에 언더바를 두 개(__) 붙이면 파이썬이 이름을 내부적으로 바꿔버려서 
        외부에서 직접 부를 수 없게 만듭니다. 이를 **네임 맹글링(Name Mangling)**이라고 합니다.'''
class MyCalcClass:
    def __init__(self):
        self.__point = 100  # 외부에서 접근 불가능하게 숨김
        self.name = "Public" # 외부에서 접근 가능

addr1 = MyCalcClass()
print(addr1.name)     # 출력: Public
# print(addr1.__point) # 에러 발생! (AttributeError)



''' 2. "조심해줘"라는 신호: 싱글 언더바 _
        언더바를 하나만 붙이는 것은 문법적으로 막지는 않지만, 
        개발자들 사이에서 **"이건 내부용이니까 밖에서 수정하지 마!"**라는 강력한 경고 신호로 통합니다. '''
class MyCalcClass:
    def __init__(self):
        self._internal_value = 10  # 약속된 숨김 변수

addr1 = MyCalcClass()

# 1. 일반적인 출력
print(addr1._internal_value)    # 출력: 10

# 2. 객체의 내부 상태(__dict__) 확인
print(addr1.__dict__)           # 출력: {'_internal_value': 10}



''' 3. 숨긴 변수를 안전하게 가져오거나 바꾸는 법 (Getter/Setter)
        변수를 숨겼다면, 대신 그 값을 안전하게 주고받을 통로(함수)를 만들어주는 것이 정석입니다.'''
class MyCalcClass:
    def __init__(self):
        self.__point = 100

    # 값을 확인하는 통로 (Getter)
    def get_point(self):
        return self.__point

    # 값을 수정하는 통로 (Setter)
    def set_point(self, value):
        if value < 0:
            print("점수는 0보다 작을 수 없습니다!")
        else:
            self.__point = value

addr1 = MyCalcClass()
addr1.set_point(150)   # 안전하게 수정
print(addr1.get_point()) # 안전하게 가져오기

# -----------------------------------------------------------------------------------
