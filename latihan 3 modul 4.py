def login():
    # User credentials
    username = "mahasiswa"
    password = "12345"

    # Authentication
    input_username = input("Masukkan username: ")
    input_password = input("Masukkan password: ")

    return input_username == username and input_password == password

def input_mata_kuliah():
    if login():
        mata_kuliah = input("Masukkan nama mata kuliah: ")
        dosen = input("Masukkan nama dosen pengampuh: ")
        print("Mata kuliah", mata_kuliah, "diampu oleh", dosen)
    else:
        print("Login gagal.")

if __name__ == "__main__":
    input_mata_kuliah()