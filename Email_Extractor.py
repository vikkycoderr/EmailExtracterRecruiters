import Recruiter_Email_Formatter
import Scrape_Recruiters
import EmailFormatProviderChatGPT

results=Scrape_Recruiters.searchLinked("Jacksonville, Florida") #the location you are scraping
company=""
title=""
def nameExtractor(title2):
    firstName=""
    lastName=""
    counterDashDot=0
    counterSpace=0
    name=""
    for i in title2:
        if i=="-" or i=="." or i==",":
            counterDashDot+=1
        if i==" ":
            counterSpace+=1
        if counterDashDot==1 or counterSpace==2:
            break
        name+=i
    index=0
    for j in name:
        if index==0: 
            if j != " ":
                firstName+=j
        if index==1:
            lastName+=j
        if j==" ":
            index+=1
    return [firstName,lastName]
lastCompany=""
lastResponse=""
for i in results:
    if len(i[0])>0:
        company=i[0]
    try:
        if len(i[1])>0:
            if company!=lastCompany:
                response = EmailFormatProviderChatGPT.getChatResponse(company)
                lastCompany=company
                lastResponse=response
            else:
                response=lastResponse
            print("Email: "+Recruiter_Email_Formatter.seperater(nameExtractor(title)[0],nameExtractor(title)[1],response))

    except IndexError:
        title=i[0]
        counterDash=0
        word=""
        for a in i[0]:
            if a=="-":
                counterDash+=1
        if counterDash==2:
            for j in i[0]:
                if j!="-":
                    word+=j
                else:
                    word=""
            company=word
            print("Email: "+Recruiter_Email_Formatter.seperater(nameExtractor(title)[0],nameExtractor(title)[1],EmailFormatProviderChatGPT.getChatResponse(company)))
        else:
            print("Enough Info Not Present")



        



