class Student: #類別定義屬性 #物件是類別的實體 #方法是物件可以做甚麼事
    def __init__(self,new_gender,new_major,new_id): #建構子 #self實體化一定要
        self.__gender=new_gender #兩個下底線變成private下面記得改
        self.major=new_major
        self.id=new_id

    def set_gender(self, new_gender): #用getter setter取用屬性
        if new_gender == 'm' or new_gender == 'f':
            self.__gender = new_gender
        else:
            print('====請傳入"m"或"f"====')

    def join_class(self): #方法定義
        pass
    def quit_class(self): #方法定義
        pass
studentA = Student('m','工管系','B10721036') #類別實體化成物件student
studentA.__gender='F' #改性別 #物件點屬性
print(studentA.__gender)
print(studentA.major)
studentA.join_class() #呼叫物件join_class方法括號里不用打self #物件點方法
studentA.set_gender('d')
