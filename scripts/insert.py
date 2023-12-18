import openai

# Set your OpenAI API key
api_key = "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"

# Set the OpenAI API key
openai.api_key = api_key

# Read the schema from the file
with open('schema.txt', 'r') as file:
    schema_content = file.read()

with open('cred.txt', 'r') as file:
   cred_content = file.read()

# Specify a larger number of data items in the prompt
num_data_items = 1000  # You can adjust this number based on your needs
prompt = f"Generate {num_data_items} data items and create tables with the following schema: {schema_content} to create table and insert it to mysql database using python script using faker and use this connection: {cred_content} "

# Set up and make the API request
response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.7,
    max_tokens=3000,  # Adjust max_tokens based on the desired length of the generated data
    stop=None
)

# Extract the generated data from the response
generated_data = response['choices'][0]['text']

# Process the generated data as needed
print("Generated Data:", generated_data)

# Write the generated data to a file
output_file_path = 'generated_data.py'
with open(output_file_path, 'w') as output_file:
    output_file.write(generated_data)

