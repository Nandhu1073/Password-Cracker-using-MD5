# Password-Cracker-using-MD5


# MD5 Hash Cracker

This is a simple MD5 hash cracker implemented in Python. It takes an MD5 hashed password as input and tries to crack it by comparing it with a list of common passwords stored in a file named `wordlist.txt`.

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/md5-hash-cracker.git
    ```

2. Navigate to the project directory:

    ```bash
    cd md5-hash-cracker
    ```

3. Prepare the wordlist:
   - Create a file named `wordlist.txt` containing a list of passwords you want to try for cracking. Each password should be on a separate line.

4. Run the script with the MD5 hashed password as an argument:

    ```bash
    python md5_cracker.py <hashed_password>
    ```

    Replace `<hashed_password>` with the MD5 hash you want to crack.

5. Wait for the script to finish. If a match is found in the wordlist, the password will be displayed.

## Example

Suppose you have an MD5 hashed password `e10adc3949ba59abbe56e057f20f883e`. You can run the script as follows:

```bash
python md5_cracker.py e10adc3949ba59abbe56e057f20f883e

This project is licensed under the MIT License - see the LICENSE file for details.

typescript


Make sure to replace `yourusername` with your GitHub username and customize any other information specific to your project. Additionally, ensure that you have the `md5_cracker.py` script and the `wordlist.txt` file in your repository.
