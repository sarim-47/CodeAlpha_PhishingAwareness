import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    print("=" * 60)
    print("      CODEALPHA CYBER SECURITY AWARENESS TRAINING MODULE      ")
    print("                 Topic: Phishing Mitigation                  ")
    print("=" * 60 + "\n")

def run_tutorial():
    clear_screen()
    print_header()
    print("[*] LESSON 1: WHAT IS PHISHING?")
    print("    Phishing is a social engineering attack where bad actors impersonate")
    print("    legitimate brands (Banks, Google, Netflix) to steal credentials.\n")
    time.sleep(2)
    
    print("[*] LESSON 2: IDENTIFYING RED FLAGS")
    print("    1. Sender Spoofing: Look closely at the domain (e.g., @netf1ix.com).")
    print("    2. Urgent Tone: Threatening account suspension within hours.")
    print("    3. Suspicious Links: Mismatched hyperlinked URLs.\n")
    input("\nPress Enter to start the Interactive Quiz and test your skills...")

def run_quiz():
    clear_screen()
    print_header()
    score = 0
    
    # Question 1
    print("[?] QUESTION 1:")
    print("You receive an urgent email from 'security@paypa1-support.com' stating")
    print("your account is locked. It asks you to click a link to verify your identity.")
    print("\nIs this email legitimate or a phishing attempt?")
    print("1. Legitimate")
    print("2. Phishing Attempt")
    
    ans1 = input("\nChoose option (1 or 2): ")
    if ans1 == "2":
        print("\n[+] CORRECT! Notice the typo 'paypa1' (with a number 1 instead of l). This is Typosquatting.")
        score += 1
    else:
        print("\n[-] INCORRECT! The domain 'paypa1.com' is fake. Real domain is paypal.com.")
    
    input("\nPress Enter for the next scenario...")
    clear_screen()
    print_header()

    # Question 2
    print("[?] QUESTION 2:")
    print("An email claims you won a $1000 Amazon gift card. The sender address is")
    print("'rewards@amazon.com', but the tracking link points to 'http://bit.ly/claim-prize99'.")
    print("\nWhat should you do?")
    print("1. Click the link immediately before it expires.")
    print("2. Do not click. Inspect the shortened URL and verify on official portal.")
    
    ans2 = input("\nChoose option (1 or 2): ")
    if ans2 == "2":
        print("\n[+] CORRECT! Shortened URLs (like bit.ly) are heavily used to hide real destination paths.")
        score += 1
    else:
        print("\n[-] INCORRECT! Clicking generic shortened links can lead to credential harvesting pages.")

    # Final Results
    input("\nPress Enter to view your Performance Report...")
    clear_screen()
    print_header()
    print(f"[#] TRAINING COMPLETED!")
    print(f"    Your Total Score: {score}/2")
    if score == 2:
        print("    Result: EXCELLENT! You can successfully spot phishing vectors.")
    else:
        print("    Result: NEEDS IMPROVEMENT. Always analyze domains and URLs carefully.")
    print("\n" + "=" * 60)

if __name__ == "__main__":
    run_tutorial()
    run_quiz()
