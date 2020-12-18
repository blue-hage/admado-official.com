#!/usr/local/bin/python3
from flask import request
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

USER_NAME_CONTACT = "contact@admado-official.com"
USER_NAME_CLIENT = "client@admado-official.com"
PASSWORD_CONTACT = "20201202"
PASSWORD_CLIENT = "20201203"
ADMADO_RECIPIENT_CONTACT = "contact-receiver@admado-official.com"
ADMADO_RECIPIENT_CLIENT = "client-receiver@admado-official.com"

def contact_create(email, name, contents):
  body1 = """
  {0}様

  当サイトをご覧頂きありがとうございます。
  お問い合わせを承りました。
  返信に多少のお時間を頂く事がございます。
  ご理解・ご協力をよろしくお願い致します。

  * こちらは自動返信メールとなっております。ご返信はお控え下さい。

  (お問い合わせ内容)
  お名前: {0}様
  メールアドレス: {1}
  内容: {2}
  """.format(name, email, contents)

  msg1 = MIMEText(body1)
  msg1["Subject"] = "お問い合わせ完了"
  msg1["From"] = USER_NAME_CONTACT
  msg1["To"] = email

  body2 = """
  お名前: {0}
  メールアドレス: {1}
  お問い合わせ内容: {2}
  """.format(name, email, contents)

  msg2 = MIMEText(body2)
  msg2["Subject"] = "お問い合わせの受付"
  msg2["From"] = USER_NAME_CONTACT
  msg2["To"] = ADMADO_RECIPIENT_CONTACT
  
  msg = [msg1, msg2]
  return msg


def client_create(email, tel, company, user, contents, attachment):

  if attachment is not None:
    design = request.files['design']
    filename = design.filename
  else:
    filename = "無し"


  body1 = """
  {0}様

  当サイトをご覧頂きありがとうございます。
  当社サービスへの広告掲載申込を承りました。
  返信に多少のお時間を頂く事がございます。
  ご理解・ご協力をよろしくお願い致します。

  * こちらは自動返信メールとなっております。ご返信はお控え下さい。

  (受付内容)
  企業（個人）名: {0}様
  ご担当者様: {1}様
  メールアドレス: {2}
  電話番号: {3}
  デザインファイル: {4}
  その他: {5}
  """.format(company, user, email, tel, filename, contents)

  msg1 = MIMEText(body1)
  msg1["Subject"] = "広告掲載応募"
  msg1["From"] = USER_NAME_CLIENT
  msg1["To"] = email

  body2 = """
  企業（個人）名: {0}
  ご担当者様: {1}
  メールアドレス: {2}
  電話番号: {3}
  デザインファイル: {4}
  その他: {5}
  """.format(company, user, email, tel, filename, contents)

  msg2 = MIMEMultipart()
  msg2["Subject"] = "広告掲載申込"
  msg2["From"] = USER_NAME_CLIENT
  msg2["To"] = ADMADO_RECIPIENT_CLIENT
  body2 = MIMEText(body2)
  msg2.attach(body2)

  if attachment is not None:
    fp = open(attachment, 'rb')
    img = MIMEImage(fp.read())
    fp.close()
    img.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg2.attach(img)
  
  msg = [msg1, msg2]
  return msg