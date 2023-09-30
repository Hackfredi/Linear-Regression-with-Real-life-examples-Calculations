#Program to predict price of pizza data required radius of pizza and price

import statistics

def calc():


    # Data input for x and y
    cons=int(input("Enter number of data "))

    #list for x and y
    x_indp=[]
    y_indp=[]

    for i in range(cons):

        # Data input for x
        data1=int(input("input data 1 "))
        x_indp.append(data1)

        # Data input for y
        data2=int(input("input data 2 "))
        y_indp.append(data2)

    #mean of x
    mean_x=statistics.mean(x_indp)

    #mean of y
    mean_y=statistics.mean(y_indp)

    #deviation of x
    dev_x=[]

    #deviation of y
    dev_y=[]

    for i in range(cons):

        #calculating deviation for x and adding answer to the list
        dev_x.append(x_indp[i]-mean_x)

        #calculating deviation for y and adding answer to the list
        dev_y.append(y_indp[i]-mean_y)
    
    #product of deviation
    p_dev=[]

    for i in range(cons):

        #calculating product of deviation and adding it to the list
        p_dev.append(dev_x[i]*dev_y[i])
    
    #sum of products of devation
    sum_p_dev=0

    for i in range(cons):

        #sum of products and adding to variable
        sum_p_dev=sum_p_dev+p_dev[i]

    #square of deviation of x
    sq_dev_x=[]

    for dev in dev_x:

        #calculating square of x 
        square=dev**2 
         
        #adding it in list
        sq_dev_x.append(square)

    #sum of square
    sum_sq_x=0
    
    for i in range(cons):

        #storing sum of square of deviation
        sum_sq_x=sum_sq_x+sq_dev_x[i]

    #calculating value of m
    m=sum_p_dev/sum_sq_x

    #calculating value of b
    b=mean_y-(mean_x*m)

    #printing m and b
    print(m)
    print(b)

    x=int(input("Enter number to be predict"))

    #predict the result
    y=(m*x)+b

    return y

predict=calc()

print(predict)