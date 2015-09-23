# decryption

This is a brief program that I wrote to decrypt a single encrypted message. The methodology was straight forward (and also not fully automated).

$ Note: I am currently working on a more generalized version of this algorithm that will take a message encrypted in the same manner as this and give all possible decodings. This new program can be found in the decrypt2 repository. As of September 23rd, 2015, it is still incomplete.

I took the longest word in the message; in this case, it happened to be twelve letters long. I then downloaded a dictionary that consisted of English words that are twelve letters long. I then had the program run through to eliminate which words would still qualify (ie, the twelve letter word had a double letter by starting with "szz...". As such, any twelve letter words that didn't share the same 2nd and 3rd letter were eliminated).

This left me with a list of about 30 possibilities for the longest word in the code. I had the program run through the rest of the code using the key that was created from the longest word. However, there was also a one letter word in the encrypted message; this letter also appeared in the twelve letter word. I was then able to eliminate any possibilities where the single letter was not a word (in English, the only single letter words are "a", "I" and "o"). This left me with five possible results. From there, it was easy to brute force solve the message.


