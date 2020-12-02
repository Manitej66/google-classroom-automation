# 💻 google-classroom-automation

This is a Python automation script that attends online classes (Google classroom) on your behalf 😉

## 👀 Features

- Automatic joining in all classes from timetable in single click
- Custom timetable support
- Sends message if a specific keyword is called
- Custom keyword support

## 🤖 Requirements

- PyAutoGUI
- selenium

## ❓ How to run the script :

1. Clone the repo
2. Open terminal in folder and run the below code

   ```python
   pip install -r requirements.txt
   ```

3. Go to [Chrome driver download](https://chromedriver.chromium.org/downloads) and download the driver specific to your chrome version

4. Extract the zip in `C:\Program Files (x86)` directory

5. Go to `today_classes.py` and replace `alertWords` , `classes` and `subjects` with your time table

6. Go to `today_classes.py` line 81 and enter your email

7. Go to `today_classes.py` line 88 and enter your email password

8. That's it. There are 3 options in the script

   - get today periods

   ```python
   class -t
   ```

   - join a specific period

   ```python
   class -subject_name
   ```

   - automate today classes

   ```python
   class -a
   ```

## 📚 Reference repos

1. https://github.com/kathir-t/GoogleMeet_CallAlerter

2. https://github.com/ItsDandelia/Google-Meet-Auto-SignIn

3. https://github.com/theunhackable/google-classroom-automation
