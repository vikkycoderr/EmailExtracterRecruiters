def seperater(firstName,lastName,format):
    user=""
    domain=""
    conditionD=False
    for a in format:
        if a=="@":
            conditionD=True
        if conditionD==True:
            domain+=a
        if conditionD==False:
            user+=a
    first=""
    second=""
    tempF=""
    tempL=""
    linebreak=""
    if "." in user:
        linebreak="."
    elif "]" in user:
       linebreak="]"
    index=0
    for c in user:
        if c!=linebreak:
            tempF+=c
        else:
            if  linebreak=="]":
                tempF+="]"
                index=user.find(linebreak)+1
            break
    conditionLast=False
    for d in user:
        if conditionLast==True:
            tempL+=d
        if d==linebreak:
            conditionLast=True
    if "jane.doe" in format:
        tempF="jane"
        tempL="doe"
        linebreak="."
    if tempF=="[first name]":
        first=firstName
    if tempF=="[first]":
        first=firstName
    if tempF=="first":
        first=firstName
    if tempF=="last":
        first=lastName
    if tempF=="[last name]":
        first=lastName
    if tempF=="[last]":
        first=lastName
    if tempF=="firstname":
        first=firstName
    if tempF=="lastname":
        first=lastName
    if tempF=="Firstname":
        first=firstName
    if tempF=="Lastname":
        first=lastName
    if tempF=="[first_name]":
        first=firstName
    if tempF=="[last_name]":
        first=lastName
    if tempF=="jane":
        first=firstName
    if tempF=="john":
        first=firstName
    if tempF=="j":
        first=firstName[0]
    if tempF=="doe":
        first=lastName
    if tempF=="d":
        first=lastName[0]
    if tempF=="Jane":
        first=firstName
    if tempF=="John":
        first=firstName
    if tempF=="J":
        first=firstName[0]
    if tempF=="Doe":
        first=lastName
    if tempF=="D":
        first=lastName[0]
    if tempF=="Smith":
        first=lastName
    if tempF=="S":
        first=lastName[0]
    if tempF=="smith":
        first=lastName
    if tempF=="s":
        first=lastName[0]
    if tempF=="[last_initial]":
        first=lastName[0]
    if tempF=="[last name initial]":
        first=lastName[0]
    if tempF=="firstinitial":
        first=firstName[0]
    if tempF=="lastinitial":
        first=lastName[0]
    if tempF=="[last initial]":
        first=lastName[0]
    if tempF=="[first_initial]":
        first=firstName[0]
    if tempF=="[first initial]":
        first=firstName[0]
    if tempF=="[first name initial]":
        first=firstName[0]
    if tempL=="[first name]":
        second=firstName
    if tempL=="[last name]":
        second=lastName
    if tempL=="[first]":
        second=firstName
    if tempL=="[last]":
        second=lastName
    if tempL==".[first]":
        second=firstName
    if tempL==".[last]":
        second=lastName
    if tempL=="first":
        second=firstName
    if tempL=="last":
        second=lastName
    if tempL=="[first_name]":
        second=firstName
    if tempL=="[last_name]":
        second=lastName
    if tempL=="firstname":
        second=firstName
    if tempL=="lastname":
        second=lastName
    if tempL=="Firstname":
        second=firstName
    if tempL=="Lastname":
        second=lastName
    if tempL=="jane":
        second=firstName
    if tempL=="john":
        second=firstName
    if tempL=="j":
        second=firstName[0]
    if tempL=="doe":
        second=lastName
    if tempL=="d":
        second=lastName[0]
    if tempL=="Jane":
        second=firstName
    if tempL=="John":
        second=firstName
    if tempL=="J":
        second=firstName[0]
    if tempL=="Doe":
        second=lastName
    if tempL=="D":
        second=lastName[0]
    if tempL=="Smith":
        second=lastName
    if tempL=="S":
        second=lastName[0]
    if tempL=="smith":
        second=lastName
    if tempL=="s":
        second=lastName[0]
    if tempL=="[last_initial]":
        second=lastName[0]
    if tempL=="[last name initial]":
        second=lastName[0]
    if tempL=="[first_initial]":
        second=firstName[0]
    if tempL=="[first initial]":
        second=firstName[0]
    if tempL=="lastinitial":
        second=lastName[0]
    if tempL=="[last initial]":
        second=lastName[0]
    if tempL=="firstinitial":
        second=firstName[0]
    if tempL=="[first name initial]":
        second=firstName[0]
    if tempL==" [last_initial]":
        second=lastName[0]
    if tempL==" [last name initial]":
        second=lastName[0]
    if tempL==" [first_initial]":
        second=firstName[0]
    if tempL==" lastinitial":
        second=lastName[0]
    if tempL==" firstinitial":
        second=firstName[0]
    if tempL==" [first name initial]":
        second=firstName[0]
    if tempL=="_[last name]":
        second=lastName
    if tempL=="_[last_name]":
        second=lastName
    if tempL==".[last name]":
        second=lastName
    if tempL==".[last_name]":
        second=lastName
    if tempL==" [last name]":
        second=lastName
    if tempL==" [last_name]":
        second=lastName
    if tempL=="_doe":
        second=lastName
    if tempL=="_Doe":
            second=lastName
    if linebreak=="]":
        linebreak="."
    if "_"==user[index]:
        linebreak="_"
    email=first+linebreak+second+domain
    if "[firstinitial][lastname]" in format:
       first=firstName[0]
       second=lastName
       email=first+second+domain
    if "jdoe" in format:
       first=firstName[0]
       second=lastName
       email=first+second+domain
    if "[firstnamelastname]" in format:
        first=firstName
        second=lastName
        email=first+second+domain
    if "[firstlast]" in format:
        first=firstName
        second=lastName
        email=first+second+domain
    if "[first.last]" in format:
        first=firstName
        second=lastName
        email=first+second+domain
    else:
        email=first+linebreak+second+domain
    return email