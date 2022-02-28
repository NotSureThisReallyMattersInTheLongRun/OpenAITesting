
import openai
import sys
import json


working_dir = "/Users/cjduggan/projects/python_testing"
fileName = f"built_model.dat"
openai.api_key = "{your key}"
#result = openai.File.create(
#    file=open("train_set_2.jsonl"), 
#    purpose="classifications",
#    user_provided_filename= fileName
#    )

#print(result)
#exit(1)

prompt = "%"
while True:
    line = input("%")
    if 'q' == line.rstrip():
        break
    result = openai.Classification.create(
        file="file-WYPs5jIFjnwNqhtzKOAb27Fb",
        query=line.rstrip(),
        search_model="ada", 
        model="curie", 
        max_examples=3
    )
    sys.stdout.write(result.get("label"))
    sys.stdout.write("\n")

print("Exited")
