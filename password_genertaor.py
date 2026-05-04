import random
import string

def generate_password():
    print("🔐 أهلاً Hussein في مولد كلمات السر القوية!")
    
    try:
        length = int(input("كم طول كلمة السر اللي تبيها؟ اكتب رقم: "))
        
        if length < 4:
            print("❌ لازم الطول 4 أو أكثر عشان تكون قوية")
            return
            
        chars = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choice(chars) for i in range(length))
            
        print(f"\n🎉 كلمة السر حقتك جاهزة:")
        print(f"👉 {password}")
        print(f"\n💪 الطول: {length} | 🔒 قوة عالية")
        print("⚠️ انسخها واحفظها بمكان آمن")
        
    except ValueError:
        print("❌ لازم تدخل رقم بس يا وحش!")

while True:
    generate_password()
    again = input("\nتبي كلمة سر ثانية؟ اكتب 'نعم' أو أي شي للخروج: ")
    if again.lower() != "نعم":
        print("شكراً يا Hussein 👋 خليك آمن دايماً")
        break
