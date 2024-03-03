import random
import base64

def generate_random_answers(length=40):
    choices = ['A', 'B', 'C', 'D']
    return ''.join(random.choice(choices) for _ in range(length))

def encode_answers(answers):
    encoding_mapping = {'A': '00', 'B': '01', 'C': '10', 'D': '11'}

    # Group answers into pairs before encoding
    answer_pairs = [answers[i:i+2] for i in range(0, len(answers), 2)]

    binary_representation = ''.join([encoding_mapping[answer[0]] + encoding_mapping[answer[1]] for answer in answer_pairs])
    encoded_bytes = int(binary_representation, 2).to_bytes(len(binary_representation) // 8, byteorder='big')

    # Limit the base64 encoded string to 20 characters
    encoded_string = base64.b64encode(encoded_bytes).decode('utf-8')[:20]

    return encoded_string

def decode_answers(encoded_string, answer_length=40):
    decoding_mapping = {'00': 'A', '01': 'B', '10': 'C', '11': 'D'}

    # Pad the encoded string to ensure correct decoding
    encoded_string = encoded_string.ljust(20, '=')

    decoded_bytes = base64.b64decode(encoded_string)
    expected_binary_length = answer_length * 2

    binary_representation = format(int.from_bytes(decoded_bytes, 'big'), '0' + str(expected_binary_length) + 'b')

    decoded_answers = ''.join(decoding_mapping[binary_representation[i:i+2]] for i in range(0, len(binary_representation), 2))

    return decoded_answers

# Generate a random string of 40 answers
random_answers = generate_random_answers()
print(f"Random Answers: {random_answers}")

# Encode the random answers
encoded_string = encode_answers(random_answers)
print(f"Encoded String: {encoded_string}")

# Decode the encoded string back into answers
decoded_answers = decode_answers(encoded_string, len(random_answers))
print(f"Decoded Answers: {decoded_answers}")

# Verify the encoding and decoding process
assert random_answers == decoded_answers, "Mismatch in the original and decoded answers!"
print("Encoding and decoding verified successfully!")
