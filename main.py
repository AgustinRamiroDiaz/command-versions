import os

token = os.getenv("OKTETO_TOKEN")
print(token[0] + "..." + token[1:])
