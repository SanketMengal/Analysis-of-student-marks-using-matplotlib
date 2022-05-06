'''
Project Name: Analysis of Student Performance Depending on Academic Marks and Sports Marks Using
Charts in Matplotlib:
Author : Akshay Mandalik,Sanket Mengal
Last Modified: 04/05/2022 03:27:00 AM
'''
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("StudentsPerformance.csv")


print("Overview\n")
print(f"{df.head()}\n")  # Inspecting the first 5 rows
print(f"{df.shape}\n")  # Shape of the Dataset

print("No. of missing cells in each column:\n") 
print(df.info())    # Basic Info.
print(df.isnull().sum()) # No. of missing cells in each column.


print("\nSummary:") 
print(f"{df.describe()}\n")     # Summary of Dataset





####################################### Data Visualization #########################################


def getUnique(arg):
   return  df[arg].unique()

def getCount(arg):
    return df[arg].value_counts().to_dict()

# 1. Gender: 
print("Gender:\n")
genderUniqueValues = getUnique('gender')
print(f"Distinct:{genderUniqueValues} ")

gender_dict = getCount('gender')
gender = list(gender_dict.keys())
no_of_male_female = list(gender_dict.values())


plt.bar(gender, no_of_male_female, color ='blue',width = 0.4)
plt.xlabel("Gender")
plt.ylabel("No. Of Students")
plt.title("Male and Female Students At School")
plt.show()

# 2. race / ethnicity: 
print("race/ethnicity:\n")
uniqueRace = getUnique('race/ethnicity')
print(f"Distinct:{uniqueRace}")

race_dict = getCount('race/ethnicity')
race = list(race_dict.keys())
no_of_each_race = list(race_dict.values())

cols = ['c','m','r','g','y']
plt.pie(no_of_each_race,labels=race,colors=cols,startangle=90,shadow= True,autopct='%1.1f%%')
plt.title('Race/ethnicity')
plt.show()


# 3. Parental Level Of Education: 
print("Parental Level Education:\n")
uniqueEducation = getUnique('parental level of education')
print(f"Distinct:{uniqueEducation}")

Edu_dict = getCount('parental level of education')
Education = list(Edu_dict.keys())
no_of_parents = list(Edu_dict.values())


plt.bar(Education, no_of_parents, color ='red',width = 0.4)
plt.xlabel("Education")
plt.ylabel("No. Of Parents")
plt.title("Parental Level Of Education")
plt.show()


# 4. test preparation course:

print("Test Preperation Course:\n ")
uniquetest = getUnique('test preparation course')
print(f"Distinct:{uniquetest}")

test_dict= getCount('test preparation course')
test = list(test_dict.keys())
noOfCompletedNoncompletedTest = list(test_dict.values())

plt.bar(test, noOfCompletedNoncompletedTest, color ='green',width = 0.4)
plt.xlabel("Test")
plt.ylabel("No. Of Students")
plt.title("Test preperation Course")
plt.show()

# 5. Math Score: 
math_score = df['math score'].tolist()
writing_score = df['writing score'].tolist()
reading_score = df['reading score'].tolist()

print("Math Score:\n")
uniquemathScore = getUnique('math score')
print(f"Distinct:{uniquemathScore}")

plt.scatter(math_score, writing_score, c ="blue")
plt.xlabel("Math Score")
plt.ylabel("Writing Score")
plt.show()

plt.scatter(math_score, reading_score, c ="blue")
plt.xlabel("Math Score")
plt.ylabel("Reading Score")
plt.show()


# 6. Comparing All Scores:

studentList = df['Student_number'].tolist()
math_score.sort(reverse=True)
writing_score.sort(reverse=True)
reading_score.sort(reverse=True)
plt.plot(studentList[0:100], math_score[0:100],   label = 'Math Score', marker='o', linewidth=3)
plt.plot(studentList[0:100], writing_score[0:100],   label = 'Writing Score',  marker='o', linewidth=3)
plt.plot(studentList[0:100], reading_score[0:100], label = 'Reading Score', marker='o', linewidth=3)

plt.xlabel('No. Of  Students')
plt.ylabel('Score')
plt.legend(loc='upper left')
plt.xticks([0,100])
plt.yticks([80,85,90,95,100])
plt.title('Students Score')
plt.show()