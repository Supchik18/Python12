import math

while True:
    
    print("�������� ��������:")
    print("1. ��������")
    print("2. ���������")
    print("3. ���������")
    print("4. �������")
    print("5. ���������� � �������")
    print("6. ���������� ������")
    print("7. ����� 1 ������� �� �����")
    print("8. ����� ��������� �����")
    print("9. ����� �� ���������")
    print("10. �����")
    print("11. �������")
    print("12. �������")
    while True:
        try:
            choice = int(input("������� ����� ��������: "))
            break
        except ValueError:
            print ("����� ������ �����, � �� �����")
    if choice == 1:
        try:
            num1 = float(input("������� ������ �����: "))
            num2 = float(input("������� ������ �����: "))
            result = num1 + num2
            print("���������:", result)
        except ValueError:
            print("����� ������ �����,� �� �����")
    elif choice == 2:
        try:
            num1 = float(input("������� ������ �����: "))
            num2 = float(input("������� ������ �����: "))
            result = num1 - num2
            print("���������:", result)
        except ValueError:
            print("����� ������ �����,� �� �����")
    elif choice == 3:
        try:
            num1 = float(input("������� ������ �����: "))
            num2 = float(input("������� ������ �����: "))
            result = num1 * num2
            print("���������:", result)
        except ValueError:
            print("����� ������ �����,� �� �����")
    elif choice == 4:
        try:
            num1 = float(input("������� ������ �����: "))
            num2 = float(input("������� ������ �����: "))
            result = num1 / num2
            print("���������:", result)
        except ValueError:
            print("����� ������ �����,� �� �����")
    elif choice == 5:
        try:
            num1 = float(input("������� �����: "))
            power = int(input("������� �������: "))
            result = num1 ** power
            print("���������:", result)
        except ValueError:
            print("����� ������ �����,� �� �����")
    elif choice == 6:
        try:
            choice = int(input("������� ����� "))
            print("��������� ",choice**0.5)
        except ValueError:
            print("����� ������ �����,� �� �����")
    elif choice == 7:
        try:
            num = float(input("������� �����: "))
            result = num * 0.01
            print("���������:", result)
        except ValueError:
            print("����� ������ �����,� �� �����")
    elif choice == 8:
        try:
            num = int(input("������� �����: "))
            result = 1
            for i in range(1, num + 1):
                result *= i
            print("���������:", result)
        except ValueError:
            print("����� ������ �����,� �� �����")
    elif choice == 9:
        try:
            break
        except ValueError:
            print("����� ������ �����,� �� �����")
    elif choice == 10:
        try:
            num = float(input("������� �����: "))
            result = math.sin(num)
            print("���������:", result)
        except ValueError:
            print("����� ������ �����,� �� �����")
    elif choice == 11:
        try:
            num = float(input("������� �����: "))
            result = math.cos(num)
            print("���������:", result)
        except ValueError:
            print("����� ������ �����,� �� �����")
    elif choice == 12:
        try:
            num = float(input("������� �����: "))
            result = math.tan(num)
            print("���������:", result)
        except ValueError:
            print("����� ������ �����,� �� �����")
