# Script for writing html script for demo site

def a(link, name):
    # Example: 
    # <a target=blank href=https://oecd.ai/en/incidents?search_terms=%5B%5D&and_condition=false&from_date=2014-01-01&to_date=2024-07-05&properties_config=%7B%22principles%22:%5B%5D,%22industries%22:%5B%5D,%22harm_types%22:%5B%5D,%22harm_levels%22:%5B%5D,%22harmed_entities%22:%5B%5D%7D&only_threats=false&order_by=date&num_results=20>
    #- OECD AI Incidents Monitor (AIM)</a> <br></br>

    s1 = "<a target=blank href="
    s2 = link
    s3 = ">-"
    s4 = name
    s5 = "</a><br></br>"

    return s1+s2+s3+s4+s5

