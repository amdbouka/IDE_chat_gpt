# IDE_chat_gpt
run your chat_gpt command on IDE and save results in files automatically. 
'''Important:You need to add your chat_gpt API in .env file to run the code'''


This Python code takes user input for a task description and sends a request to OpenAI's API to generate code for that task. The API used here is the OpenAI GPT-3 API.

The code prompts the user to input the task description and sets up the API endpoint and API key for OpenAI. It then sets up the request headers and data to send a POST request to the API endpoint.

The request data includes the GPT-3 model to use, the user prompt as the task description, the maximum number of tokens to generate in the response, and the temperature parameter for controlling the randomness of the generated code.

After sending the request, the code checks if a file with the same name already exists and increments the serial number if it does. It then generates a unique file name and saves the response code to the output file. If the request is unsuccessful, the code outputs a message indicating the status code of the failed request.
