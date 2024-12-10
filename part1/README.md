
Here is the updated `README.md` content with the steps outlined:

---

# Part 1 of the problem set (ECB and CTR encryption)

## Subpart 1
In this subpart, students will be asked to implement ECB and CTR encryption modes based on their knowledge learned during a lecture. On our part, we provide an empty python script file, where students will write their code. In order to make the problem more interesting, we would like to ask students to upload their own image and apply two types of encrytpion on it. Then, they should briefly describe the differences between ECB and CTR and their implications on security in the comment section of their code. 

## Subpart 2
In the second subpart, students will carry out frequency distribution analysis. They only need to writte a code to plot a graph of frequency distribution, we will provide an ECB encrypted text. Here are the step-by-step explanation of this subpart:

1. **Launch the Flask server**:
   ```
   python app.py
   ```
2. **Request the ECB encrypted text**:

   Students need to send their Harvard ID to the server, which would uniquely identify them.
   ```
   curl "http://localhost:8080/get_text?id=123"
   ```
   The server will return an ECB encrypted text to a student. They would get something like:
   ```
   {"selected_text":"B QQWBPS WXY WS BYN WWSS XWTSSVD WWVV BSNSQ NBUS FYYK BKNWPSV"}
   ```
3. **After performing the frequency disitrbution analysis and decrypting the text, students would check whether their answer is correct by sending the check request to the server**
   ```
   curl "http://localhost:8080/check?id=123&text=all%20happy%20families%20are%20alike%20each%20unhappy%20family%20is%20unhappy%20in%20its%20own%20way"
   ```
   Here `%20` represents a space, but later we would consider making sending the request much easier for the students.

   If their answer is correct, then the server will send the "Correct!" message; otherwise, "Try Again!" would be received.

**Important point**:
- We are thinking of having a launched server that will handle the backend stuff like storing the encrypted texts for each student's ID and checking the answer. Right now, we are using a smiple .txt file to store the mapping (Student ID - encrypted text); however, we are open to more complex solutions that would make the grading process easier for the CS50 stuff. 
- Also, we are planning to have a pool of plaintexts, from which a randomly selected text would be given to a student. If there were only one text, it would be too trivial for students. So, we hope this would add some complexity to the task and makes it more engaging.
