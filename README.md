# AES-Encrypted-Communication
Python implementation of a server-client encrypted communication program using my own algorithms for ECB and CBF (Advanced Encryption Standard argorithms)
**Program Flow**:
  - A sends B and KM(key manager) the encryption method (ECB/CBF)
  - KM encrypts a random key and sends it to A
  - A sends B the encrypted key
  - Both A and B  decrypt the key
  - A and B exchange messages encrypted with the selected encryption method, using the key from KM 
