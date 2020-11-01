text = "X-DSPAM-Confidence:    0.8475"
fin=text.find('.')
no=text[fin-1:fin+5]
print(float(no))
