from roy import get_name as get_name_member1
from Abraham import get_name as get_name_member2
from Andre import get_name as get_name_member3
from Derrick import get_name as get_name_member4
from calson import get_name as get_name_member5
from WenTao import get_name as get_name_member6

def team_introduction():
    # 打印团队介绍
    print("This is Team CND. We are：")

    # 打印每个团队成员的名字
    print(get_name_member1())
    print(get_name_member2())
    print(get_name_member3())
    print(get_name_member4())
    print(get_name_member5())
    print(get_name_member6())
    
if __name__ == "__main__":
    team_introduction()