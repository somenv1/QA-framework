from transformers import pipeline
pipe = pipeline('text2text-generation',model="valhalla/t5-base-qg-hl")
text = input("Enter context to generate question:")
prompt = "Generate an question based on the following:" + text
pipe(prompt)