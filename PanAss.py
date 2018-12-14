#!/usr/bin/env python
# coding: utf-8

# In[24]:


import pandas as pd
import numpy as np
school_data_to_load = "schools_complete.csv"
student_data_to_load = "students_complete.csv"

school_data = pd.read_csv(school_data_to_load)
student_data = pd.read_csv(student_data_to_load)

school_data_complete = pd.merge(student_data, school_data, how="left", on=["school_name", "school_name"])


# In[25]:


school_data_complete.head()


# In[26]:


number_students= school_data_complete["student_name"].count()
number_students


# In[27]:


number_schools= school_data_complete["school_name"].unique()
len(number_schools)


# In[ ]:





# In[28]:


budget=school_data_complete["budget"].sum() 
budget


# In[29]:


math= school_data_complete["math_score"]
math_one= math.sum()
math_two= math.count()
math_average= math_one/math_two
math_average


# In[30]:





reading= school_data_complete["reading_score"]
reading_one= reading.sum()
reading_two= reading.count()
reading_average= reading_one/reading_two
reading_average


# In[31]:


overal_score= (math_average + reading_average)/2
overal_score


# In[32]:


pass_math= school_data_complete.loc[school_data_complete["math_score"]>=70,:]
pass_math_one= pass_math["math_score"].sum()
pass_math_two= pass_math["math_score"].count()
pass_math_average= pass_math_one/pass_math_two
pass_math_average


# In[33]:


pass_read= school_data_complete.loc[school_data_complete["reading_score"]>=70,:]
pass_read_one= pass_read["math_score"].sum()
pass_read_two= pass_read["math_score"].count()
pass_read_average= pass_read_one/pass_read_two
pass_read_average
overal_score_pass= (pass_math_average + pass_read_average)/2
overal_score_pass

summary_table= pd.DataFrame({"Total Schools":[len(number_schools)],
                            "Total Students":[number_students],
                            "Total Budget":[budget],
                            "Average Math Score":[math_average],
                            "Average Reading Score":[reading_average],
                            "% Passing Math":[pass_math_average],
                            "% Passing Reading":[pass_read_average],
                            "% Overall Passing Rate":[overal_score_pass]})
summary_table


# In[34]:


school_data_complete.head()


# In[35]:


number_schools= school_data_complete["school_name"].unique()
number_schools


# In[36]:


group_school= school_data_complete.groupby(["school_name"]) 
group_school


# In[37]:


group_rd_score=group_school["reading_score"].mean()
group_rd_score


# In[38]:


group_math_score= group_school["math_score"].mean()
group_math_score


# In[39]:


budget= group_school["budget"].mean()
budget


# In[40]:


count_student= group_school["student_name"].count()
count_student


# In[41]:


overal_score= (group_rd_score+group_math_score)/2
overal_score


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[42]:


group_mean = group_school["reading_score"].mean()
group_mean_R= group_mean[group_school["reading_score"].mean()>70]
group_mean_R


# In[43]:


group_mean = group_school["math_score"].mean()
group_mean_M= group_mean[group_school["math_score"].mean()>70]
group_mean_M


# In[72]:


group_type= group_school["type"].describe()["top"]
group_type


# In[73]:


budged_per_student= budget/count_student
budged_per_student


# In[74]:


overal_pass_mean= (group_mean_M + group_mean_R)/2 
overal_pass_mean
summary_school=({"School Type":group_type,
                 "Total Students":count_student,
                 "Total Budget":budget,
                 "Per Student Budget":budged_per_student,
                 "Average Math Score":group_math_score,
                 "Average Reading Score":group_rd_score,
                 "% Passing Math":group_mean_M,
                 "% Passing Reading":group_mean_R,
                 "% Overall Passing Rate":overal_pass_mean,})  

summary_school=pd.DataFrame(summary_school)
summary_school


# In[75]:


summary_school_top= summary_school.sort_values(["% Overall Passing Rate"],ascending=False)
summary_school_top.head(5)


# In[76]:


summary_school_botton= summary_school.sort_values(["% Overall Passing Rate"],ascending=True)
summary_school_botton.head(5)


# In[ ]:





# In[77]:


math_grade= school_data_complete.loc[:,["grade","school_name","math_score"]]
math_grade.head()


# In[ ]:





# In[78]:


mgnine= math_grade.loc[math_grade["grade"]=="9th",:].groupby(["school_name"])
mgnine.mean()


# In[79]:


mgnten= math_grade.loc[math_grade["grade"]=="10th",:].groupby(["school_name"])
mgnten.mean()


# In[80]:


mgneleven= math_grade.loc[math_grade["grade"]=="11th",:].groupby(["school_name"])
mgneleven.mean()


# In[81]:


mgntwelve= math_grade.loc[math_grade["grade"]=="12th",:].groupby(["school_name"])
mgntwelve.mean()


# In[82]:


math= ({"9th":mgnine.mean()["math_score"],
        "10th":mgnten.mean()["math_score"],
        "11th":mgneleven.mean()["math_score"],
        "12th":mgntwelve.mean()["math_score"],})

math= pd.DataFrame(math)
math


# In[83]:


rd_grade= school_data_complete.loc[:,["grade","school_name","reading_score"]]
rd_grade.head()


# In[84]:


rdnine= rd_grade.loc[rd_grade["grade"]=="9th",:].groupby(["school_name"])
rdnine.mean()


# In[85]:


rdten= rd_grade.loc[rd_grade["grade"]=="10th",:].groupby(["school_name"])
rdten.mean()


# In[86]:


rdeleven= rd_grade.loc[rd_grade["grade"]=="11th",:].groupby(["school_name"])
rdeleven.mean()


# In[87]:


rdtwelve= rd_grade.loc[rd_grade["grade"]=="12th",:].groupby(["school_name"])
rdtwelve.mean()


# In[88]:


rd= ({"9th":rdnine.mean()["reading_score"],
      "10th":rdten.mean()["reading_score"],
      "11th":rdeleven.mean()["reading_score"],
      "12th":rdtwelve.mean()["reading_score"],})

rd= pd.DataFrame(math)
rd


# In[89]:




b_p_s= pd.DataFrame({"Per Student Budget":budged_per_student,
                     "Average Math Score":group_math_score,
                     "Average Reading Score":group_rd_score,
                     "% Passing Math":group_mean_M,
                     "% Passing Reading":group_mean_R,
                     "% Overall Passing Rate":overal_pass_mean})
b_p_s.head()


# In[90]:



bins= [0, 585, 615, 645, 675]
group_names = ["<$585", "$585-615", "$615-645", "$645-675"]

b_b = pd.cut(b_p_s["Per Student Budget"], bins, labels=group_names)
b_b


# In[91]:


b_p_s["Bin_Badget"]=b_b


# In[92]:


b_p_s.head()


# In[93]:


bins_badget= b_p_s.groupby("Bin_Badget")
bins_badget.mean().drop("Per Student Budget",axis=1)


# In[94]:


school_size= group_school["size"].mean()
school_size


# In[95]:


size= pd.DataFrame({"school_size":school_size,
                     "Average Math Score":group_math_score,
                     "Average Reading Score":group_rd_score,
                     "% Passing Math":group_mean_M,
                     "% Passing Reading":group_mean_R,
                     "% Overall Passing Rate":overal_pass_mean})
size.head()


# In[96]:


bins = [0, 1000, 2000, 5000]
group_names = ["Small (<1000)", "Medium (1000-2000)", "Large (2000-5000)"]

size["Bins_size"]=pd.cut(size["school_size"], bins, labels=group_names)
size.groupby("Bins_size").mean().drop("school_size",axis=1)


# In[97]:


#This is how I select the type
school_type= group_school["type"].describe()["top"]    
school_type.head()               


# In[98]:


type_pd= pd.DataFrame({"Average Math Score":group_math_score,
                    "Average Reading Score":group_rd_score,
                    "% Passing Math":group_mean_M,
                    "% Passing Reading":group_mean_R,
                    "% Overall Passing Rate":overal_pass_mean,
                    "school_type":school_type})
type_pd.head()


# In[99]:


group_type= type_pd.groupby(["school_type"])
group_type.mean()

Interpretation of the data:
    
1-The district type of school has lowers math score, reading score, average math passing score, average reading passing score and average overall passing score.
2-The large school has lowers math score, reading score, average math passing score, average reading passing score and average overall passing score.
3-The school with highest budget per students has lowers math score, reading score average passing math score, average reading passing score and overall passing score.























