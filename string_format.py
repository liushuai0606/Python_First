department1 = 'Security'
department2 = 'Python'
depart1_m = 'cq_bomb'
depart2_m = 'qinke'
COURSE_FEES_SEC = 456789.123456
COURSE_FEES_Python = 1234.3456
#方法1
#line1 = 'Department1 name:%-10s Manager:%-10s COURSE FEES:%-10.2f The End!' % (department1,depart1_m,COURSE_FEES_SEC)
#line2 = 'Department2 name:%-10s Manager:%-10s COURSE FEES:%-10.2f The End!' % (department2,depart2_m,COURSE_FEES_Python)
#方法2
#line1 = 'Department1 name:{0:<15} Manager:{1:<15} COURSE FEES:{2:<15.2f} The End!' .format (department1,depart1_m,COURSE_FEES_SEC)
#line2 = 'Department2 name:{0:<15} Manager:{1:<15} COURSE FEES:{2:<15.2f} The End!' .format (department2,depart2_m,COURSE_FEES_Python)
#方法3
line1 = f'Department1 name:{department1:<20} Manager:{depart1_m:<20}  COURSE FEES:{COURSE_FEES_SEC:<20.2f} The End!'
line2 = f'Department1 name:{department2:<20} Manager:{depart2_m:<20}  COURSE FEES:{COURSE_FEES_Python:<20.2f} The End!'

length = len(line1)
print('='*length)
print(line1)
print(line2)
print('='*length)