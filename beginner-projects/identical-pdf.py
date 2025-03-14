import hashlib
from difflib import SequenceMatcher
import fitz

def hash_file(fileName1, fileName2):

  h1 = hashlib.sha1()
  h2 = hashlib.sha1()

  with open(fileName1, "rb") as file:
    chunk = 0
    while chunk != b"":
      chunk = file.read(1024)
      h1.update(chunk)

  with open(fileName2, "rb") as file:
    chunk = 0
    while chunk != b"":
      chunk = file.read(1024)
      h2.update(chunk)

  return h1.hexdigest(), h2.hexdigest()

def hash_pdf_text(fileName):
  h = hashlib.sha1()
  doc = fitz.open(fileName)

  full_text = ""
  for page in doc:
    text = page.get_text("text")
    clean_text = text.strip().lower().replace(" ", "").replace("\n", "")
    full_text += clean_text

  h.update(full_text.encode("utf-8"))
  return h.hexdigest()

msg1, msg2 = hash_file("pd1.pdf", "pd2.pdf")
# msg1, msg2 = hash_file("pd1.pdf", "pd1.pdf")

msg1_text = hash_pdf_text("pd1.pdf")
msg2_text = hash_pdf_text("pd2.pdf")

if (msg1 != msg2):
  print("These files are not identitcal")
else:
  print("These files are identical")

if (msg1_text != msg2_text):
  print("These files are not identitcal")
else:
  print("These files are identical")