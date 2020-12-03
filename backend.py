from flask import request, redirect
from email.mime.text import MIMEText
from email.utils import formatdate

USER_NAME = "contact@admado-official.com"
ADMADO_RECIPIENT = "contact-receiver@admado-official.com"

def contact_create():
  email = request.form.get("email")
  name = request.form.get("name")
  contents = request.form.get("contents")

  body1 = """
  当サイトをご覧いただきありがとうございます。<br>
  お問い合わせを承りました。<br>
  返答に多少のお時間をいただく事があります、ご理解の方の方をよろしくお願い致します。<br>
  * こちらは自動返信用メールとなっております。
  """

  msg1 = MIMEText(body1, "html")
  msg1["Subject"] = "お問い合わせ完了"
  msg1["From"] = USER_NAME
  msg1["To"] = email

  body2 = """
  お名前: {0}<br>
  メールアドレス: {1}<br>
  お問い合わせ内容: {2}<br>
  """.format(name, email, contents)

  msg2 = MIMEText(body2 , "html")
  msg2["Subject"] = "お問い合わせの受付"
  msg2["From"] = USER_NAME
  msg2["To"] = ADMADO_RECIPIENT
  
  msg = [msg1, msg2]
  return msg


def client_create():
  email = request.form.get("email")
  tel = request.form.get("tel")
  name = request.form.get("name")
  contents = request.form.get("contents")

  body1 = """
  当サイトをご覧いただきありがとうございます。
  お問い合わせを承りました。
  返答に多少のお時間をいただく事があります、ご理解の方の方をよろしくお願い致します。
  * こちらは自動返信用メールとなっております。
  """

  msg1 = MIMEText(body1, "html")
  msg1["Subject"] = "お問い合わせ完了"
  msg1["From"] = USER_NAME
  msg1["To"] = email

  body2 = """
  お名前: {0}
  メールアドレス: {1}
  お問い合わせ内容: {2}
  """.format(name, email, contents)

  msg2 = MIMEText(body2 , "html")
  msg2["Subject"] = "お問い合わせの受付"
  msg2["From"] = USER_NAME
  msg2["To"] = ADMADO_RECIPIENT
  
  msg = [msg1, msg2]
  return msg