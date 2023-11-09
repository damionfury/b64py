# Reimplementing base64 encode and decode
I learn better when I have a goal in mind. After seeing an article about how base64 encode and decode functions work, I got it in my head to write my own implementation in python.

## Goal
Create a module that offers base64 encode and decode

## Roadmap
1. Make a function that can base64 encode a string [done]
2. Make a function that can base64 decode a string [done]
3. Modify the functions to work with any data [done]
4. Turn it into a module that can be imported. [done]
5. Make it throw errors properly [done]
6. Create a complete set of unit tests. [in progress]

## Can I use this?
Yes, but why? There is no rational reason for you to use this. Still – if you're dead set on making bad decisions – it's licensed CC0. I'd kinda prefer you left my name out of it.

## How do I use this?
Import it like any other package. It has two functions:
- `encode()` - Accepts any object and returns a base64 encoded string representation
- `decode()` - Accepts a base64 string and an optional parameter for output type.
    - If no output type is provided, it returns the decoded string as a string.
    - If output type is provided, it must be 'string' or 'bytearray' and will return the decoded string as the specified type.