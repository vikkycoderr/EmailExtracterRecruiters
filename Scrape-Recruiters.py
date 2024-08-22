from google_serp_api import ScrapeitCloudClient

api_key = 'your API key'
client = ScrapeitCloudClient(api_key)

def returnResults2(location):
    try:
        params = {
            "q": "site:linkedin.com/in " + location+" technical recruiter" + " talent acquisition",
            "gl": "us",
            "hl": "en",
            "location": location,
            "num": 100
        }

        response = client.scrape(params)

        data = response.json()
        return data

    except Exception as e:
        print(f"Error occurred: {e}")

def searchLinked(location):
    results=returnResults2(location)
    '''print("------------------RESULTS-------------------------")           #if you want to print JSON results you can uncomment this line
    print(results)'''            
    list_results = results["organicResults"]
    new_data=[]

    for i,_ in enumerate(list_results):
        data_for_new =[]
        if  "richSnippet" in list_results[i].keys():
            data_for_new.append(results["organicResults"][i]["richSnippet"]["top"]["extensions"][-1:][0])

        data_for_new.append(list_results[i]["title"])
        new_data.append(data_for_new)
    '''print("===========================NEW DATA===================================")   #if you want to print the list compiling all the recruiter info you can uncomment this line
    print(new_data)'''
    return new_data

