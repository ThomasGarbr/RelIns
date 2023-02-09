import sqlite3
import json
import re

tweets = []
for pack in range(1646, 1713):
    with open(f"crawl_json/crawl_1646_0.json", 'r', encoding="utf8") as json_file:
        data = json.loads(json_file.read())
        for i in range(len(data)):
            if not re.findall(r'\b([a-z]+[.]*[A-Z]+)', data[f'{i}']["maintext"]) and "This copy is for your personal" not in data[f'{i}']["maintext"] and "»" not in data[f'{i}']["maintext"]:
                to_append = data[f'{i}']["maintext"][:500]
                ind = to_append.rfind('. ')
                tweets.append(to_append[:ind+1])
        
db = sqlite3.connect("EmoPicker/db.sqlite3")
c = db.cursor()

query = "insert into Homepage_datasettext(text,rating) values (?,?)"
for i in tweets:
    c.execute(query, (i, 0))
    db.commit()
c.close()

