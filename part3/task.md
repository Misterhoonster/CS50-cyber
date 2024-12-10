In this section, you will explore how the signatures work in the encryption system. In general, signatures do ensure the integrity and authenticity of the messages; however, it is not a panacea. One could possibly find many ways to crack or perform attacks on signed messages. That is what you are going to figure out. 


Again, David Malan is the main character of this section. Suppose David wants to send a signed message to his friend in another state. Also, assume that there is an attacker that can intercept and see the communication between the two endpoints. You are going to take the role of David's friend expecting a message from him.  

Part 1: 
David did well on his CS security course at the College. So, he decides to append the same signature to his plaintext messages. As a signature he decides to use his public key ecnrypted using his private key. However, do not forget that an attacker is constantly monitoring the communication channel. 

(a) Why David using the same signature every time he sends a message to you is problematic? What could an attacker possibly do?

(b) So, a dumb attacker sees how David is appending some signature to his cleartext messages, so he decides to add his own random number of the same length.  Suppose that you get two identical messages but with different signatures. Which one of them belongs to David?

Part 2:
You tell David that there is someone in between you who is intercepting messages, then he figures to act smarter this time. Instead of encrypting his public key, David chooses encrypt the cleartext message itself with his private key and use it as a signature. It means that each message will get a unique signature, and thus, an attacker will not be able to change the content of a message as it will break the signature. Hence, David is confident that the integrity of messages is preserved. Moreover, David claims that this new approach helps him make sure that the messages are sent by him and only him since only he has the private key that he used to create a signature. 

(a) Which one of David's assumtpions regarding the new approach is wrong? Why?

Part 3:
In part 2, you figured out where the new approach of David to encrypt messages with his private key to create signatures falls short. Based on that, to address that problem from part 2 and to finally ensure that an attacker can not perform any malicious attacks, what could David possibly modify the signature? 