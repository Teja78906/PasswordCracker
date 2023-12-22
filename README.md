# Web Login Bruteforce Tool

This Python script is a simple web login bruteforce tool that attempts to find the correct username and password for a given page URL.

## Usage

1. **Setup:**

   - Install the required modules by running:

     ```bash
     pip install requests termcolor
     ```

2. **Run the Script:**

   - Execute the `bruteforce.py` script:

     ```bash
     python bruteforce.py
     ```

   - The script will prompt you to enter the page URL, the username for the account to bruteforce, the password file, and other optional parameters.

3. **Parameters:**

   - **Page URL:** The URL of the login page.
   - **Username:** The target username for bruteforcing.
   - **Password File:** The file containing the list of passwords to try.
   - **Login Failed String:** String that indicates a login failure.
   - **Cookie Value (Optional):** Provide a cookie value if needed for the request.

4. **Output:**

   - The script will print the attempts and notify you if a valid username and password are found.

## Files

- `bruteforce.py`: Contains the bruteforce script.
- `passwords.txt`: Example password file.

## Dependencies

- `requests`: HTTP library for making requests.
- `termcolor`: Colored output for the terminal.

## Disclaimer

This script is for educational purposes only. Unauthorized access to systems or accounts is illegal and unethical. Use responsibly and only on systems you have explicit permission to test.

## License

This project is licensed under the [MIT License](LICENSE).
