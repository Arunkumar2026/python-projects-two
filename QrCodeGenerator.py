import qrcode as qr
img = qr.make("https://www.geeksforgeeks.org/python/python-projects-beginner-to-advanced/")
img.save("PythonProjects.png")