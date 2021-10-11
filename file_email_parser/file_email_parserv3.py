import imaplib
import os
import email


class AttachmentsParser:
    def __init__(self, login, password, path_folder):
        self.path_folder = path_folder
        self.password = password
        self.login = login

    def login_email(self):
        self.mail = imaplib.IMAP4_SSL('imap.gmail.com', 993)
        self.mail.login(self.login, self.password)
        self.mail.select('Inbox')
        self.type, self.data = self.mail.search(None, 'ALL')

    def download_attachment(self):
        for num in self.data[0].split():
            typ, data = self.mail.fetch(num, '(RFC822)')
            raw_email = data[0][1]
            raw_email_string = raw_email.decode('latin-1')
            email_message = email.message_from_string(raw_email_string)
            for part in email_message.walk():
                if part.get_content_maintype() == 'multipart':
                    continue
                if part.get('Content-Disposition') is None:
                    continue
                file_name = part.get_filename()
                if file_name is not None:
                    if file_name.startswith("map_"):
                        file_name = file_name + '.png'
                if bool(file_name):
                    file_path = os.path.join(self.path_folder, file_name)
                    if not os.path.isfile(file_path):
                        h = email.header.make_header(email.header.decode_header(file_name))
                        with open(str(h), 'wb') as new_file:
                            new_file.write(part.get_payload(decode=True))
                    print(f'Downloaded: {file_name}')


parser = AttachmentsParser('*********@gmail.com', '****************', 'C:\Python_work\email_parser')
parser.login_email()
parser.download_attachment()
