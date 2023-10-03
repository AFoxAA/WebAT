import smtplib
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

your_email = 'your_email'
receiver_email = 'receiver_email'
password = 'your_password'
report_name = 'log.txt'

msg = MIMEMultipart()
msg['From'] = your_email
msg['To'] = receiver_email
msg['Subject'] = 'Отчет о тестировании ...'
email_text = 'Результат о тестировании проекта "..."'

msg.attach(MIMEText(email_text))

try:
    with open(report_name, 'rb') as file:
        part = MIMEApplication(file.read(), Name=basename(report_name))
        part['Content-Disposition'] = f'attachment; filename="{basename(report_name)}"'
        msg.attach(part)
except FileNotFoundError:
    print(f"Ошибка: Файл '{report_name}' не найден.")
except Exception as e:
    print(f"Ошибка при чтении файла: {str(e)}")

try:
    server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
    server.login(your_email, password)
    email_message = msg.as_string()
    server.sendmail(your_email, receiver_email, email_message)
    server.quit()
    print("Письмо успешно отправлено")
except Exception as e:
    print(f"Ошибка при отправке письма: {str(e)}")
