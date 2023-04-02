"""
9. Write a Python program to display the examination schedule. (extract the date from exam_st_date). Go to the editor
exam_st_date = (11, 12, 2014)
Sample Output : The examination will start from : 11 / 12 / 2014
"""
exam_st_date = (11,12,2014)
print( "The examination will start from : %d / %d / %d"%exam_st_date)


print("=================================================================")
exam_date=(1,1,2023)
print(type(exam_date))
str2=str(exam_date)
print(str2)
print(type(str2))
exam_date3=str2.replace(",","/")
print(exam_date3)
exam_0=int(exam_date3[1])
exam_1=int(exam_date3[4])
exam_2=int(exam_date3[7:11])

tuple2=(exam_0,exam_1,exam_2)

print(exam_0,exam_1,exam_2)

#exam_date=tuple(exam_date3)

print(tuple2)
print(type(tuple2))