import pandas as pd
    
    
def DBA():
    #code to read excel
    df=pd.read_excel("D:\\Ph.D\\Amity Ph.D\\1st Journal Paper\\Code Python FCFS\\Test.xlsx")
    #df
    df['successful'] = pd.Series([0 for x in range(len(df.index))])
    row_list =[]
    excel_data=[]
    copy_excel=[]
      
    # Iterate over each row
    for index, rows in df.iterrows():
      my_list=[]
      my_list =[rows.Tasks,rows.n,rows.AT,rows.ST, rows.Dur,rows.DL,rows.Size,rows.successful]
      #print(my_list)
      row_list.append(my_list)
      excel_data.append(my_list)
      copy_excel.append(my_list)


    print("\n-------------------------- Data Set from excel ---------------------------")
    print("Id---VM---AT----ST----Dur---DLT---Size---Execstatus")
    for xs in row_list:
         print("--".join(map(str, xs)))

    #print(row_list)
    # from operator import length_hint
    # size=length_hint(row_list)
    #print(size)
    task=0
    n=1
    AT=2
    ST=3
    Dur=4
    DL=5
    Size=6
    successful=7
    # Code to fing the simailr tasks among the gievn set
    row_list.sort(key = lambda row_list:row_list[AT])
    row_list
    final=[]
    for i in range(len(row_list)):
      j=i+1
      while(j<len(row_list) ):
        if(row_list[i][n]==row_list[j][n] and row_list[i][ST]==row_list[j][ST] and row_list[i][DL]==row_list[j][DL]):
          x=row_list[i]
          y=row_list[j]
          final.append(x)
          final.append(y)    
          break
        j=j+1
    #print("1.  ============================")
    #print(final)

    my_set = set(tuple(x) for x in final)
    similartask=list(my_set)
    similartask.sort()
    #similartask



    slc_task=[]
    from operator import length_hint
    len_of_slc_task=length_hint(slc_task)
    for i in range(len(similartask)):
      my_list =[similartask[i][task],similartask[i][AT],similartask[i][Dur],similartask[i][Size]]
      #print(my_list)
      slc_task.append(my_list)
    print("\n-------------------------- Similar Taks ---------------------------")
    print("Id---ST----Dur---Size")
    for xs in slc_task:
         print("--".join(map(str, xs)))



    AT1=1
    Dur1=2
    Size1=3
    task1=0
    arrival=[]
    duration=[]
    size2=[]

    ## Code to create the Z matrix
    from operator import length_hint
    len_of_slc_task=length_hint(slc_task)
    for i in range(len(slc_task)):
      x=slc_task[i][AT1]
      y=slc_task[i][Dur1]
      z=slc_task[i][Size1]
      arrival.append(x)
      duration.append(y)
      size2.append(z)

    min_AT=min(arrival)
    min_Size=min(size2)
    min_Dur=min(duration)
    #print(size2)
    #print(min_AT,min_Size,min_Dur)
    from statistics import mean
    avg_AT=mean(arrival)
    avg_Dur=mean(duration)
    avg_Size=mean(size2)
    #print(avg_AT,avg_Size,avg_Dur)
    import statistics
    sd_AT= statistics.pstdev(arrival)
    # next line added ABG
    sd_AT = 0.005 if(sd_AT == 0.0) else sd_AT
    sd_Dur= statistics.pstdev(duration)
    sd_Size= statistics.pstdev(size2)

    #from operator import length_hint
    #len_of_slc_task=length_hint(slc_task)
    print(sd_AT,sd_Size,sd_Dur)
    w=[0,min_AT,min_Dur,min_Size]
    slc_task.append(w)
    for i in range(len(slc_task)):
            slc_task[i][AT1]=round((((slc_task[i][AT1]-avg_AT)/sd_AT)),4)        
            slc_task[i][Dur1]=round(((slc_task[i][Dur1]-avg_Dur)/sd_Dur),4)
            slc_task[i][Size1]=round(((slc_task[i][Size1]-avg_Size)/sd_Size),4)


    print("\n--------------------------Z Matrix ---------------------------")
    print("Id------ST------Dur-----Size")
    for xs in slc_task:
         print("--".join(map(str, xs)))


    square=[]
    for i in range(len(slc_task)-1):
      x=round(pow((slc_task[i][AT1]-slc_task[len(slc_task)-1][AT1]),2),4)
      y=round(pow((slc_task[i][Dur1]-slc_task[len(slc_task)-1][Dur1]),2),4)
      z=round(pow((slc_task[i][Size1]-slc_task[len(slc_task)-1][Size1]),2),4)
      my_list=[slc_task[i][task1],x,y,z]
      square.append(my_list)
    print("\n--------------------------Square Matrix ---------------------------")
    print("Id------ST------Dur-----Size")
    for xs in square:
         print("--".join(map(str, xs)))

    import math
    rank=[]

    for i in range(len(square)):
      x=round(square[i][AT1]+square[i][Dur1]+square[i][Size1],4)
                                                 
      y=round((math.sqrt(x)),4)
      my_list=[square[i][task1],x,y]
      
      rank.append(my_list)
    sum=1
    sqt_rt=2

    rank.sort(key = lambda test_list: test_list[sum])
    rank

    copy=rank
    print("\n--------------------------Ranked Matrix ---------------------------")
    print("Id----Sum-----Sqrt")
    for xs in copy:
         print("--".join(map(str, xs)))

    copy_row_list=copy_excel



    l=[]
    for i in range(len(row_list)):
      for j in range(len(rank)):
        if(row_list[i][0]==rank[j][0]):
          #print(rank[j][0])
          l.append(i)
    #print(l)
    for i in range(len(l)):
      x=int(rank[i][0])
      excel_data[l[i]][task]=rank[i][0]
      excel_data[l[i]][n]=copy_row_list[x-1][n]
      excel_data[l[i]][AT]=copy_row_list[x-1][AT]
      excel_data[l[i]][ST]=copy_row_list[x-1][ST]
      excel_data[l[i]][Dur]=copy_row_list[x-1][Dur]
      excel_data[l[i]][DL]=copy_row_list[x-1][DL]
      excel_data[l[i]][Size]=copy_row_list[x-1][Size]
      
    print("\n--------------------------Ranked merged with org Task Matrix ---------------------------")
    print("Id---VM---AT----ST----Dur---DLT---Size---Execstatus")
    for xs in excel_data:
         print("--".join(map(str, xs)))

    copy_row_list=copy_excel


    clock=row_list[0][ST]
    vm_total=8
    # code to run the tasks as per Queue
    for i in range(len(excel_data)):
      if(clock<excel_data[i][DL]):
        rem_vm=vm_total-excel_data[i][n]
        duration=round((excel_data[i][Dur])/60,2)
        currST=excel_data[i][ST] # currST is the start time of the current running task
        j=i+1                     # 'j' here stands for next task in queue
        excel_data[i][7]=1        # declaring status as executed for current task
        clock=clock+duration     # clock moves to next stage after running for a 'duration'
        
        #test_list.pop(1)
        # while loop for running the tasks in parallel 
        while(j<len(excel_data) and rem_vm<=8):
         # print("\ni =",i, " j =",j)
          if(excel_data[j][n]<=rem_vm and excel_data[j][ST]<=currST and excel_data[j][DL]<clock):
            rem_vm=rem_vm-row_list[j][n]  # Ques
             
            if(excel_data[j][Dur]<duration): 
              excel_data[j][7]=1
              break;
            else:
              excel_data[j][Dur]=round(excel_data[j][Dur]-duration,2)  
              break;  
                
          else:
            j=j+1
        #clock=clock+duration
    print("\n--------------------------Final Execution---------------------------")
    print("Id---VM---AT----ST----Dur---DLT---Size---Execstatus")
    for xs in excel_data:
         print("--".join(map(str, xs)))
         
         
'''
****************************
Code for FCFS
****************************
'''
def FCFS():

    #Code to read data from excel
    df=pd.read_excel("D:\\Ph.D\\Amity Ph.D\\1st Journal Paper\\Code Python FCFS\\Test.xlsx")
    #print(df)
    df['successful'] = pd.Series([0 for x in range(len(df.index))])
    row_list =[]
      
    # Iterate over each row
    for index, rows in df.iterrows():
      my_list=[]
      my_list =[rows.Tasks,rows.n,rows.AT,rows.ST, rows.Dur,rows.DL,rows.Size,rows.successful]
      #print(my_list)
      row_list.append(my_list)
    print("\n")
    print("----------Dataset simulated for 15 Tasks is ------------")
    print("\n")
    print("Id---VM---AT---ST---Dur---DLT---Size---Execstatus")
    
    for xs in row_list:
         print("--".join(map(str, xs)))
    
    # Finding the size of data set
    from operator import length_hint
    size=length_hint(row_list)
    #print(size)
    task=0
    n=1
    AT=2
    ST=3
    Dur=4
    DL=5
    Size=6
    successful=7
    row_list.sort(key = lambda row_list: row_list[AT])
    print("\n")
    print("---------- Dataset as per FCFS (sorted as per Arrival time) ------------")
    print("\n")
    print("Id---VM---AT---ST---Dur---DLT---Size---Execstatus")
    
    for xs in row_list:
         print("--".join(map(str, xs)))
    
    
    #Sorting data set FCFS
   
    row_list.sort(key = lambda row_list: row_list[ST])
    print("\n")
    print("---------- Dataset as per FCFS (sorted as per Start time) ------------")
    print("\n")
    print("Id---VM---AT---ST---Dur---DLT---Size---Execstatus")
    
    for xs in row_list:
         print("--".join(map(str, xs)))
    
    #code for running  backfill tasks in parallel
    clock=row_list[0][ST]
    vm_total=8
    for i in range(size):
      if(clock<row_list[i][DL]):
        rem_vm=vm_total-row_list[i][n]
        duration=(row_list[i][Dur])/60
        x=row_list[i][ST]
        j=i+1
        row_list[i][7]=1
        clock=clock+duration
        
        #test_list.pop(1)
        while(j<size and rem_vm<=8):
          if(row_list[j][n]<=rem_vm and row_list[j][ST]<=x and row_list[j][DL]<clock):
            rem_vm=rem_vm-row_list[j][n]
            if(row_list[j][Dur]<duration): 
              row_list[j][7]=1
              break;
            else:
              row_list[j][Dur]=round(row_list[j][Dur]-duration,2) 
              break; 
                
          else:
            j=j+1
        #clock=clock+duration
    print("\n")
    print("----------Final task status--------------- ")
    print("\n")
    print("Id---VM---AT---ST---Dur---DLT---Size---Execstatus")
    
    for xs in row_list:
         print("--".join(map(str, xs)))
        
userInput = int(input("Choice which code to run 1: for FCFS, 2: for DBA\n"))
if userInput == 1:
    #print("test")
    FCFS()
else:
    DBA()
