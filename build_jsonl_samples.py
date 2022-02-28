import sys

assetNames = [
    "jmsac",
    "jmsba",
    "jmsa",
    "jmsc",
    "omhq169a",
    "omhq169b",
    "omsdp1233",
    "vx1232",
    "vx2342",
    "omhqv2134",
    "omhqp2342",
    "prod141",
    "po02",
    "xtst043",
    "dev123",
    "test324",
    "po03",
]

samples = {
        "getstatus":
        [
            "Get status of NAME.",
            "What is the status of NAME?",
            "How is NAME?",
            "Tell me how NAME is doing.",
        ],
        "getdependencies":
        [
            "What depends on NAME?",
            "What apps are related to NAME?",
            "If NAME goes down, what is impacted?",
            "What is impacted by NAME?",
        ],
        "gethistory":
        [
            "When did NAME go down?",
            "When was the last alert for NAME?",
            "How long has NAME been down?",
        ]
}
# Structure
# {"text": "What is the status of {ASSET_NAME}?","label": "GetStatus", "metadata": {"source":"example.com"}}

f = open("train_set_2.jsonl", "w")
for k in samples.keys():
    intent = k
    for s in samples[k]:
        for a in assetNames:
            line = s.replace("NAME", a)
            sample = "{\"text\": \"%s\", \"label\": \"%s\", \"metadata\": {\"source\": \"uprr.com\"}}\n" % (line, intent)
            f.write(sample)

f.close()