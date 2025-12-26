from bytez import Bytez

key = "a937e27bca105197c7d2c4124415781b"
sdk = Bytez(key)

# choose oh-dcft-v3.1-gemini-1.5-flash
model = sdk.model("mlfoundations-dev/oh-dcft-v3.1-gemini-1.5-flash")

# FIX: Assign to a single variable 'response'
response = model.run([
  {
    "role": "user",
    "content": "Hello"
  }
])

# Print the full response to see the structure
print(response)